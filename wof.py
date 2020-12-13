"""Who's On First

The Who's On First module consists of a display which shows 0-2 words,
and 6 buttons underneath, each of which shows 1-2 words.
"""


from utils import get_input

def get_wof_display():
    """Prompt user for input to get the word on the display."""
    while True:
        display = get_input('\nWhat word is on the display? (type "exit" to cancel): ')
        if display in ("EXIT", "QUIT"):
            print("Exiting\n")
            return None
        if display in VALID_DISPLAYS:
            return display
        print("Please input a valid display entry")

def get_wof_button(display):
    """Prompt user for input to get the word on a specific button."""
    while True:
        button = get_input(f"What word is on the {DISPLAY_DICT[display]} button? ")
        if button == ("EXIT", "QUIT"):
            print("Exiting\n")
            return None
        if button in VALID_BUTTONS:
            return button
        print("Please input a valid button entry")


class WOF:
    """Class to represent the Who's On First module. Solving requires
    inputting the word(s) on the display. This then prompts for the
    word(s) on a specific button. Based on the latter word(s), the user
    must press the first word in a list of words that appears on one of
    their buttons.
    """
    def __init__(self):
        pass

    def solve(self):
        """Solves the "Who's on first" module, by outputting the list of
        potential solutions in order.
        """
        # We keep going until the user wants to stop
        while True:
            display = get_wof_display()
            if display is None:  # "EXIT" or "QUIT"
                return
            button = get_wof_button(display)
            if button is None:  # "EXIT" or "QUIT"
                return
            print("\nThe button to press is the first valid entry in the following list: ")
            for word in BUTTON_DICT[button]:
                print(word)


if __name__ == "__main__":
    print("Please run the script ktane.py instead!")

# WOF data
# pylint: disable=C0301
VALID_DISPLAYS = ['YES', 'FIRST', 'DISPLAY', 'OKAY', 'SAYS', 'NOTHING', '',
                  'BLANK', 'NO', 'LED', 'LEAD', 'READ', 'RED', 'REED',
                  'LEED', 'HOLDON', 'YOU', 'YOUARE', 'YOUR', "YOU'RE", 'UR',
                  'THERE', "THEY'RE", 'THEIR', 'THEYARE', 'SEE', 'C', 'CEE']

DISPLAY_DICT = \
{'YES': 'middle left', 'FIRST': 'top right', 'DISPLAY': 'bottom right',
'OKAY': 'top right', 'SAYS': 'bottom right', 'NOTHING': 'middle left',
'': 'bottom left', 'BLANK': 'middle right', 'NO': 'bottom right',
'LED': 'middle left', 'LEAD': 'bottom right', 'READ': 'middle right',
'RED': 'middle right', 'REED': 'bottom left', 'LEED': 'bottom left',
'HOLDON': 'bottom right', 'YOU': 'middle right', 'YOUARE': 'bottom right',
'YOUR': 'middle right', "YOU'RE": 'middle right', 'UR': 'top left',
'THERE': 'bottom right', "THEY'RE": 'bottom left', 'THEIR': 'middle right',
'THEYARE': 'middle left', 'SEE': 'bottom right', 'C': 'top right',
'CEE': 'bottom right'}

VALID_BUTTONS = ['READY', 'FIRST', 'NO', 'BLANK', 'NOTHING', 'YES', 'WHAT',
                 'UHHH', 'LEFT', 'RIGHT', 'MIDDLE', 'OKAY', 'WAIT', 'PRESS',
                 'YOU', 'YOUARE', 'YOUR', "YOU'RE", 'UR', 'U', 'UHHUH',
                 'UHUH', 'WHAT?', 'DONE', 'NEXT', 'HOLD', 'SURE', 'LIKE']

