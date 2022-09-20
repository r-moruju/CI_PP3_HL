# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

countries = {
    "England": 60,
    "Poland": 40,
    "France": 45,
    "Spain": 44,
    "Ucraine": 39,
}

countries_list = [key for key in countries.keys()]

random.shuffle(countries_list)


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


main()
