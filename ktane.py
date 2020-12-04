#!/usr/bin/env python3

"""
KTANE Solver

A friendly interactive manual, written in Python3, to help solve
modules and defuse bombs in Keep Talking and Nobody Explodes.

"""
from collections import namedtuple
from sys import version_info, exit

import complicated_wires
import simple_wires
import wof
from mazes import solve_maze
from colours import *
from utils import get_input

if version_info < (3, 6):
    print("Python 3.6 or greater is required")
    exit(1)

LOGO = r"""
 _   _______ ___   _   _  _____
| | / /_   _/ _ \ | \ | ||  ___|
| |/ /  | |/ /_\ \|  \| || |__
|    \  | ||  _  || . ` ||  __|
| |\  \ | || | | || |\  || |___
\_| \_/ \_/\_| |_/\_| \_/\____/


 _____       _
/  ___|     | |
\ `--.  ___ | |_   _____ _ __
 `--. \/ _ \| \ \ / / _ \ '__|
/\__/ / (_) | |\ V /  __/ |
\____/ \___/|_| \_/ \___|_|
"""


class Bomb:
    """Bomb object.

    Holds configuration information for the bomb.
    """
    def __init__(self,
                 serial=None,
                 num_batteries=None,
                 parallel_port=None,
                 CAR=None,
                 FRK=None):
        self.serial = serial              # The bomb's serial number
        self.num_batteries = num_batteries  # The number of batteries on the bomb
        self.parallel_port = parallel_port  # Is there a parallel port?
        self.CAR = CAR                    # Is there a _lit_ CAR indicator?
        self.FRK = FRK                    # Is there a _lit_ FRK indicator?
        self.strikes = 0

    def __repr__(self):
        rep  = f"Bomb: serial: {self.serial}"
        rep += f"      num_batteries: {self.num_batteries}"
        rep += f"      parallel_port: {self.parallel_port}"
        rep += f"      CAR: {self.CAR}"
        rep += f"      FRK: {self.FRK}"
        return rep

    def add_serial(self):
        # do-while to get input
        while True:
            serial = get_input("Input the bomb's serial number: ")
            if (serial.isalnum() and
                len(serial) == 6 and
                (serial[-1]).isdigit()):
                    self.serial = serial
                    break
            print("Invalid serial number")

    def add_batteries(self):
        while True:
            try:
                self.num_batteries = int(input("Input the number of batteries "
                                               "on the bomb: "))
                break
            except ValueError:
                print("Invalid number of batteries")

    def add_parallel_port(self):
        while True:
            parallel_port = input("Does the bomb have a parallel port? (Y/N) ").upper()
            if len(parallel_port) > 0 and parallel_port[0] == 'Y':
                self.parallel_port = True
                break
            elif len(parallel_port) > 0 and parallel_port[0] == 'N':
                self.parallel_port = False
                break
            print("Invalid input")

    def _add_indicator(self, name):
        while True:
            symbol = input(f'Is there a lit indicator with label "{name}"? (Y/N) ').upper()
            if len(symbol) > 0 and symbol[0] == "Y":
                setattr(self, symbol, True)
                break
            elif len(symbol) > 0 and symbol[0] == "N":
                setattr(self, symbol, False)
                break
            print("Invalid input")

    def add_CAR():
        self._add_indicator("CAR")

    def add_FRK():
        self._add_indicator("FRK")


# ---------------------------------------------------------- #
#                                                            #
#                       BOMB CONFIG                          #
#                                                            #
# ---------------------------------------------------------- #

def setup_bomb():
    """Sets up the bomb with a bunch of user input."""
    serial = add_serial()
    num_batteries = add_batteries()
    parallel_port = add_parallel_port()
    CAR = add_CAR()
    FRK = add_FRK()
    bomb = Bomb(serial, num_batteries, parallel_port, CAR, FRK)
    return bomb


def config_bomb(bomb):
    """Allows later configuration of the bomb in the event of
    incorrect initial input."""
    bomb.serial = add_serial()
    bomb.num_batteries = add_batteries()
    bomb.parallel_port = add_parallel_port()
    bomb.CAR = add_CAR()
    bomb.FRK = add_FRK()


def strike(bomb):
    """Adds a strike to the bomb."""
    bomb.strikes += 1

def num_strikes(bomb):
    """Prints the number of strikes currently on the bomb."""
    print(f"The bomb has {bomb.strikes} strikes")

def reset_strikes(bomb):
    """Resets strikes in case of incorrect strike input."""
    bomb.strikes = 0


