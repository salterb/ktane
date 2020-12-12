from colours import bold
from utils import get_input

VALID_LIGHTS = {"44": "UP", "43": "UP", "53": "DOWN", "32": "DOWN",
                "14": "LEFT", "03": "LEFT", "54": "RIGHT", "52": "RIGHT"}

def get_knob_input():
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
    def __init__(self):
        self.lights = get_knob_input()

    def solve(self):
        print(f'Turn knob {bold(VALID_LIGHTS[self.lights])} relative to "UP"')
