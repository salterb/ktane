"""Button

The Button module consists of a single button in 5 possible colours,
with 4 possible different words on it. Based on these two criteria,
the button should either be pressed, or held until a specific time.
"""

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
    """The possible colours of the button."""
    RED = "R"
    BLUE = "B"
    YELLOW = "Y"
    WHITE = "W"
    BLACK = "K"


class Word(Enum):
    """The possible words on the button."""
    ABORT = "A"
    DETONATE = "D"
    HOLD = "H"
    PRESS = "P"


def get_button_colour():
    """Get user input to get the colour of the button."""
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
    """Get user input to get the word on the button."""
    while True:
        button_word = get_input("Input word on button: ")
        try:
            return Word(button_word[0])
        except ValueError:
            print("Supply a valid word")


class Button:
    """Class to represent the button. Solving required getting the
    colour and word, and then either pressing or holding depending
    on a web of conditions prescribed by bomb attributes.
    """
    def __init__(self, bomb):
        self.bomb = bomb
        self.colour = get_button_colour()
        self.word = get_button_word()

    def solve(self):
        """Solve the button module on the bomb."""
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