# ---------------------------------------------------------- #
#                                                            #
#                         HELPERS                            #
#                                                            #
# ---------------------------------------------------------- #


def is_valid_simon(string):
    """Helper function to determine if the Simon light sequence is
    valid.
    """
    if len(string) == 0:
        return False
    for char in string:
        if char not in ('R', 'B', 'Y', 'G'):
            return False
    return True


# Symbols functions
def _rot13(string):
    """Enable rot-13 encoding of words so my code doesn't have smutty
    words in it.
    """
    from codecs import encode
    return encode(string, "rot_13")


def symbol_parser():
    """Takes a string, and attempts to parse it to match to one of many
    symbols. The idea is that there are no two columns with similar
    symbols, so several, such as "black star" and "white star" can be
    mapped to "star". Even so, it's gonna be ugly.
    """

    # If you're reading this, this project probably became too big, and
    # you need a better parsing function. You're not gonna be able to
    # bootstrap anything onto this to make it work, you'll need to do
    # something cleverer. Sorry.

    # Do-while for input
    while True:
        string = get_input("Input your symbol (either a close letter "
                           "or very short description): ").replace('-', '')
        # The list of valid symbols to return is as follows:
        # Q, AT, LAMBDA, N, CAT, H, C, EURO, PHI, STAR, QUESTION,
        # OMEGA, K, 3, 6, PARAGRAPH, TB, FACE, PSI, NOTEQUAL, AE
        # Note that some symbols overlap, but this isn't a problem as they
        # are all in separate columns
        if string in ("Q", "QOPPA", "KOPPA", "WEIRDQ", "LOLLY", "LOLLIPOP",
                      "LOLLYPOP", "POPSICLE"):
            symbol = "Q"
        elif string in ("AT", "TA", "WEIRDA", "A", "PYRAMID", "LADDER"):
            symbol = "AT"
        elif string in ("LAMBDA", "LAMBDALINE", "WEIRDLAMBDA", "LAMBDAWITHLINE"):
            symbol = "LAMBDA"
        elif string in ("N", "WEIRDN", "BACKWARDSN", "LIGHTNING", "BOLT", "LIGHTNINGBOLT",
                        "THUNDER", "THUNDERBOLT", "NWITHHAT", "NHAT", "NSQUIGGLE", "NBREVE"):
            symbol = "N"
        elif string in ("CAT", "KITTY", "JELLYFISH", "WHAT", "WHAT?", "HWITHTRIANGLE",
                        "HTRIANGLE"):
            symbol = "CAT"
        elif string in ("H", "CURLY H", "CURSIVEH", "GOTHICH", "HWITHTAIL", "HTAIL", "WEIRDH"):
            symbol = "H"
        elif string in ("C", "CWITHDOT", "CDOT", "BACKWARDC", "BACKWARDCDOT", "COPYRIGHT",
                        "CINCIRCLE"):
            symbol = "C"
        elif string in ("EURO", "EUROUMLAUT", "EURODOTS", "E", "EDOTS", "BACKWARDSEURO"):
            symbol = "EURO"
        elif string in ("PHI", "SPRING", "COIL", "CURL", "CURLYQ"):
            symbol = "PHI"
        elif string in ("STAR", "WHITESTAR", "BLACKSTAR", "FILLEDINSTAR"):
            symbol = "STAR"
        elif string in ("QUESTION", "QUESTIONMARK", "UPSIDEDOWNQUESTIONMARK",
                        "UPSIDEDOWNQUESTION", "?"):
            symbol = "QUESTION"

        # ROT-13 encoding here because SOME PEOPLE claim that this
        # symbol resembles various bodily parts, the names of which I
        # don't want in my code. IT'S AN OMEGA, EVERYONE!
        elif string in ("OMEGA", "W", "WEIRDW", _rot13("NFF"), _rot13("OHZ"),
                        _rot13("OHGG"), _rot13("OBBGL"), _rot13("OBBOF"),
                        _rot13("OBBOVRF"), _rot13("GVGF"), _rot13("GVGGVRF"),
                        _rot13("ONYYF"), _rot13("GRFGRF"), _rot13("FPEBGHZ"),
                        _rot13("AHGFNPX"), _rot13("AHGF"), "HEADPHONES"):
            symbol = "OMEGA"
        elif string in ("K", "Ж", "ZHE", "KS", "2K", "2KS", "TWOK", "TWOKS", "WEIRDX",
                        "WEIRDK", "Z", "BACKTOBACKK", "BACKTOBACKKS"):
            symbol = "K"
        elif string in ("3", "WEIRD3", "HALF3", "UNFINISHED3", "THREE", "3WITHTAIL",
                        "3WITHHORNS"):
            symbol = "3"
        elif string in ("6", "SIX", "FLAT6", "FLATSIX", "WEIRD6", "WEIRDSIX", "DELTA",
                        "WEIRDDELTA"):
            symbol = "6"
        elif string in ("PARAGRAPH", "P", "WEIRDP", "BOLDP"):
            symbol = "PARAGRAPH"
        elif string in ("TB", "BT", "DT", "TD", "WEIRDB"):
            symbol = "TB"
        elif string in ("FACE", "SMILE", "SMILEY", "SMILEYFACE", "HAPPY",
                        "HAPPYFACE"):
            symbol = "FACE"
        elif string in ("PSI", "TRIDENT", "FORK", "PITCHFORK"):
            symbol = "PSI"
        elif string in ("NOTEQUAL", "NOTEQUALS", "NOTEQUALSIGN", "HASH", "HASHTAG", "POUND",
                        "POUNDSIGN", "WEIGHT", "WEIGHTS", "DUMBBELL", "WEIRDX", "CROSS"):
            symbol = "NOTEQUAL"
        elif string in ("AE", "Æ", "ASH"):
            symbol = "AE"

        return symbol


