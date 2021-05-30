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


class Indicator:
    """Indicator object.

    Holds information about the three-letter indicators present
    on the bomb.
    """

    def __init__(self, name):
        self.name = name
        self.present = None
        self.lit = None

    def __repr__(self):
        present_prefix = "" if self.present else "not "
        lit_prefix = "" if self.lit else "not "
        return f"{self.name.upper()}: {present_prefix}present, {lit_prefix}lit"

    @property
    def present(self):
        while self.__present is None:
            self.present = input(f"Is there an indicator with {self.name} (Y/N)? ").upper()
        return self.__present

    @present.setter
    def present(self, value):
        if value is None or isinstance(value, bool):
            self.__present = value
            return
        if value.startswith("Y"):
            self.__present = True
        elif value.startswith("N"):
            self.__present = False
            self.lit = False
        else:
            print("Invalid input")

    @property
    def lit(self):
        if self.present is False:  # If there's no indicator, it can't be lit
            return False
        while self.__lit is None:
            self.lit = input(f"Is the indicator with label {self.name} lit (Y/N)? ").upper()
        return self.__lit

    @lit.setter
    def lit(self, value):
        if value is None or isinstance(value, bool):
            self.__lit = value
            return
        if value.startswith("Y"):
            self.__lit = True
        elif value.startswith("N"):
            self.__lit = False
        else:
            print("Invalid input")


class Port:
    """Indicator object.

    Holds information about ports present on the bomb.
    """

    def __init__(self, name):
        self.name = name
        self.present = None

    def __repr__(self):
        status = "present" if self.present else "not present"
        return f"{self.name}: {status}"

    def __bool__(self):
        return self.present

    @property
    def present(self):
        while self.__present is None:
            self.present = input(f"Is there a {self.name} on the bomb (Y/N)? ").upper()
        return self.__present

    @present.setter
    def present(self, value):
        if value is None:
            self.__present = None
            return
        if value.startswith("Y"):
            self.__present = True
        elif value.startswith("N"):
            self.__present = False
        else:
            print("Invalid input")


class Bomb:
    """Bomb object.

    Holds configuration information for the bomb.
    """

    def __init__(self):
        self.serial = None
        self.batteries = None
        self.strikes = 0

    def __repr__(self):
        rep  = f"Bomb: serial: {self.serial}\n"
        rep += f"      batteries: {self.batteries}\n"
        rep += f"      {self.parallel_port!r}\n"
        rep += f"      {self.CAR!r}\n"
        rep += f"      {self.FRK!r}"
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

    def __getattr__(self, attr):
        if attr.isupper() and len(attr) == 3:  # Indicator
            indicator = Indicator(attr)
            setattr(self, attr, indicator)
            return indicator
        if attr.endswith("_port"):
            port = Port(attr)
            setattr(self, attr, port)
            return port
        raise AttributeError(f"'{__class__.__name__}' object has no attribute '{attr}'")


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
