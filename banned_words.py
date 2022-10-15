import time
from colors import Color as col

f = open("british-swear-words-list.txt", "r")
f_string = f.read()
banned_list = f_string.split(",")
f.close()


def validate_username(username: str) -> bool:
    if username.lower() in banned_list:
        print(col.RED + "This is a banned username. Try again.".center(80))
        time.sleep(3)
        return False

    return True