# Simon functions
def static_simon(bomb):
    """Simply prints out the relevant colour conversion list for
    Simon.
    """
    if set(['A', 'E', 'I', 'O', 'U']).isdisjoint(set(bomb.serial)):
        if bomb.strikes == 0:
            print(red("RED")+"    -> "+blue("BLUE"))
            print(blue("BLUE")+"   -> "+yellow("YELLOW"))
            print(green("GREEN")+"  -> "+green("GREEN"))
            print(yellow("YELLOW")+" -> "+red("RED"))

        elif bomb.strikes == 1:
            print(red("RED")+"    -> "+red("RED"))
            print(blue("BLUE")+"   -> "+blue("BLUE"))
            print(green("GREEN")+"  -> "+yellow("YELLOW"))
            print(yellow("YELLOW")+" -> "+green("GREEN"))

        elif bomb.strikes == 2:
            print(red("RED")+"    -> "+yellow("YELLOW"))
            print(blue("BLUE")+"   -> "+green("GREEN"))
            print(green("GREEN")+"  -> "+blue("BLUE"))
            print(yellow("YELLOW")+" -> "+red("RED"))
        else:
            raise ValueError(f"Invalid strike number: {bomb.strikes}")

    else:
        if bomb.strikes == 0:
            print(red("RED")+"    -> "+blue("BLUE"))
            print(blue("BLUE")+"   -> "+red("RED"))
            print(green("GREEN")+"  -> "+yellow("YELLOW"))
            print(yellow("YELLOW")+" -> "+green("GREEN"))
        elif bomb.strikes == 1:
            print(red("RED")+"     -> "+yellow("YELLOW"))
            print(blue("BLUE")+"    -> "+green("GREEN"))
            print(green("GREEN")+"   -> "+blue("BLUE"))
            print(yellow("YELLOW")+"  -> "+red("RED"))
        elif bomb.strikes == 2:
            print(red("RED")+"    -> "+green("GREEN"))
            print(blue("BLUE")+"   -> "+red("RED"))
            print(green("GREEN")+"  -> "+yellow("YELLOW"))
            print(yellow("YELLOW")+" -> "+blue("BLUE"))
        else:
            raise ValueError(f"Invalid strike number: {bomb.strikes}")


def interactive_simon(bomb):
    """Prompts the user for the Simon input, and displays the correct
    output.
    """

    # Repeat the process until the user wants to exit
    while True:
        # Do-while for input
        while True:
            lights = get_input('Input the light sequence shown (type "exit" to exit): ')
            if lights == "EXIT":
                return
            if is_valid_simon(lights):
                print("")  # Blank line
                break
            print("Invalid color sequence. Use one letter per colour")

        if set(['A', 'E', 'I', 'O', 'U']).isdisjoint(set(bomb.serial)):
            if bomb.strikes == 0:
                colour_dict = {'R': 'B', 'B': 'Y', 'G': 'G', 'Y': 'R'}
            elif bomb.strikes == 1:
                colour_dict = {'R': 'R', 'B': 'B', 'G': 'Y', 'Y': 'G'}
            elif bomb.strikes == 2:
                colour_dict = {'R': 'Y', 'B': 'G', 'G': 'B', 'Y': 'R'}
            else:
                raise ValueError(f"Invalid strike number: {bomb.strikes}")
        else:
            if bomb.strikes == 0:
                colour_dict = {'R': 'B', 'B': 'R', 'G': 'Y', 'Y': 'G'}
            elif bomb.strikes == 1:
                colour_dict = {'R': 'Y', 'B': 'G', 'G': 'B', 'Y': 'R'}
            elif bomb.strikes == 2:
                colour_dict = {'R': 'G', 'B': 'R', 'G': 'Y', 'Y': 'B'}
            else:
                raise ValueError(f"Invalid strike number: {bomb.strikes}")

        for char in lights:
            colour = colour_dict[char]
            if colour == 'R':
                print(red("RED"))
            elif colour == 'B':
                print(blue("BLUE"))
            elif colour == 'G':
                print(green("GREEN"))
            elif colour == 'Y':
                print(yellow("YELLOW"))
            else:
                raise ValueError(f"Invalid colour: {colour}")
        print("")  # Blank line


