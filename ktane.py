#!/usr/bin/env python3

"""
KTANE Solver

A friendly interactive manual, written in Python3, to help solve
modules and defuse bombs in Keep Talking and Nobody Explodes.

"""
from collections import namedtuple
from sys import version_info, exit

import button
import complicated_wires
import morse
import needy_knob
import password
import simon
import simple_wires
import symbol
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
                 batteries=None,
                 parallel_port=None,
                 CAR=None,
                 FRK=None):
        self.serial = serial                # The bomb's serial number
        self.batteries = batteries          # The number of batteries on the bomb
        self.parallel_port = parallel_port  # Is there a parallel port?
        self.CAR = CAR                      # Is there a _lit_ CAR indicator?
        self.FRK = FRK                      # Is there a _lit_ FRK indicator?
        self.strikes = 0

    def __repr__(self):
        rep  = f"Bomb: serial: {self.serial}\n"
        rep += f"      num_batteries: {self.num_batteries}\n"
        rep += f"      parallel_port: {self.parallel_port}\n"
        rep += f"      CAR: {self.CAR}\n"
        rep += f"      FRK: {self.FRK}"
        return rep

    @property
    def serial(self):
        while self.__serial is None:
            self.serial = get_input("Input the bomb's serial number: ")
        return self.__serial

    @serial.setter
    def serial(self, val):
        if val is None:
            self.__serial = None
            return
        if val.isalnum() and len(val) == 6 and (val[-1]).isdigit():
            self.__serial = val
        else:
            print("Invalid serial number")

    @property
    def batteries(self):
        while self.__batteries is None:
            self.batteries = input("Input the number of batteries on the bomb: ")
        return self.__batteries

    @batteries.setter
    def batteries(self, val):
        if val is None:
            self.__batteries = None
            return
        try:
            self.__batteries = int(val)
        except ValueError:
            print("Invalid number of batteries")

    @property
    def parallel_port(self):
        while self.__parallel_port is None:
            self.parallel_port = input("Does the bomb have a parallel port? (Y/N) ").upper()
        return self.__parallel_port

    @parallel_port.setter
    def parallel_port(self, val):
        self._boolean_setter("parallel_port", val)

    @property
    def CAR(self):
        while self.__CAR is None:
            self.CAR = input(f"Is there a lit indicator with label CAR? (Y/N) ").upper()
        return self.__CAR

    @CAR.setter
    def CAR(self, val):
        self._boolean_setter("CAR", val)

    @property
    def FRK(self):
        while self.__FRK is None:
            self.FRK = input(f"Is there a lit indicator with label FRK? (Y/N) ").upper()
        return self.__FRK

    @FRK.setter
    def FRK(self, val):
        self._boolean_setter("FRK", val)

    def _boolean_setter(self, name, val):
        # "Real" attributes are saved as __attr, which is
        # represented internally as _class__attr.
        # setattr on a dunder doesn't do this properly, instead
        # just setting __attr, so we need to hack the name together.
        dunder_name = f"_{__class__.__name__}__{name}"
        if val is None:
            setattr(self, dunder_name, None)
            return
        if len(val) > 0 and val[0] == "Y":
            setattr(self, dunder_name, True)
        elif len(val) > 0 and val[0] == "N":
            setattr(self, dunder_name, False)
        else:
            print("Invalid input")

    def reset_strikes(self):
        self.strikes = 0


# ---------------------------------------------------------- #
#                                                            #
#                         HELPERS                            #
#                                                            #
# ---------------------------------------------------------- #


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
    if len(wire) >= 2 and wire[0] in ("R", "B", "K") and wire[-1] in ("A", "B", "C"):
        return True
    return False


# ---------------------------------------------------------- #
#                                                            #
#                         MODULES                            #
#                                                            #
# ---------------------------------------------------------- #


