"""Simon

The Simon module consists of four coloured buttons that flash in some
sequence
"""

from colours import blue, green, red, yellow
from utils import get_input


def _is_valid_simon(string):
    """Determine if the supplied Simon light sequence is valid."""
    return len(string) > 0 and all(char in "RBYG" for char in string)


def _contains_vowels(string):
    """Return True if the string contains any vowels, False otherwise.
    """
    return set("AEIOUaeiou").isdisjoint(set(string))


def _get_simon_input():
    """Get user input for interactive Simon."""
    while True:
        lights = get_input('Input the light sequence shown. Use one letter per colour '
                           '(type "exit" to exit): ')
        if lights == "EXIT":
            return None
        if _is_valid_simon(lights):
            return lights
        print("Invalid color sequence.")


class Simon:
    """Class to represent the Simon module. Solving requires finding the
    correct move lookup table (dependent on the number of strikes and
    whether the bomb serial contains a vowel), mapping each colour to a
    different one, and then repeating back the sequences the module
    flashes, but with the "mapped" buttons instead.

    Can either run in "static mode", which prints the lookup table, or
    "interactive mode", where the colour sequence is inputted each time
    and the corresponding buttons to be pressed are printed.
    """
    def __init__(self, bomb):
        self.bomb = bomb
        self.vowels = _contains_vowels(self.bomb.serial)

    def static_simon(self):
        """Print the relevant colour conversion list for Simon."""
        if self.vowels:
            if self.bomb.strikes == 0:
                print(f'{red("RED")}    -> {blue("BLUE")}')
                print(f'{blue("BLUE")}   -> {yellow("YELLOW")}')
                print(f'{green("GREEN")}  -> {green("GREEN")}')
                print(f'{yellow("YELLOW")} -> {red("RED")}')

            elif self.bomb.strikes == 1:
                print(f'{red("RED")}    -> {red("RED")}')
                print(f'{blue("BLUE")}   -> {blue("BLUE")}')
                print(f'{green("GREEN")}  -> {yellow("YELLOW")}')
                print(f'{yellow("YELLOW")} -> {green("GREEN")}')

            elif self.bomb.strikes >= 2:
                print(f'{red("RED")}    -> {yellow("YELLOW")}')
                print(f'{blue("BLUE")}   -> {green("GREEN")}')
                print(f'{green("GREEN")}  -> {blue("BLUE")}')
                print(f'{yellow("YELLOW")} -> {red("RED")}')
            else:
                raise ValueError(f"Invalid strike number: {self.bomb.strikes}")

        else:
            if self.bomb.strikes == 0:
                print(f'{red("RED")}    -> {blue("BLUE")}')
                print(f'{blue("BLUE")}   -> {red("RED")}')
                print(f'{green("GREEN")}  -> {yellow("YELLOW")}')
                print(f'{yellow("YELLOW")} -> {green("GREEN")}')
            elif self.bomb.strikes == 1:
                print(f'{red("RED")}     -> {yellow("YELLOW")}')
                print(f'{blue("BLUE")}    -> {green("GREEN")}')
                print(f'{green("GREEN")}   -> {blue("BLUE")}')
                print(f'{yellow("YELLOW")}  -> {red("RED")}')
            elif self.bomb.strikes == 2:
                print(f'{red("RED")}    -> {green("GREEN")}')
                print(f'{blue("BLUE")}   -> {red("RED")}')
                print(f'{green("GREEN")}  -> {yellow("YELLOW")}')
                print(f'{yellow("YELLOW")} -> {blue("BLUE")}')
            else:
                raise ValueError(f"Invalid strike number: {self.bomb.strikes}")

    def interactive_simon(self):
        """Prompts the user for the Simon input, and displays the correct
        output.
        """

        # Repeat the process until the user wants to exit
        while True:
            # Do-while for input
            lights = _get_simon_input()
            if lights is None:
                return

            if self.vowels:
                if self.bomb.strikes == 0:
                    colour_dict = {"R": "B", "B": "Y", "G": "G", "Y": "R"}
                elif self.bomb.strikes == 1:
                    colour_dict = {"R": "R", "B": "B", "G": "Y", "Y": "G"}
                elif self.bomb.strikes >= 2:
                    colour_dict = {"R": "Y", "B": "G", "G": "B", "Y": "R"}
                else:
                    raise ValueError(f"Invalid strike number: {self.bomb.strikes}")
            else:
                if self.bomb.strikes == 0:
                    colour_dict = {"R": "B", "B": "R", "G": "Y", "Y": "G"}
                elif self.bomb.strikes == 1:
                    colour_dict = {"R": "Y", "B": "G", "G": "B", "Y": "R"}
                elif self.bomb.strikes >= 2:
                    colour_dict = {"R": "G", "B": "R", "G": "Y", "Y": "B"}
                else:
                    raise ValueError(f"Invalid strike number: {self.bomb.strikes}")

            for char in lights:
                colour = colour_dict[char]
                if colour == "R":
                    print(red("RED"))
                elif colour == "B":
                    print(blue("BLUE"))
                elif colour == "G":
                    print(green("GREEN"))
                elif colour == "Y":
                    print(yellow("YELLOW"))
                else:
                    raise ValueError(f"Invalid colour: {colour}")
            print("")  # Blank line


    def solve(self):
        """Solve the Simon module."""
        while True:
            user_input = get_input("Do you want interactive Simon? (Y/n) ")
            if user_input == "" or user_input[0] == "Y":
                self.interactive_simon()
                break
            if user_input[0] == "N":
                self.static_simon()
                break
            print("Please select a valid option")
        print("")  # blank line