BUTTON_DICT = \
{'READY': ['YES', 'OKAY', 'WHAT', 'MIDDLE', 'LEFT', 'PRESS', 'RIGHT', 'BLANK', 'READY', 'NO', 'FIRST', 'UHHH', 'NOTHING', 'WAIT'],
'FIRST': ['LEFT', 'OKAY', 'YES', 'MIDDLE', 'NO', 'RIGHT', 'NOTHING', 'UHHH', 'WAIT', 'READY', 'BLANK', 'WHAT', 'PRESS', 'FIRST'],
'NO': ['BLANK', 'UHHH', 'WAIT', 'FIRST', 'WHAT', 'READY', 'RIGHT', 'YES', 'NOTHING', 'LEFT', 'PRESS', 'OKAY', 'NO', 'MIDDLE'],
'BLANK': ['WAIT', 'RIGHT', 'OKAY', 'MIDDLE', 'BLANK', 'PRESS', 'READY', 'NOTHING', 'NO', 'WHAT', 'LEFT', 'UHHH', 'YES', 'FIRST'],
'NOTHING': ['UHHH', 'RIGHT', 'OKAY', 'MIDDLE', 'YES', 'BLANK', 'NO', 'PRESS', 'LEFT', 'WHAT', 'WAIT', 'FIRST', 'NOTHING', 'READY'],
'YES': ['OKAY', 'RIGHT', 'UHHH', 'MIDDLE', 'FIRST', 'WHAT', 'PRESS', 'READY', 'NOTHING', 'YES', 'LEFT', 'BLANK', 'NO', 'WAIT'],
'WHAT': ['UHHH', 'WHAT', 'LEFT', 'NOTHING', 'READY', 'BLANK', 'MIDDLE', 'NO', 'OKAY', 'FIRST', 'WAIT', 'YES', 'PRESS', 'RIGHT'],
'UHHH': ['READY', 'NOTHING', 'LEFT', 'WHAT', 'OKAY', 'YES', 'RIGHT', 'NO', 'PRESS', 'BLANK', 'UHHH', 'MIDDLE', 'WAIT', 'FIRST'],
'LEFT': ['RIGHT', 'LEFT', 'FIRST', 'NO', 'MIDDLE', 'YES', 'BLANK', 'WHAT', 'UHHH', 'WAIT', 'PRESS', 'READY', 'OKAY', 'NOTHING'],
'RIGHT': ['YES', 'NOTHING', 'READY', 'PRESS', 'NO', 'WAIT', 'WHAT', 'RIGHT', 'MIDDLE', 'LEFT', 'UHHH', 'BLANK', 'OKAY', 'FIRST'],
'MIDDLE': ['BLANK', 'READY', 'OKAY', 'WHAT', 'NOTHING', 'PRESS', 'NO', 'WAIT', 'LEFT', 'MIDDLE', 'RIGHT', 'FIRST', 'UHHH', 'YES'],
'OKAY': ['MIDDLE', 'NO', 'FIRST', 'YES', 'UHHH', 'NOTHING', 'WAIT', 'OKAY', 'LEFT', 'READY', 'BLANK', 'PRESS', 'WHAT', 'RIGHT'],
'WAIT': ['UHHH', 'NO', 'BLANK', 'OKAY', 'YES', 'LEFT', 'FIRST', 'PRESS', 'WHAT', 'WAIT', 'NOTHING', 'READY', 'RIGHT', 'MIDDLE'],
'PRESS': ['RIGHT', 'MIDDLE', 'YES', 'READY', 'PRESS', 'OKAY', 'NOTHING', 'UHHH', 'BLANK', 'LEFT', 'FIRST', 'WHAT', 'NO', 'WAIT'],
'YOU': ['SURE', 'YOU ARE', 'YOUR', "YOU'RE", 'NEXT', 'UH HUH', 'UR', 'HOLD', 'WHAT?', 'YOU', 'UH UH', 'LIKE', 'DONE', 'U'],
'YOUARE': ['YOUR', 'NEXT', 'LIKE', 'UH HUH', 'WHAT?', 'DONE', 'UH UH', 'HOLD', 'YOU', 'U', "YOU'RE", 'SURE', 'UR', 'YOU ARE'],
'YOUR': ['UH UH', 'YOU ARE', 'UH HUH', 'YOUR', 'NEXT', 'UR', 'SURE', 'U', "YOU'RE", 'YOU', 'WHAT?', 'HOLD', 'LIKE', 'DONE'],
"YOU'RE": ['YOU', "YOU'RE", 'UR', 'NEXT', 'UH UH', 'YOU ARE', 'U', 'YOUR', 'WHAT?', 'UH HUH', 'SURE', 'DONE', 'LIKE', 'HOLD'],
'UR': ['DONE', 'U', 'UR', 'UH HUH', 'WHAT?', 'SURE', 'YOUR', 'HOLD', "YOU'RE", 'LIKE', 'NEXT', 'UH UH', 'YOU ARE', 'YOU'],
'U': ['UH HUH', 'SURE', 'NEXT', 'WHAT?', "YOU'RE", 'UR', 'UH UH', 'DONE', 'U', 'YOU', 'LIKE', 'HOLD', 'YOU ARE', 'YOUR'],
'UHHUH': ['UH HUH', 'YOUR', 'YOU ARE', 'YOU', 'DONE', 'HOLD', 'UH UH', 'NEXT', 'SURE', 'LIKE', "YOU'RE", 'UR', 'U', 'WHAT?'],
'UHUH': ['UR', 'U', 'YOU ARE', "YOU'RE", 'NEXT', 'UH UH', 'DONE', 'YOU', 'UH HUH', 'LIKE', 'YOUR', 'SURE', 'HOLD', 'WHAT?'],
'WHAT?': ['YOU', 'HOLD', "YOU'RE", 'YOUR', 'U', 'DONE', 'UH UH', 'LIKE', 'YOU ARE', 'UH HUH', 'UR', 'NEXT', 'WHAT?', 'SURE'],
'DONE': ['SURE', 'UH HUH', 'NEXT', 'WHAT?', 'YOUR', 'UR', "YOU'RE", 'HOLD', 'LIKE', 'YOU', 'U', 'YOU ARE', 'UH UH', 'DONE'],
'NEXT': ['WHAT?', 'UH HUH', 'UH UH', 'YOUR', 'HOLD', 'SURE', 'NEXT', 'LIKE', 'DONE', 'YOU ARE', 'UR', "YOU'RE", 'U', 'YOU'],
'HOLD': ['YOU ARE', 'U', 'DONE', 'UH UH', 'YOU', 'UR', 'SURE', 'WHAT?', "YOU'RE", 'NEXT', 'HOLD', 'UH HUH', 'YOUR', 'LIKE'],
'SURE': ['YOU ARE', 'DONE', 'LIKE', "YOU'RE", 'YOU', 'HOLD', 'UH HUH', 'UR', 'SURE', 'U', 'WHAT?', 'NEXT', 'YOUR', 'UH UH'],
'LIKE': ["YOU'RE", 'NEXT', 'U', 'UR', 'HOLD', 'DONE', 'UH UH', 'WHAT?', 'UH HUH', 'YOU', 'LIKE', 'SURE', 'YOU ARE', 'YOUR']}
