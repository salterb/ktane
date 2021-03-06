"""Needy Knob

The Needy Knob module is a needy module that consists of a knob with
four possible directions, and a series of lights and an UP indicator to
indicate how to position the knob.
"""

from colours import bold
from utils import get_input

VALID_LIGHTS = {"44": "UP", "43": "UP", "53": "DOWN", "32": "DOWN",
                "14": "LEFT", "03": "LEFT", "54": "RIGHT", "52": "RIGHT"}

def get_knob_input():
    """Prompt user for the number of lights lit on the left/right sides
    sides of the module, and return it as a string.
    """
    while True:
        lights = get_input("\nInput the number of lit lights on the left hand side, "
                           "and the number on the right: ")
        if len(lights) < 2:
            print("Input two separate numbers")
        elif not lights[0].isdigit() or not lights[-1].isdigit():
            print("Invalid string. Input two digits")
        else:
            normalised_lights = lights[0] + lights[-1]
            if normalised_lights not in VALID_LIGHTS:
                print("Invalid light sequence")
            else:
                return normalised_lights

class NeedyKnob:
    """Class to represent the Needy Knob module. Solving requires
    getting the light arrangement, and based off that, turning the knob
    to a specific position relative to the "UP" indicator.
    """
    def __init__(self):
        self.lights = get_knob_input()

    def solve(self):
        """Solve the Needy Knob module."""
        print(f'Turn knob {bold(VALID_LIGHTS[self.lights])} relative to "UP"')
