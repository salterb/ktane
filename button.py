"""Placeholder docstring."""

from enum import Enum

from colours import bold, blue, yellow
from utils import get_input

VALID_COLOURS = ["R", "B", "Y", "W"]
VALID_WORDS = ["A", "D", "H", "P"]
HOLD_STRING = \
f"""{bold("------ HOLD, BUT DO NOT IMMEDIATELY RELEASE THE BUTTON ------")}

If the strip is {blue("BLUE")}, release the button when timer has a \
{bold("4")} in any position
If the strip is {yellow("YELLOW")}, release the button when timer has a \
{bold("5")} in any position
Otherwise release the button when timer has a {bold("1")} in any position
"""

class Colour(Enum):
    RED = "R"
    BLUE = "B"
    YELLOW = "Y"
    WHITE = "W"
    BLACK = "K"


class Word(Enum):
    ABORT = "A"
    DETONATE = "D"
    HOLD = "H"
    PRESS = "P"


def get_button_colour():
    while True:
        button_colour = get_input("Input the button colour: ")
        try:
             # Black is represented by "K", not "B", so we have a special
             # check for it
            if button_colour == "BLACK":
                colour = Colour.BLACK
            else:
                colour = Colour(button_colour[0])
            return colour
        except ValueError:
            print("Supply a valid colour")


def get_button_word():
    while True:
        button_word = get_input("Input word on button: ")
        try:
            return Word(button_word[0])
        except ValueError:
            print("Supply a valid word")


class Button:
    def __init__(self, bomb):
        self.bomb = bomb
        self.colour = get_button_colour()
        self.word = get_button_word()

    def solve(self):
        """Solves the button module on the bomb."""
        # This function is ugly. We've used 'if's and returns rather than
        # 'elif's, since we are also providing functionality for users to
        # supply the bomb data at the last possible moment, and that involves
        # provisionally going inside if statements to provide user input.

        if self.colour == Colour.BLUE and self.word == Word.ABORT:
            print(HOLD_STRING)
        elif self.word == Word.DETONATE and self.bomb.batteries > 1:
            print("\nPress and release button\n")
        elif self.colour == Colour.WHITE and self.bomb.CAR:
            print(HOLD_STRING)
        elif self.bomb.FRK and self.bomb.num_batteries > 2:
            print("\nPress and release button\n")
        elif self.colour == Colour.YELLOW:
            print(HOLD_STRING)
        elif self.colour == Colour.RED and self.word == Word.HOLD:
            print("\nPress and release button\n")
        else:
            print(HOLD_STRING)