# Memory functions
def _memory_input(arg):
    """Gets input for the Memory module. Either asks for number on
    display, which value was in the button pressed, or which position
    the pressed button was in, depending on the argument provided.
    """
    DISPLAY = 0
    WHICH_LABEL = 1
    WHICH_POSITION = 2
    if arg not in (DISPLAY, WHICH_LABEL, WHICH_POSITION):
        raise ValueError(f"Invalid argument passed to memoryDisplayInput: {arg}")

    # Do-while for input
    while True:
        if arg == DISPLAY:
            ipt = get_input("Input the number on the display: ")
        elif arg == WHICH_LABEL:
            ipt = get_input("What value was in that position? ")
        else:
            ipt = get_input("Which position was that in? ")

        if ipt.isdigit() and 1 <= int(ipt) <= 4:
            return int(ipt)
        print("Invalid input")


def is_valid_wire_sequence(wire):
    """Verifies the provided wire sequence consists of valid
    characters.
    """
    if len(wire) >= 2 and wire[0] in ('R', 'B', 'K') and wire[-1] in ('A', 'B', 'C'):
        return True
    return False


# ---------------------------------------------------------- #
#                                                            #
#                         MODULES                            #
#                                                            #
# ---------------------------------------------------------- #


def button(bomb):
    """Solves the button module on the bomb.
    This function is ugly. We've used 'if's and returns rather than
    'elif's, since we are also providing functionality for users to
    supply the bomb data at the last possible moment, and that involves
    provisionally going inside if statements to provide user input.
    """

    # Two do-while loops to get the button color and word
    valid_colours = ["R", "B", "Y", "W"]
    while True:
        button_colour = get_input("Input the button colour: ")
        if button_colour in valid_colours:
            break
        print("Please supply a valid colour from [R, B, Y, W]")

    button_word = ""
    valid_words = ["A", "D", "H", "P"]
    while button_word not in valid_words:
        button_word = get_input("Input first letter of word on button: ")
        if button_word not in valid_words:
            print("Please supply a valid letter from [A, D, H, P]")

    release_string = (bold("------ DO NOT IMMEDIATELY RELEASE THE "
                           "BUTTON ------\n\n") +
                      "If the strip is " + blue("BLUE") + ", release the "
                      "button when timer has a " + bold("4") + " in any "
                      "position\nIf the strip is " + yellow("YELLOW") + ", "
                      "release the button when timer has a " + bold("5") + "in "
                      "any position\nOtherwise release the button when timer "
                      "has a " + bold("1") + " in any position\n")

    if button_colour == "B" and button_word == "A":
        print("\nHold button\n")
        print(release_string)
        return

    if (button_word == "D" and (bomb.num_batteries is None or bomb.num_batteries > 1)):
        if bomb.num_batteries is None:
            bomb.num_batteries = add_batteries()

        if bomb.num_batteries > 1:
            print("\nPress and release button\n")
            return

    if button_colour == "W" and bomb.CAR is not False:
        if bomb.CAR is None:
            bomb.CAR = add_CAR()

        if bomb.CAR is True:
            print("\nHold button\n")
            print(release_string)
            return

    if (bomb.FRK is not False and (bomb.num_batteries is None or bomb.num_batteries > 2)):
        if bomb.num_batteries is None:
            bomb.num_batteries = add_batteries()
        if bomb.FRK is None:
            bomb.FRK = add_FRK()

        if bomb.FRK is True:
            print("\nPress and release button\n")
            return

    if button_colour == "Y":
        print("Hold button")
        print(release_string)
        return

    if button_colour == "R" and button_word == "H":
        print("\nPress and release button\n")
        return

    else:
        print("Hold button")
        print(release_string)
        return


