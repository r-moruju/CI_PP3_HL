"""
This file contains ascii arts.
"""
from colors import Color as col
LOGO = """
     _      _         _                    __ _
    | |    (_)       | |                  / /| |
    | |__   _   __ _ | |__    ___  _ __  / / | |  ___  __      __ ___  _ __ 
    | '_ \ | | / _` || '_ \  / _ \| '__|/ /  | | / _ \ \ \ /\ / // _ \| '__|
    | | | || || (_| || | | ||  __/| |  / /   | || (_) | \ V  V /|  __/| |
    |_| |_||_| \__, ||_| |_| \___||_| /_/    |_| \___/   \_/\_/  \___||_|
                __/ |
               |___/
"""


def print_logo():
    """
    Clear terminal and print logo
    """
    print("\033c")  # Code from Stack Overflow
    print(col.YELLOW + LOGO.center(80))
