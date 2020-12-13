"""Simple Wires

The Simple Wires module consists of 3-6 horizontal wires with various
possible colours.
"""

from utils import get_input
from colours import bold

def _is_valid_simple_wires(wires):
    """Helper function to determine if the wire arrangement specified
    is valid.
    """
    if len(wires) < 3 or len(wires) > 6:
        return False
    for char in wires:
        if char not in ('K', 'B', 'Y', 'R', 'W'):
            return False
    return True


class SimpleWires:
    """Class to represent the SimpleWires module. Solving requires
    inputting the list of wire colours, and then cutting a wire
    based on a web of conditions based on the number and colours of
    the wires, and the bomb's serial number
    """
    def __init__(self, bomb):
        # Do-while to get the wire sequence
        while True:
            wire_sequence = get_input("Input the wire sequence. Use one letter per wire. "
                                      "Use 'K' for black: ")
            if _is_valid_simple_wires(wire_sequence):
                self.wires = wire_sequence
                break
            print("Invalid wire sequence")
        self.bomb = bomb

    def __repr__(self):
        return self.wires

    def _solve_3_wires(self):
        if "R" not in self.wires:
            print(f'\nCut the {bold("SECOND")} wire\n')
        elif self.wires[-1] == "W":
            print(f'\nCut the {bold("LAST")} wire')
        elif self.wires.count("B") > 1:
            print(f'\nCut the {bold("LAST BLUE")} wire\n')
        else:
            print(f'\nCut the {bold("LAST")} wire\n')

    def _solve_4_wires(self):
        if self.wires.count("R") > 1 and int(self.bomb.serial[-1]) % 2 == 1:
            print(f'\nCut the {bold("LAST RED")}  wire\n')
        elif self.wires[-1] == "Y" and "R" not in self.wires:
            print(f'\nCut the {bold("FIRST")} wire\n')
        elif self.wires.count("B") == 1:
            print(f'\nCut the {bold("FIRST")} wire\n')
        elif self.wires.count("Y") > 1:
            print(f'\nCut the {bold("LAST")} wire\n')
        else:
            print(f'\nCut the {bold("SECOND")} wire\n')

    def _solve_5_wires(self):
        if self.wires[-1] == "K" and int(self.bomb.serial[-1]) % 2 == 1:
            print(f'\nCut the {bold("FOURTH")} wire\n')
        elif self.wires.count("R") == 1 and self.wires.count('Y') > 1:
            print(f'\nCut the {bold("FIRST")} wire\n')
        elif "K" not in self.wires:
            print(f'\nCut the {bold("SECOND")} wire\n')
        else:
            print(f'\nCut the {bold("FIRST")} wire\n')

    def _solve_6_wires(self):
        if "Y" not in self.wires and int(self.bomb.serial[-1]) % 2 == 1:
            print(f'\nCut the {bold("THIRD")} wire\n')
        elif self.wires.count("Y") == 1 and self.wires.count("W") > 1:
            print(f'\nCut the {bold("FOURTH")} wire\n')
        elif "R" not in self.wires:
            print(f'\nCut the {bold("LAST")} wire\n')
        else:
            print(f'\nCut the {bold("FOURTH")} wire\n')

    def solve(self):
        """Solve the simple wires module on the bomb. The user inputs the
        sequence of wires, and the function tells the user which one to
        cut.
        """
        solver = getattr(self, f"_solve_{len(self.wires)}_wires")
        solver()
