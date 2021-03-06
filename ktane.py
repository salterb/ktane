#!/usr/bin/env python3
"""
KTANE Solver

A friendly interactive manual, written in Python3, to help solve
modules and defuse bombs in Keep Talking and Nobody Explodes.

"""
# We're using setattr to set some attributes, which confuses pylint,
# so silence those errors
# pylint: disable=E1101

import button
import complicated_wires
import keypad
import maze
import memory
import morse
import needy_knob
import password
import simon
import simple_wires
import wire_sequence
import wof
from utils import get_input

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
        rep += f"      batteries: {self.batteries}\n"
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
            self.CAR = input("Is there a lit indicator with label CAR? (Y/N) ").upper()
        return self.__CAR

    @CAR.setter
    def CAR(self, val):
        self._boolean_setter("CAR", val)

    @property
    def FRK(self):
        while self.__FRK is None:
            self.FRK = input("Is there a lit indicator with label FRK? (Y/N) ").upper()
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
            module = keypad.Keypad()
        elif func_to_call in ("SIMON", "SIMONSAYS"):
            module = simon.Simon(bomb)
        elif func_to_call in ("WOF", "WHOSONFIRST", "WHO'SONFIRST"):
            module = wof.WOF()
        elif func_to_call in ("MEMORY",):
            module = memory.Memory()
        elif func_to_call in ("MORSE", "MORSECODE"):
            module = morse.Morse()
        elif func_to_call in ("COMP", "COMPLICATED", "COMPLICATEDWIRES"):
            module = complicated_wires.ComplicatedWires(bomb)
        elif func_to_call in ("SEQUENCE", "SEQUENCES", "WIRESEQUENCE", "WIRESEQUENCES"):
            module = wire_sequence.WireSequence()
        elif func_to_call in ("MAZE", "MAZES"):
            module = maze.Maze()
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
    solve_modules()

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):  # Catch CTRL+C and CTRL+D
        print("\n\nWe hope your defusal was a success. Come again soon!\n")
