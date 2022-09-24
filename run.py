# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from worksheet import accounts_list
from worksheet import usernames
from countries_api import countries_list
from countries_api import country_class

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
            return False
        elif existing_username not in usernames:
            print(f"There is no account with the username {existing_username}")
            print("You can try again or type 'exit' to close")
        else:
            print(f"Welcome back {existing_username}")
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


def print_question():
    """
    This function print the question and return True or False
    by comparing the two countries populations
    """
    top_countrie = countries_list[list_iterator]
    bottom_countrie = countries_list[list_iterator + 1]
    print(f"Does {top_countrie} have more population than {bottom_countrie}?")
    return country_class(top_countrie) > country_class(bottom_countrie)


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


#returning_player = ask_if_returning_user()
#if returning_player == "n":
    #new_username = ask_for_username()
    #new_passcode = ask_for_passcode()
    #new_account = create_new_account(new_username, new_passcode)
    #accounts.append_row(new_account)
#elif returning_player == "y":
    #old_user = log_in_username()
    #decision = log_in_passcode(old_user)

#print(decision)

main()