def memory():
    """Solves the memory module by storing all previous input and
    automatically referring back to it to find the correct answers.
    """
    DISPLAY = 0
    WHICH_LABEL = 1
    WHICH_POSITION = 2

    stage = namedtuple("stage", ["label", "position"])
    # Stage 1
    ipt = _memory_input(DISPLAY)
    print("")  # Blank line
    if ipt in (1, 2):
        print(f'Press the button in {bold("POSITION 2")}\n')
        stage1 = stage(_memory_input(WHICH_LABEL), 2)
    elif ipt == 3:
        print(f'Press the button in {bold("POSITION 3")}\n')
        stage1 = stage(_memory_input(WHICH_LABEL), 3)
    elif ipt == 4:
        print(f'Press the button in {bold("POSITION 4")}\n')
        stage1 = stage(_memory_input(WHICH_LABEL), 4)
    else:
        raise ValueError(f"Invalid option passed to memory stage 1: {ipt}")

    # Stage 2
    ipt = _memory_input(DISPLAY)
    print("")  # Blank line
    if ipt == 1:
        print(f'Press the button with {bold("LABEL 4")}\n')
        stage2 = stage(4, _memory_input(WHICH_POSITION))
    elif ipt in (2, 4):
        print(f'Press the button in {bold(f"POSITION {stage1.position}")}\n')
        stage2 = stage(_memory_input(WHICH_LABEL), stage1.position)
    elif ipt == 3:
        print(f'Press the button in {bold("POSITION 1")}\n')
        stage2 = stage(_memory_input(WHICH_LABEL), 1)
    else:
        raise ValueError(f"Invalid option passed to memory stage 2: {ipt}")

    # Stage 3
    ipt = _memory_input(DISPLAY)
    print("")  # Blank line
    if ipt == 1:
        print(f'Press the button with {bold(f"LABEL {stage2.label}")}\n')
        stage3 = stage(stage2.label, _memory_input(WHICH_POSITION))
    elif ipt == 2:
        print(f'Press the button with {bold(f"LABEL {stage1.label}")}\n')
        stage3 = stage(stage1.label, _memory_input(WHICH_POSITION))
    elif ipt == 3:
        print(f'Press the button in {bold("POSITION 3")}\n')
        stage3 = stage(_memory_input(WHICH_LABEL), 3)
    elif ipt == 4:
        print(f'Press the button with {bold("LABEL 4")}\n')
        stage3 = stage(4, _memory_input(WHICH_POSITION))
    else:
        raise ValueError(f"Invalid option passed to memory stage 3: {ipt}")

    # Stage 4
    ipt = _memory_input(DISPLAY)
    print("")  # Blank line
    if ipt == 1:
        print(f'Press the button in {bold(f"POSITION {stage1.label}")}\n')
        stage4 = stage(stage1.label, _memory_input(WHICH_POSITION))
    elif ipt == 2:
        print(f'Press the button in {bold("POSITION 1")}\n')
        stage4 = stage(_memory_input(WHICH_LABEL), 1)
    elif ipt in (3, 4):
        print(f'Press the button in {bold(f"POSITION {stage2.position}")}\n')
        stage4 = stage(_memory_input(WHICH_LABEL), stage2.position)
    else:
        raise ValueError(f"Invalid option passed to memory stage 4: {ipt}")

    # Stage 5
    ipt = _memory_input(DISPLAY)
    print("")  # Blank line
    if ipt == 1:
        print(f'Press the button with {bold(f"LABEL {stage1.label}")}\n')
    elif ipt == 2:
        print(f'Press the button with {bold(f"LABEL {stage2.label}")}\n')
    elif ipt == 3:
        print(f'Press the button with {bold(f"LABEL {stage4.label}")}\n')
    elif ipt == 4:
        print(f'Press the button with {bold(f"LABEL {stage3.label}")}\n')
    else:
        raise ValueError(f"Invalid option passed to memory stage 5: {ipt}")


