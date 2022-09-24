import random
from colors import Color as col
from countries_api import countries_list
from countries_api import country_class
from countries_api import country_population
from worksheet import user_account_login


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
        print(col.GREEN + "You answered right")
        return True
    elif answer.lower() == "n" and not question_return:
        print(col.GREEN + "You answered right")
        return True
    else:
        print(col.RED + "Wrong answer\n")
        return False


def print_result(num):
    """
    Print Score at the end of the game
    """
    print(f"You scored {num}.")
    if num < 3:
        print("Better luck next time.")
    elif num >= 3 and num < 7:
        print("This is a decent result.")
    else:
        print("Well done! Outstanding performance.")


def main():
    """
    Main function that execute a while loop as long as the user gives
    right answers
    """
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
                print("Goodby!")
                keep_playing = False
                break
            if keep_play_q.lower() == "y":
                print("Good luck!")
                keep_playing = True
                break
            if keep_play_q.lower() not in ("y", "n"):
                print("Enter 'Y' for yes or 'N' for no.")


LOGIN = user_account_login()
while not LOGIN:
    LOGIN = user_account_login()
main()
