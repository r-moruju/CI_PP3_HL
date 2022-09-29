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
    print(col.BLUE + "Welcome to Higher/Lower game.\n".center(80))
    while True:
        question = input("Are you a returning user? (Y/N):\n ".center(80))
        if question.lower() != "y" and question.lower() != "n":
            print_logo()
            print(col.YELLOW + "Type 'Y' for yes or 'N' for no.".center(80))
        else:
            print_logo()
            print("Ok...".center(80))
            break
    return question.lower()


def ask_for_username():
    """
    Ask for username and check if it's available
    """
    print("Let's create a new account for you.".center(80))
    time.sleep(3)
    keep_looping = True
    while keep_looping:
        keep_looping = False
        print_logo()
        input_name = input("Type new username:\n ".center(80))
        if len(input_name) < 2 or len(input_name) > 12:
            print(col.RED + "Username must be between 2 - 12 characters long.".center(80))
            print(col.RED + "Please try again.\n".center(80))
            time.sleep(3)
            keep_looping = True
            continue
        for lst in accounts_list:
            if input_name == lst[0]:
                print(col.RED + "This username already in use. Try again.".center(80))
                time.sleep(3.5)
                keep_looping = True
    print_logo()
    print(col.BLUE + f"Welcome {input_name}.".center(80))
    time.sleep(3)
    return input_name


def ask_for_passcode():
    """
    Create new user passcode
    """
    while True:
        print_logo()
        passcode = pwinput.pwinput(prompt="Create your passcode:\n ".center(80))
        if len(passcode) <= 3:
            print(col.RED + "Passcode must be longer than 3 characters".center(80))
            time.sleep(3)
            continue
        return passcode


def log_in_username():
    """
    Ask user to login by entering username and check if username exists
    """
    while True:
        print_logo()
        user = input("Enter your username:\n ".center(80))
        if user == "exit":
            print(col.RED + "Login failed.".center(80))
            time.sleep(3)
            return False
        if user not in usernames:
            print(col.YELLOW + f"There is no account with username {user}.".center(80))
            print('You can try again or type "exit" to start over.'.center(80))
            time.sleep(4)
        else:
            print_logo()
            print(col.BLUE + f"Welcome back {user}.".center(80))
            time.sleep(2)
            break
    return user


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
        existing_pass = pwinput.pwinput(prompt=f"Passcode for {username}:\n ".center(80))
        if existing_pass == "exit":
            print(col.RED + "Login failed.".center(80))
            time.sleep(3)
            return False
        if existing_pass == curent_account[1]:
            print(col.GREEN + "Login successful.".center(80))
            time.sleep(3)
            return True
        print(col.RED + "Wrong passcode!".center(80))
        print('You can try again or type "exit" to start over.'.center(80))
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
        print(f"{error} at account creation.".center(80))
        user_account_login()
    else:
        print_logo()
        print(col.GREEN + "Account successfully created.".center(80))
        time.sleep(3)


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
            return False  # Return false if user type exit instead of username
        decision = log_in_passcode(old_user)
        #  decision may be false if user types exit when asked for the passcode
        return decision


def update_score(num):
    """
    Push the score to Google worksheet and update the score cell
    @param num(int): The new score to be pushed to worksheet
    """
    print_logo()
    print(col.YELLOW + "Updating score...".center(80))
    time.sleep(1)
    new_accounts = SHEET.worksheet('acounts')
    try:
        to_finde = new_accounts.find(new_username)
        cor1 = to_finde.row
        cor2 = to_finde.col
        old_score = new_accounts.cell(cor1, cor2 + 2).value
        if num > int(old_score):
            new_accounts.update_cell(cor1, cor2 + 2, num)
            print(col.GREEN + "Score updated successfully.".center(80))
        else:
            print("Done.".center(80))
    except NameError:
        to_finde = new_accounts.find(old_user)
        cor1 = to_finde.row
        cor2 = to_finde.col
        old_score = new_accounts.cell(cor1, cor2 + 2).value
        if num > int(old_score):
            new_accounts.update_cell(cor1, cor2 + 2, num)
            print(col.GREEN + "Score updated successfully.".center(80))
        else:
            print("Done.".center(80))
    time.sleep(2)


def height_scores():
    """
    Create a dictionary with usernames and their score from the worksheet
    and sort descending by score value
    """
    updated_acc_list = accounts.get_all_values()
    top_scores = {}
    for accnt in updated_acc_list:
        top_scores[accnt[0]] = accnt[2]
    sort_scores = sorted(top_scores.values())
    sorted_dict = {}
    for item in sort_scores[::-1]:
        for key in top_scores.keys():
            if top_scores[key] == item:
                sorted_dict[key] = top_scores[key]
    return sorted_dict
