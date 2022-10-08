import time
import random
from colors import Color as col
from countries_api import countries_list
from countries_api import country_class
from countries_api import country_population
from worksheet import user_account_login
from worksheet import update_score
from worksheet import height_scores
from art import print_logo


def print_question() -> bool:
    """
    This function prints the question
    and returns True or False comparing the population of the two countries
    """
    print_logo()
    country1 = countries_list[list_iterator]
    country2 = countries_list[list_iterator + 1]
    print(f"Does {country1} have more population than {country2}?".center(80))
    return country_class(country1) > country_class(country2)


def get_answer() -> bool:
    """
    Get user input and and by comparing with question output
    return True or False
    """
    while True:
        answer = input("Your answer is (Y/N):\n ".center(80))
        if answer.lower() not in ("y", "n"):
            print(col.RED + "Wrong input!".center(80))
            print(col.YELLOW + "Enter 'Y' for yes or 'N' for no.".center(80))
            time.sleep(2)
        if answer.lower() == "y" and question_return:
            print_logo()
            print(col.GREEN + "Correct answer!".center(80))
            time.sleep(2)
            return True
        if answer.lower() == "n" and not question_return:
            print_logo()
            print(col.GREEN + "Correct answer!".center(80))
            time.sleep(2)
            return True
        if answer.lower() == "y" and not question_return:
            print_logo()
            print(col.RED + "Wrong answer!\n".center(80))
            return False
        if answer.lower() == "n" and question_return:
            print_logo()
            print(col.RED + "Wrong answer!\n".center(80))
            return False


def print_result(num: int):
    """
    Print Score at the end of the game
    @param num(int): A number which represent the score
    """
    print("\n")
    print(f"You scored {num}.".center(80))
    if num < 3:
        print(col.RED + "Better luck next time.".center(80))
    elif num >= 3 and num < 7:
        print(col.YELLOW + "This is a decent result.".center(80))
    else:
        print(col.GREEN + "Well done! Outstanding performance.".center(80))


def replay() -> bool:
    """
    Ask user to play again and return True or False
    """
    while True:
        keep_play_q = input("Do you want to play again? (Y/N):\n ".center(80))
        if keep_play_q.lower() == "n":
            return False
        if keep_play_q.lower() == "y":
            return True
        if keep_play_q.lower() not in ("y", "n"):
            print_logo()
            print(col.YELLOW + "Enter 'Y' for yes or 'N' for no.".center(80))
            time.sleep(3)


def main():
    """
    Main function that execute a while loop as long as the user gives
    right answers
    """
    print_logo()
    print(col.BLUE + "Gues witch country has more population.".center(80))
    print(col.BLUE + "Just answer with 'Y' for yes or 'N' for no.".center(80))
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
            print("while".center(80))
            country_population(bottom_countrie)

        print_result(score)
        keep_playing = replay()
        update_score(score)
        top_five()
        log_out()


def initializator():
    """
    The first called function
    """
    print_logo()
    LOGIN = user_account_login()
    while not LOGIN:
        LOGIN = user_account_login()
    main()


def top_five():
    """
    Print top five heighscores
    """
    sorted_dict = height_scores()
    print_logo()
    print(col.YELLOW + "Heighscores:".center(80))
    breaker = 0
    for k, v in sorted_dict.items():
        breaker += 1
        if breaker == 1:
            continue
        print(f"{k}: {v}".center(80))
        if breaker == 6:
            break


def log_out():
    """
    Print Logging out message
    """
    time.sleep(2)
    print("\n" + 33*" " + "Logging out", end="")
    for num in range(4):
        time.sleep(2)
        print(".", end="")
    initializator()


initializator()
