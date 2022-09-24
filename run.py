# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from countries_api import countries_list
from countries_api import country_class
from worksheet import user_account_login

random.shuffle(countries_list)


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
    answer = input("Your answer is (Y/N): ")
    if answer.lower() == "y" and question_return:
        print("You answered right")
        return True
    elif answer.lower() == "n" and not question_return:
        print("You answered right")
        return True
    else:
        print("Wrong answer\n")
        return False


def main():
    """
    Main function that execute a while loop as long as the user gives
    right answers
    """
    global question_return
    global list_iterator
    global score
    score = 0
    list_iterator = 0
    question_return = print_question()
    game_on = get_answer()

    while game_on:
        score += 1
        list_iterator += 1
        question_return = print_question()
        game_on = get_answer()

    print(f"You scored {score}")


LOGIN = user_account_login()
if LOGIN:
    main()
