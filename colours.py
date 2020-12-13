"""Colours

Contains helper functions to add the relevant control codes to print
text in different colours in a terminal.
"""

def red(string):
    """Return a string that will appear red in a terminal."""
    return f"\033[1;91m{string}\033[0m"


def green(string):
    """Return a string that will appear green in a terminal."""
    return f"\033[1;92m{string}\033[0m"


def yellow(string):
    """Return a string that will appear yellow in a terminal."""
    return f"\033[1;93m{string}\033[0m"


def blue(string):
    """Return a string that will appear blue in a terminal."""
    return f"\033[1;94m{string}\033[0m"


def bold(string):
    """Return a string that will appear bold in a terminal."""
    return f"\033[1m{string}\033[0m"


if __name__ == "__main__":
    print("Please run the script ktane.py instead!")