def keypad():
    """Solves the symbol keypad."""
    from copy import deepcopy as dc
    columns = [["Q", "AT", "LAMBDA", "N", "CAT", "H", "C"],
               ["EURO", "Q", "C", "PHI", "STAR", "H", "QUESTION"],
               ["C", "OMEGA", "PHI", "K", "3", "LAMBDA", "STAR"],
               ["6", "PARAGRAPH", "TB", "CAT", "K", "QUESTION", "FACE"],
               ["PHI", "FACE", "TB", "C", "PARAGRAPH", "3", "STAR"],
               ["6", "EURO", "NOTEQUAL", "AE", "PSI", "N", "OMEGA"]]
    symbols = []
    print("\n"+"-"*20+" CAUTION "+"-"*20)
    print("This module is hard for a computer to solve.\nPlease try to "
          "describe all symbols using a very short and obvious description.\n"
          + "-"*49, end='\n\n')
    while len(symbols) < 4:
        string = symbol_parser()
        if string in symbols:
            print("Symbol already added")
        elif string is None:
            print("Symbol not recognised")
        else:
            symbols.append(string)

    # Make a copy of the columns for iterating over
    columns_copy = dc(columns)
    for col in columns_copy:
        for item in symbols:
            if item not in col:
                columns.remove(list)
                break

    # Now we have the correct column (or none at all), so we just print out
    # our symbols in order
    if len(columns) == 1:
        correct_column = columns[0]
        for item in correct_column:
            if item in symbols:
                print(bold(item.capitalize()))
    elif len(columns) > 1:
        raise ValueError(f"Multiple valid columns: {columns}")
    else:
        print("No valid columns. Did you input the symbols correctly?")


def simon(bomb):
    """Solves the "Simon" module, in one of two ways. Either prints out
    the colour map, or enters "interactive mode", where the user inputs
    a color string and we print out the correct sequence of colors to
    press.
    """
    # Check strike validity
    if bomb.strikes not in (0, 1, 2):
        print((f"You have {bomb.strikes} strikes. Please run \"reset strikes\" to try again"))
        return

    if bomb.serial is None:
        bomb.serial = add_serial()
    while True:
        user_input = get_input("Do you want interactive Simon? (Y/n) ")
        if user_input == "" or user_input[0] == "Y":
            interactive_simon(bomb)
            print("")  # Blank line
            break
        elif user_input[0] == "N":
            static_simon(bomb)
            print("")  # Blank line
            break
        else:
            print("Please select a valid option")


def whos_on_first():
    """Solves the "Who's on first" module, by outputting the list of
    potential solutions in order.
    """

    # We keep going until the user wants to stop
    while True:
        # Do-while to get the word on the display
        while True:
            display = get_input('\nWhat word is on the display? (type "exit" to cancel): ')
            if display == "EXIT":
                print("Exiting\n")
                return
            if display in wof.VALID_DISPLAYS:
                break
            print("Please input a valid display entry")

        # Do-while to get the word on the button
        while True:
            button = get_input(f"What word is on the {wof.DISPLAY_DICT[display]} button? ")
            if button == "EXIT":
                print("Exiting\n")
                return
            if button in wof.VALID_BUTTONS:
                break
            print("Please input a valid button entry")

        print("\nThe button to press is the first valid entry in the following list: ")
        print(wof.BUTTON_DICT[button])


