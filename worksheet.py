from argparse import ArgumentError
import time
import gspread
import pwinput
from google.oauth2.service_account import Credentials
from colors import Color as col
from art import print_logo

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hight_low_game')

accounts = SHEET.worksheet('acounts')
accounts_list = accounts.get_all_values()
usernames = [lst[0] for lst in accounts_list]


def ask_if_returning_user():
    """
    Get information for new or returning user
    """
    print_logo()
    print(col.BLUE + "Welcome to Higher/Lower game\n")
    while True:
        question = input("Are you a returning user? (Y/N): ")
        if question.lower() != "y" and question.lower() != "n":
            print_logo()
            print("Type 'Y' for yes or 'N' for no")
        else:
            print_logo()
            print("Ok...")
            break
    return question.lower()


def ask_for_username():
    """
    Ask for username and check if it's available
    """
    print("Let's create a new account for you.")
    time.sleep(3)
    keep_looping = True
    while keep_looping:
        keep_looping = False
        print_logo()
        input_name = input("Type new username: ")
        for lst in accounts_list:
            if input_name == lst[0]:
                print("This username already in use. Try again.")
                time.sleep(3.5)
                keep_looping = True
    print_logo()
    print(f"Welcome {input_name}")
    time.sleep(3)
    return input_name


def ask_for_passcode():
    """
    Create new user passcode
    """
    print_logo()
    passcode = pwinput.pwinput(prompt="Create your passcode: ")
    return passcode


def log_in_username():
    """
    Ask user to login by entering username and check if username exists
    """
    while True:
        print_logo()
        old_user = input("Enter your username: ")
        if old_user == "exit":
            print(col.RED + "Login failed")
            time.sleep(3)
            return False
        if old_user not in usernames:
            print(col.YELLOW + f"There is no account with username {old_user}")
            print('You can try again or type "exit" to start over')
            time.sleep(4)
        else:
            print(f"\nWelcome back {old_user}")
            time.sleep(2)
            break
    return old_user


def log_in_passcode(username):
    """
    Ask for current user password and check if match
    @param username(string): Username typed by user
    """
    for lst in accounts_list:
        if lst[0] == username:
            curent_account = lst
    while True:
        print_logo()
        existing_pass = pwinput.pwinput(prompt=f"Passcode for {username}: ")
        if existing_pass == "exit":
            print(col.RED + "Login failed")
            time.sleep(3)
            break
        if existing_pass == curent_account[1]:
            print(col.GREEN + "Login successful")
            time.sleep(3)
            return True
        else:
            print(col.RED + "Wrong passcode!")
            print('You can try again or type "exit" to start over')
            time.sleep(3)


def create_new_account(name, passcode, new_score=0):
    """
    Create a new account
    @paran name(string): New username
    @param passcode(string): New passcode for the above username
    @param new_score(int): Gives a default zero value to populate the worksheet
    """
    print_logo()
    n_account = [name, passcode, new_score]
    return n_account


def upload_new_acount(lst):
    """
    Update worksheet with new account
    @param lst(list): A list to be appended as a new row to the worksheet
    """
    try:
        accounts.append_row(lst)
    except ValueError as error:
        print(f"{error} at account creation")
        user_account_login()
    else:
        print_logo()
        print(col.GREEN + "Account successfully created.\n")
        time.sleep(4)


def user_account_login():
    """
    Guide the user through login or account creation
    """
    returning_player = ask_if_returning_user()
    if returning_player == "n":
        global new_username
        new_username = ask_for_username()
        new_passcode = ask_for_passcode()
        new_account = create_new_account(new_username, new_passcode)
        upload_new_acount(new_account)
        return True
    if returning_player == "y":
        global old_user
        old_user = log_in_username()
        if old_user is False:
            return False
        decision = log_in_passcode(old_user)
        return decision


def update_score(num):
    """
    Push the score to Google worksheet and update the cell
    @param num(int): The new score to be pushed to worksheet
    """
    print_logo()
    print("Updating score...")
    time.sleep(2)
    new_accounts = SHEET.worksheet('acounts')
    try:
        to_finde = new_accounts.find(new_username)
        cor1 = to_finde.row
        cor2 = to_finde.col
        new_accounts.update_cell(cor1, cor2 + 2, num)
        print("Score updated successfully.")
    except ArgumentError:
        to_finde = new_accounts.find(old_user)
        cor1 = to_finde.row
        cor2 = to_finde.col
        new_accounts.update_cell(cor1, cor2 + 2, num)
        print("Score updated successfully.")
