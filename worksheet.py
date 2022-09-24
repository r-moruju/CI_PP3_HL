import gspread
from google.oauth2.service_account import Credentials

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
    Get input for new or returning user
    """
    while True:
        first_question = input("Are you a returning user? (Y/N) ")
        if first_question.lower() != "y" and first_question.lower() != "n":
            print("Type 'Y' for yes or 'N' for no")
        else:
            print("Ok...")
            break
    return first_question.lower()


def ask_for_username():
    """
    Ask for username and check if is available
    """
    print("Let's create a new account for you.\n")
    keep_looping = True
    while keep_looping:
        keep_looping = False
        input_name = input("Type username: ")
        for lst in accounts_list:
            if input_name == lst[0]:
                print("This username already in use. Try a different one.")
                keep_looping = True
    print(f"Welcome {input_name}")
    return input_name


def ask_for_passcode():
    """
    Create new user pascode
    """
    passcode = input("Create your pascode: ")
    return passcode


def log_in_username():
    """
    Ask user to login by entering username and passcode
    """
    while True:
        existing_username = input("Enter your username: ")
        if existing_username == "exit":
            print("\nLogin unssuccesful")
            return False
        elif existing_username not in usernames:
            print(f"\nThere is no account with username {existing_username}")
            print("You can try again or type 'exit' to close")
        else:
            print(f"\nWelcome back {existing_username}")
            break
    return existing_username


def log_in_passcode(username):
    """
    Ask for curent user passcode and check if match
    """
    for lst in accounts_list:
        if lst[0] == username:
            curent_account = lst
    while True:
        existing_passcode = input(f"Enter passcode for username {username}: ")
        if existing_passcode == "exit":
            print("Login unssuccesful")
            break
        if existing_passcode == curent_account[1]:
            print("Login successfull")
            return True
        else:
            print("Wrong passcode!")
            print("Try again or type 'exit'")


def create_new_account(name, passcode, new_score=0):
    """
    Create a new account or update score
    """
    n_account = [name, passcode, new_score]
    print("Account created successfuly.")
    return n_account


def upload_new_acount(lst):
    """
    Update worksheet with new account
    """
    accounts.append_row(lst)


def user_account_login():
    """
    Guide user thru login or acount creation
    """
    returning_player = ask_if_returning_user()
    if returning_player == "n":
        new_username = ask_for_username()
        new_passcode = ask_for_passcode()
        new_account = create_new_account(new_username, new_passcode)
        upload_new_acount(new_account)
        return True
    if returning_player == "y":
        old_user = log_in_username()
        if old_user is False:
            return False
        decision = log_in_passcode(old_user)
        return decision
