"""
Creates a color Class with color properties,
witch are easier to call when needed
"""
from colorama import init

# Initializes Colorama
init(autoreset=True)


class Color:
    """
    Color class to print different color text on terminal
    """
    YELLOW = "\033[1;33;48m"
    RED = "\033[1;31;48m"
    GREEN = "\033[1;32;48m"
    BLUE = "\033[1;34;48m"
