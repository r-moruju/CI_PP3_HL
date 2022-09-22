# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
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

acounts = SHEET.worksheet('acounts')
acounts_list = acounts.get_all_values()

countries = {
    "England": 60,
    "Poland": 40,
    "France": 45,
    "Spain": 44,
    "Ucraine": 39,
}

countries_list = [key for key in countries.keys()]

random.shuffle(countries_list)


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
        for lst in acounts_list:
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


def log_in():
    """
    Ask user to login by entering username and passcode
    """
    


def create_new_account(name, passcode, new_score=0):
    """
    Create a new account or update score
    """
    n_account = [name, passcode, new_score]
    print("Account created successfuly.")
    return n_account


def print_question():
    """
    This function print the question and return True or False
    by comparing the two countries populations
    """
    top_countrie = countries_list[list_iterator]
    bottom_countrie = countries_list[list_iterator + 1]
    print(f"Dos {top_countrie} have more population than {bottom_countrie}?")
    return countries[top_countrie] > countries[bottom_countrie]


def get_answer():
    """
    Get user input and and by comparing with question output
    return True or False
    """
    global score
    score = 0
    answer = input("Your answer is (Y/N): ")
    if answer.lower() == "y" and question_return:
        print("You answered right")
        score += 1
        return True
    elif answer.lower() == "n" and not question_return:
        print("You answered right")
        score += 1
        return True
    else:
        print("Wrong answer\n")
        print(f"You scored {score}")
        return False
        

def main():
    """
    Main function that execute a wihle loop as long as the user gives
    right answers
    """
    global question_return
    global list_iterator
    list_iterator = 0
    question_return = print_question()
    game_on = get_answer()

    while game_on:
        list_iterator += 1
        question_return = print_question()
        game_on = get_answer()


returning_player = ask_if_returning_user()
if returning_player == "n":
    new_username = ask_for_username()
    new_passcode = ask_for_passcode()
    new_account = create_new_account(new_username, new_passcode)
    acounts.append_row(new_account)

print(new_account)
# main()