def memory():
    """Solves the memory module by storing all previous input and
    automatically referring back to it to find the correct answers.
    """
    DISPLAY = 0
    WHICH_LABEL = 1
    WHICH_POSITION = 2

    stage = namedtuple('stage', ["label", "position"])
    # Stage 1
    ipt = _memory_input(DISPLAY)
    print("")  # Blank line
    if ipt in (1, 2):
        print("Press the button in " + bold("POSITION 2\n"))
        stage1 = stage(_memory_input(WHICH_LABEL), 2)
    elif ipt == 3:
        print("Press the button in " + bold("POSITION 3\n"))
        stage1 = stage(_memory_input(WHICH_LABEL), 3)
    elif ipt == 4:
        print("Press the button in " + bold("POSITION 4\n"))
        stage1 = stage(_memory_input(WHICH_LABEL), 4)
    else:
        raise ValueError(f"Invalid option passed to memory stage 1: {ipt}")

    # Stage 2
    ipt = _memory_input(DISPLAY)
    print("")  # Blank line
    if ipt == 1:
        print("Press the button with " + bold("LABEL 4\n"))
        stage2 = stage(4, _memory_input(WHICH_POSITION))
    elif ipt in (2, 4):
        print("Press the button in " + bold(f"POSITION {stage1.position}\n"))
        stage2 = stage(_memory_input(WHICH_LABEL), stage1.position)
    elif ipt == 3:
        print("Press the button in " + bold("POSITION 1\n"))
        stage2 = stage(_memory_input(WHICH_LABEL), 1)
    else:
        raise ValueError(f"Invalid option passed to memory stage 2: {ipt}")

    # Stage 3
    ipt = _memory_input(DISPLAY)
    print("")  # Blank line
    if ipt == 1:
        print("Press the button with " + bold(f"LABEL {stage2.label}\n"))
        stage3 = stage(stage2.label, _memory_input(WHICH_POSITION))
    elif ipt == 2:
        print(f"Press the button with " + bold(f"LABEL {stage1.label}\n"))
        stage3 = stage(stage1.label, _memory_input(WHICH_POSITION))
    elif ipt == 3:
        print("Press the button in " + bold("POSITION 3\n"))
        stage3 = stage(_memory_input(WHICH_LABEL), 3)
    elif ipt == 4:
        print("Press the button with " + bold("LABEL 4\n"))
        stage3 = stage(4, _memory_input(WHICH_POSITION))
    else:
        raise ValueError(f"Invalid option passed to memory stage 3: {ipt}")

    # Stage 4
    ipt = _memory_input(DISPLAY)
    print("")  # Blank line
    if ipt == 1:
        print("Press the button in " + bold(f"POSITION {stage1.label}\n"))
        stage4 = stage(stage1.label, _memory_input(WHICH_POSITION))
    elif ipt == 2:
        print("Press the button in " + bold("POSITION 1\n"))
        stage4 = stage(_memory_input(WHICH_LABEL), 1)
    elif ipt in (3, 4):
        print("Press the button in " + bold(f"POSITION {stage2.position}\n"))
        stage4 = stage(_memory_input(WHICH_LABEL), stage2.position)
    else:
        raise ValueError(f"Invalid option passed to memory stage 4: {ipt}")

    # Stage 5
    ipt = _memory_input(DISPLAY)
    print("")  # Blank line
    if ipt == 1:
        print("Press the button with " + bold(f"LABEL {stage1.label}\n"))
    elif ipt == 2:
        print("Press the button with " + bold(f"LABEL {stage2.label}\n"))
    elif ipt == 3:
        print("Press the button with " + bold(f"LABEL {stage4.label}\n"))
    elif ipt == 4:
        print("Press the button with " + bold(f"LABEL {stage3.label}\n"))
    else:
        raise ValueError(f"Invalid option passed to memory stage 5: {ipt}")


def morse():
    """Solves the morse module. The user inputs morse characters until
    there is only one valid word left.
    """
    valid_words = ["SHELL", "HALLS", "SLICK", "TRICK", "BOXES", "LEAKS",
                   "STROBE", "BISTRO", "FLICK", "BOMBS", "BREAK", "BRICK",
                   "STEAK", "STING", "VECTOR", "BEATS"]
    freqs = [3.505, 3.515, 3.522, 3.532, 3.535, 3.542, 3.545, 3.552, 3.555,
             3.565, 3.572, 3.575, 3.582, 3.592, 3.595, 3.600]
    morse_freqs = dict(zip(valid_words, freqs))
    morse_letters = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
                     ".": "E", "..-.": "F", "--.": "G", "....": "H",
                     "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
                     "--": "M", "-.": "N", "---": "O", ".--.": "P",
                     "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
                     "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
                     "-.--": "Y", "--..": "Z"}

    while len(valid_words) > 1:
        while True:
            morse_sequence = get_input("Input a morse code letter (. = dot, - = dash): ")
            if morse_sequence in ("EXIT", "QUIT"):
                return

            # Test whether the input has valid morse characters
            valid_morse = True
            for char in morse_sequence:
                if char not in ['.', '-']:
                    valid_morse = False
            if len(morse_sequence) == 0 or len(morse_sequence) > 4:
                valid_morse = False
            if valid_morse:
                break
            print("Invalid morse sequence. Please try again")

        valid_words_copy = valid_words[:]
        for word in valid_words_copy:
            if morse_letters[morse_sequence] not in word:
                valid_words.remove(word)

    # Now we have at most one valid word
    if len(valid_words) == 0:
        print("Morse inputs do not match any known word. Please run module again.")
    else:
        print(f"\nThe word is {valid_words[0]}")
        freq_str = f"{morse_freqs[valid_words[0]]:.3f}"  # Pad with zeroes
        print("The frequency is " + bold(freq_str) + " MHz\n")