def sequences():
    """Loads an interface that can solve the wire sequences module.
    Also implements a "delete" function in case of accidental input.
    """
    RED = -1
    BLUE = -2
    BLACK = -3
    valid_reds = {0: "C", 1: "B", 2: "A", 3: "AC", 4: "B",
                  5: "AC", 6: "ABC", 7: "AB", 8: "B"}
    valid_blues = {0: "B", 1: "AC", 2: "B", 3: "A", 4: "B",
                   5: "BC", 6: "C", 7: "AC", 8: "A"}
    valid_blacks = {0: "ABC", 1: "AC", 2: "B", 3: "AC", 4: "B",
                    5: "BC", 6: "AB", 7: "C", 8: "C"}
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
        if wire[0] == "R":
            if wire[1] in valid_reds[red_count]:
                cut()
            else:
                no_cut()
            red_count += 1
            previous_move = RED
        elif wire[0] == "B":
            if wire[1] in valid_blues[blue_count]:
                cut()
            else:
                no_cut()
            blue_count += 1
            previous_move = BLUE
        elif wire[0] == "K":
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


# ---------------------------------------------------------- #
#                                                            #
#                       USAGE FUNCTIONS                      #
#                                                            #
# ---------------------------------------------------------- #

def solve_modules():
    """Gets input from user regarding what module to solve/option to
    run, and attempts to parse it as a valid choice. Currently is very
    naive and almost certainly won't cover every option people would
    want to give it.
    """
    bomb = Bomb()
    while True:
        module = None
        func_to_call = get_input('Which module would you like to solve? '
                                 '(type "help" for options): ')
        if func_to_call in ("SIMPLEWIRES", "SIMPLE", "WIRES"):
            module = simple_wires.SimpleWires(bomb)
        elif func_to_call in ("BUTTON",):
            module = button.Button(bomb)
        elif func_to_call in ("SYMBOL", "SYMBOLS", "SYM", "KEYPAD"):
            module = symbol.Symbol()
        elif func_to_call in ("SIMON", "SIMONSAYS"):
            module = simon.Simon(bomb)
        elif func_to_call in ("WOF", "WHOSONFIRST", "WHO'SONFIRST"):
            module = wof.WOF()
        elif func_to_call in ("MEMORY",):
            memory()
        elif func_to_call in ("MORSE", "MORSECODE"):
            module = morse.Morse()
        elif func_to_call in ("COMP", "COMPLICATED", "COMPLICATEDWIRES"):
            module = complicated_wires.ComplicatedWires(bomb)
        elif func_to_call in ("SEQUENCE", "SEQUENCES", "WIRESEQUENCE", "WIRESEQUENCES"):
            sequences()
        elif func_to_call in ("MAZE", "MAZES"):
            maze()
        elif func_to_call in ("PASSWORD", "PASS"):
            module = password.Password()
        elif func_to_call in ("NEEDY", "KNOB", "NEEDYKNOB", "DIAL"):
            module = needy_knob.NeedyKnob()
        elif func_to_call in ("STRIKE",):
            bomb.strikes += 1
            print(f"The bomb now has {bomb.strikes} strike{'' if bomb.strikes == 1 else 's'}")
        elif func_to_call in ("NUMSTRIKE", "NUMSTRIKES"):
            print(f"The bomb has {bomb.strikes} strike{'' if bomb.strikes == 1 else 's'}")
        elif func_to_call in ("RESETSTRIKE", "RESETSTRIKES"):
            bomb.reset_strikes()
            print("Bomb strikes reset to 0")
        elif func_to_call in ("RESET", "RESETBOMB"):
            bomb = Bomb()
            print("Bomb config reset")
        elif func_to_call in ("HELP", "H", "-H", "--HELP"):
            get_help()
        elif func_to_call in ("EXIT", "QUIT"):
            print("\nWe hope your defusal was a success. Come again soon!\n")
            break
        else:
            print("Please try again")

        if module:
            module.solve()


def get_help():
    """Prints list of options to give to the parser, and what they
    do."""
    print("\nKTANE Solver help")
    print("-"*50, end="\n\n")
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
    print("   reset          Reset the bomb configuration")
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
    solve_modules()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nWe hope your defusal was a success. Come again soon!\n")
