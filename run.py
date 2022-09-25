import time
import random
from colors import Color as col
from countries_api import countries_list
from countries_api import country_class
from countries_api import country_population
from worksheet import user_account_login
from art import print_logo


def print_question():
    """
    This function prints the question
    and returns True or False comparing the population of the two countries
    """
    print_logo()
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
        print_logo()
        print(col.GREEN + "Correct answer")
        time.sleep(2)
        return True
    if answer.lower() == "n" and not question_return:
        print_logo()
        print(col.GREEN + "Correct answer")
        time.sleep(2)
        return True
    print_logo()
    print(col.RED + "Wrong answer\n")
    return False


def print_result(num):
    """
    Print Score at the end of the game
    """
    print(f"\nYou scored {num}.")
    if num < 3:
        print(col.RED + "Better luck next time.")
    elif num >= 3 and num < 7:
        print(col.YELLOW + "This is a decent result.")
    else:
        print(col.GREEN + "Well done! Outstanding performance.")


def main():
    """
    Main function that execute a while loop as long as the user gives
    right answers
    """
    print_logo()
    print(col.BLUE + "Gues witch country has more population")
    print(col.BLUE + "Just answer with 'Y' for yes or 'N' for no")
    time.sleep(5)
    keep_playing = True
    while keep_playing:

        random.shuffle(countries_list)
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

        top_countrie = countries_list[list_iterator]
        bottom_countrie = countries_list[list_iterator + 1]
        if not game_on:
            country_population(top_countrie)
            print("while")
            country_population(bottom_countrie)

        print_result(score)

        while True:
            keep_play_q = input("Do you want to play again? (Y/N): ")
            if keep_play_q.lower() == "n":
                print("Goodbye!")
                keep_playing = False
                break
            if keep_play_q.lower() == "y":
                print("Good luck!")
                keep_playing = True
                break
            if keep_play_q.lower() not in ("y", "n"):
                print_logo()
                print("Enter 'Y' for yes or 'N' for no.")
                time.sleep(3)


print_logo()
LOGIN = user_account_login()
while not LOGIN:
    LOGIN = user_account_login()
main()