def sequences():
    """Loads an interface that can solve the wire sequences module.
    Also implements a "delete" function in case of accidental input.
    """
    RED = -1
    BLUE = -2
    BLACK = -3
    valid_reds = {0: 'C', 1: 'B', 2: 'A', 3: 'AC', 4: 'B',
                  5: 'AC', 6: 'ABC', 7: 'AB', 8: 'B'}
    valid_blues = {0: 'B', 1: 'AC', 2: 'B', 3: 'A', 4: 'B',
                   5: 'BC', 6: 'C', 7: 'AC', 8: 'A'}
    valid_blacks = {0: 'ABC', 1: 'AC', 2: 'B', 3: 'AC', 4: 'B',
                    5: 'BC', 6: 'AB', 7: 'C', 8: 'C'}
    red_count = 0
    blue_count = 0
    black_count = 0
    previous_move = None
    # Keep going until the user wants to exit
    while True:
        # Do-while for input
        while True:
            wire = get_input("\nInput the colour of the wire, and the letter to which "
                             "it is connected. Use 'K' for black.\n"
                             "(Type 'exit' to exit, 'undo' to undo previous move.) ")
            if wire == "EXIT":
                print("\nExiting\n")
                return
            if wire == "UNDO":
                if previous_move is None:
                    print("Nothing to undo!")
                elif previous_move == RED:
                    red_count -= 1
                elif previous_move == BLUE:
                    blue_count -= 1
                elif previous_move == BLACK:
                    black_count -= 1
                previous_move = None
                break

            if is_valid_wire_sequence(wire):
                break
            print("Invalid wire")

        # Now our wire is valid, we provide output.
        if wire[0] == 'R':
            if wire[1] in valid_reds[red_count]:
                cut()
            else:
                no_cut()
            red_count += 1
            previous_move = RED
        elif wire[0] == 'B':
            if wire[1] in valid_blues[blue_count]:
                cut()
            else:
                no_cut()
            blue_count += 1
            previous_move = BLUE
        elif wire[0] == 'K':
            if wire[1] in valid_blacks[black_count]:
                cut()
            else:
                no_cut()
            black_count += 1
            previous_move = BLACK

        if red_count > 8 or blue_count > 8 or black_count > 8:
            print("Used too many wires. Exiting\n")
            return


def maze():
    """Calls the external maze solver from a separate module."""
    solve_maze()


def password():
    """Solves the password module."""
    valid_passwords = ["ABOUT", "AFTER", "AGAIN", "BELOW", "COULD",
                       "EVERY", "FIRST", "FOUND", "GREAT", "HOUSE",
                       "LARGE", "LEARN", "NEVER", "OTHER", "PLACE",
                       "PLANT", "POINT", "RIGHT", "SMALL", "SOUND",
                       "SPELL", "STILL", "STUDY", "THEIR", "THERE",
                       "THESE", "THING", "THINK", "THREE", "WATER",
                       "WHERE", "WHICH", "WORLD", "WOULD", "WRITE"]
    letter_pos = 0
    while len(valid_passwords) > 1:
        # Do-while to obtain the letters
        while True:
            letters = get_input(f"Input the list of letters in position {letter_pos+1}: ")
            if letters in ("EXIT", "QUIT"):
                return

            if letters.isalpha() and len(letters) <= 6:
                break

            print("Invalid letter sequence. Please try again")

        letters = list(letters)

        # We have to copy the password list so we can remove items from the
        # original list whilst still correctly iterating over the list.
        valid_passwords_copy = valid_passwords[:]
        for word in valid_passwords_copy:
            if word[letter_pos] not in letters:
                valid_passwords.remove(word)
        letter_pos += 1

    # Now there is at most one word in the list. If there's none, the user
    # made an error and we tell them to try again
    if len(valid_passwords) == 0:
        print("Invalid input letters. Please run module again")
    else:
        print("\nThe password is " + bold(valid_passwords[0]) + "\n")


def needy_knob():
    """Solves (temporarily) the needy knob module."""
    valid_lights = {"44": "UP", "43": "UP", "53": "DOWN", "32": "DOWN",
                    "14": "LEFT", "03": "LEFT", "54": "RIGHT", "52": "RIGHT"}
    # Do-while for input
    while True:
        lights = get_input("\nInput the number of lit lights on the left hand side, "
                           "and the number on the right: ")
        if len(lights) < 2:
            print("Please input two separate numbers")
        elif not lights[0].isdigit() or not lights[-1].isdigit():
            print("Please only input two digits")
        else:
            lights_stripped = lights[0] + lights[-1]
            if lights_stripped not in valid_lights.keys():
                print("Invalid light sequence")
            else:
                print("\n" + bold(valid_lights[lights_stripped]) + "\n")
                return


