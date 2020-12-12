from colours import bold
from utils import get_input

red_cuts = {0: "C", 1: "B", 2: "A", 3: "AC", 4: "B",
            5: "AC", 6: "ABC", 7: "AB", 8: "B"}
blue_cuts = {0: "B", 1: "AC", 2: "B", 3: "A", 4: "B",
             5: "BC", 6: "C", 7: "AC", 8: "A"}
black_cuts = {0: "ABC", 1: "AC", 2: "B", 3: "AC", 4: "B",
              5: "BC", 6: "AB", 7: "C", 8: "C"}


def cut():
    """Informs the user to cut the wire."""
    print(f"\n{bold('CUT')} the wire")

def no_cut():
    """Informs the user NOT to cut the wire."""
    print(f"\nDo {bold('NOT')} cut the wire")


def is_valid_wire_sequence(wire):
    """Verifies the provided wire sequence consists of valid
    characters.
    """
    if len(wire) == 2 and wire[0] in ("R", "B", "K") and wire[1] in ("A", "B", "C"):
        return True
    return False


class WireSequence:
    def __init__(self):
        self.red = 0
        self.blue = 0
        self.black = 0
        self.sequence = []

    def get_wire(self):
        while True:
            wire = get_input("\nInput the colour of the wire, and the letter to which "
                             "it is connected. Use 'K' for black.\n"
                             "(Type 'exit' to exit, 'undo' to undo previous move.) ")
            if wire == "EXIT":
                print("\nExiting\n")
                return None

            if wire == "UNDO":
                if not self.sequence:
                    print("Nothing to undo!")
                else:
                    self.sequence.pop()
                    print("Last move undone")
            elif is_valid_wire_sequence(wire):
                return wire
            print("Invalid wire")

    def solve(self):
        # Keep going until the user wants to exit
        while True:
            wire = self.get_wire()
            if wire is None:  # "EXIT"
                return

            # Now our wire is valid, we provide output.
            # TODO this isn't very DRY. We could clean this up
            if wire[0] == "R":
                if wire[1] in red_cuts[self.red]:
                    cut()
                else:
                    no_cut()
                self.red += 1
            elif wire[0] == "B":
                if wire[1] in blue_cuts[self.blue]:
                    cut()
                else:
                    no_cut()
                self.blue += 1
            elif wire[0] == "K":
                if wire[1] in black_cuts[self.black]:
                    cut()
                else:
                    no_cut()
                self.black += 1
