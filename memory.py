from collections import namedtuple
from enum import IntEnum

from colours import bold
from utils import get_input

class Input(IntEnum):
    DISPLAY = 0
    LABEL = 1
    POSITION = 2

Stage = namedtuple("Stage", ["label", "position"])

# Memory functions
def _input(arg):
    """Gets input for the Memory module. Either asks for number on
    display, which value was in the button pressed, or which position
    the pressed button was in, depending on the argument provided.
    """

    # Do-while for input
    while True:
        if arg == Input.DISPLAY:
            ipt = get_input("Input the number on the display: ")
        elif arg == Input.LABEL:
            ipt = get_input("What value was in that position? ")
        elif arg == Input.POSITION:
            ipt = get_input("Which position was that in? ")
        else:
            raise ValueError(f"Invalid argument: {arg}")

        if ipt.isdigit() and 1 <= int(ipt) <= 4:
            print("")  # Blank line
            return int(ipt)
        print("Invalid input")

class Memory:
    def __init__(self):
        self.stages = []

    def stage_1(self):
        """Solve and store results from stage 1 of the Memory Module."""
        ipt = _input(Input.DISPLAY)
        if ipt in (1, 2):
            print(f'Press the button in {bold("POSITION 2")}\n')
            self.stages.append(Stage(_input(Input.LABEL), 2))
        elif ipt == 3:
            print(f'Press the button in {bold("POSITION 3")}\n')
            self.stages.append(Stage(_input(Input.LABEL), 3))
        elif ipt == 4:
            print(f'Press the button in {bold("POSITION 4")}\n')
            self.stages.append(Stage(_input(Input.LABEL), 4))
        else:
            raise ValueError(f"Invalid option passed to memory stage 1: {ipt}")

    def stage_2(self):
        """Solve and store results from stage 2 of the Memory Module."""
        ipt = _input(Input.DISPLAY)
        if ipt == 1:
            print(f'Press the button with {bold("LABEL 4")}\n')
            self.stages.append(Stage(4, _input(Input.POSITION)))
        elif ipt in (2, 4):
            print(f'Press the button in {bold(f"POSITION {self.stages[0].position}")}\n')
            self.stages.append(Stage(_input(Input.LABEL), self.stages[0].position))
        elif ipt == 3:
            print(f'Press the button in {bold("POSITION 1")}\n')
            self.stages.append(Stage(_input(Input.LABEL), 1))
        else:
            raise ValueError(f"Invalid option passed to memory stage 2: {ipt}")

    def stage_3(self):
        """Solve and store results from stage 3 of the Memory Module."""
        ipt = _input(Input.DISPLAY)
        if ipt == 1:
            print(f'Press the button with {bold(f"LABEL {self.stages[1].label}")}\n')
            self.stages.append(Stage(self.stages[1].label, _input(Input.POSITION)))
        elif ipt == 2:
            print(f'Press the button with {bold(f"LABEL {self.stages[0].label}")}\n')
            self.stages.append(Stage(self.stages[0].label, _input(Input.POSITION)))
        elif ipt == 3:
            print(f'Press the button in {bold("POSITION 3")}\n')
            self.stages.append(Stage(_input(Input.LABEL), 3))
        elif ipt == 4:
            print(f'Press the button with {bold("LABEL 4")}\n')
            self.stages.append(Stage(4, _input(Input.POSITION)))
        else:
            raise ValueError(f"Invalid option passed to memory stage 3: {ipt}")

    def stage_4(self):
        """Solve and store results from stage 4 of the Memory Module."""
        ipt = _input(Input.DISPLAY)
        if ipt == 1:
            print(f'Press the button in {bold(f"POSITION {self.stages[0].label}")}\n')
            self.stages.append(Stage(self.stages[0].label, _input(Input.POSITION)))
        elif ipt == 2:
            print(f'Press the button in {bold("POSITION 1")}\n')
            self.stages.append(Stage(_input(Input.LABEL), 1))
        elif ipt in (3, 4):
            print(f'Press the button in {bold(f"POSITION {self.stages[1].position}")}\n')
            self.stages.append(Stage(_input(Input.LABEL), self.stages[1].position))
        else:
            raise ValueError(f"Invalid option passed to memory stage 4: {ipt}")

    def stage_5(self):
        """Solve and store results from stage 5 of the Memory Module."""
        ipt = _input(Input.DISPLAY)
        if ipt == 1:
            print(f'Press the button with {bold(f"LABEL {self.stages[0].label}")}\n')
        elif ipt == 2:
            print(f'Press the button with {bold(f"LABEL {self.stages[1].label}")}\n')
        elif ipt == 3:
            print(f'Press the button with {bold(f"LABEL {self.stages[3].label}")}\n')
        elif ipt == 4:
            print(f'Press the button with {bold(f"LABEL {self.stages[2].label}")}\n')
        else:
            raise ValueError(f"Invalid option passed to memory stage 5: {ipt}")

    def solve(self):
        self.stage_1()
        self.stage_2()
        self.stage_3()
        self.stage_4()
        self.stage_5()