# ---------------------------------------------------------- #
#                                                            #
#                       USAGE FUNCTIONS                      #
#                                                            #
# ---------------------------------------------------------- #

def parse_module(bomb):
    """Gets input from user regarding what module to solve/option to
    run, and attempts to parse it as a valid choice. Currently is very
    naive and almost certainly won't cover every option people would
    want to give it.
    """
    while True:
        func_to_call = get_input('Which module would you like to solve? '
                                 '(type "help" for options): ')
        if func_to_call in ("SIMPLEWIRES", "SIMPLE", "WIRES"):
            module = simple_wires.SimpleWires(bomb)
            module.solve()
        elif func_to_call in ("BUTTON",):
            button(bomb)
        elif func_to_call in ("SYMBOL", "SYMBOLS", "SYM", "KEYPAD"):
            keypad()
        elif func_to_call in ("SIMON", "SIMONSAYS"):
            simon(bomb)
        elif func_to_call in ("WOF", "WHOSONFIRST", "WHO'SONFIRST"):
            whos_on_first()
        elif func_to_call in ("MEMORY",):
            memory()
        elif func_to_call in ("MORSE", "MORSECODE"):
            morse()
        elif func_to_call in ("COMP", "COMPLICATED", "COMPLICATEDWIRES"):
            module = complicated_wires.ComplicatedWires(bomb)
            module.solve()
        elif func_to_call in ("SEQUENCE", "SEQUENCES", "WIRESEQUENCE", "WIRESEQUENCES"):
            sequences()
        elif func_to_call in ("MAZE", "MAZES"):
            maze()
        elif func_to_call in ("PASSWORD", "PASS"):
            password()
        elif func_to_call in ("NEEDY", "KNOB", "NEEDYKNOB", "DIAL"):
            needy_knob()
        elif func_to_call in ("STRIKE",):
            strike(bomb)
        elif func_to_call in ("NUMSTRIKE", "NUMSTRIKES"):
            num_strikes(bomb)
        elif func_to_call in ("RESETSTRIKE", "RESETSTRIKES"):
            reset_strikes(bomb)
        elif func_to_call in ("CONFIG", "CONF"):
            config_bomb(bomb)
        elif func_to_call in ("HELP", "H", "-H", "--HELP"):
            get_help()
        elif func_to_call in ("EXIT", "QUIT"):
            print("\nWe hope your defusal was a success. Come again soon!\n")
            break
        else:
            print("Please try again")


def get_help():
    """Prints list of options to give to the parser, and what they
    do."""
    print("\nKTANE Solver help")
    print("-"*50, end='\n\n')
    print("Valid commands:\n")
    print("   simple         Solve the simple wires module")
    print("   button         Solve the button module")
    print("   symbols        Solve the symbol keypad module")
    print("   simon          Solve the Simon Says module")
    print("   wof            Solve the \"Who's on first?\" module")
    print("   memory         Solve the memory module")
    print("   complicated    Solve the complicated wires module")
    print("   sequence       Solve the wire sequence module")
    print("   maze           Solve the maze module")
    print("   password       Solve the password module")
    print("   knob           Find correct position for needy knob\n")

    print("   strike         Add a strike to the bomb")
    print("   num strikes    Print the number of strikes currently on the bomb")
    print("   reset strike   Reset number of strikes on bomb to zero")
    print("   config         (Re)configure the bomb")
    print("   help           Show this help menu")
    print("   exit           Exit the program\n")


def main():
    """Creates the bomb object with the relevant info, then calls the
    desired function based on user input."""

    print(LOGO)
    print("Welcome to the KTANE solver!")
    print("We hope you have a successful defusal, with minimal death.\n")
    print("\nYou may configure your bomb now if you wish.")
    print("If you do not, we may ask for additional information later")

    # Do-while for input
    while True:
        user_input = get_input("Do you wish to configure your bomb now (recommended)? (Y/n) ")
        if user_input == "" or user_input[0] == "Y":
            bomb = setup_bomb()
            break
        elif user_input[0] == "N":
            bomb = Bomb()
            break
        print("Please select a valid option")

    # Now, we ask the user to supply the name of the module they want to solve

    parse_module(bomb)


if __name__ == "__main__":
    main()
