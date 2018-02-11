#!/usr/bin/env python3

from bomb_config import *
from wof import *
from mazes import solve_maze


class Bomb:
    def __init__(self,
                 serial=None,
                 numBatteries=None,
                 parallelPort=None,
                 CAR=None,
                 FRK=None):
        self.serial = serial              # The bomb's serial number
        self.numBatteries = numBatteries  # The number of batteries on the bomb
        self.parallelPort = parallelPort  # Is there a parallel port?
        self.CAR = CAR                    # Is there a _lit_ CAR indicator?
        self.FRK = FRK                    # Is there a _lit_ FRK indicator?

# ---------------------------------------------------------- #
#                                                            #
#                         HELPERS                            #
#                                                            #
# ---------------------------------------------------------- #

# Wire validator functions
def isValidSimpleWires(wires):
    """ Helper function to determine if the wire arrangement specified
        is valid """
    if len(wires) < 3 or len(wires) > 6:
        return False
    for char in wires:
        if char not in ['K', 'B', 'Y', 'R', 'W']:
            return False
    return True


def isValidCompWire(wire):
    """ Helper function to determine if a string representing a complicated
        wire is valid """
    if len(wire) > 4:
        return False
    for char in wire:
        if char not in ['R', 'B', 'S', 'L']:
            return False
    return True


# "Cut" functions for complicated wires
def cut(bomb):
    print("\n\033[1mCUT\033[0m the wire")


def noCut(bomb):
    print("\nDo \033[1mNOT\033[0m cut the wire")


def serialCut(bomb):
    if bomb.serial is None:
        bomb.serial = addSerial()
    if int(bomb.serial[-1]) % 2 == 0:
        print("\n\033[1mCUT\033[0m the wire")
    else:
        print("\nDo \033[1mNOT\033[0m cut the wire")


def pPortCut(bomb):
    if bomb.parallelPort is None:
        bomb.parallelPort = addPPort()
    if bomb.parallelPort is True:
        print("\n\033[1mCUT\033[0m the wire")
    else:
        print("\nDo \033[1mNOT\033[0m cut the wire")


def batteryCut(bomb):
    if bomb.numBatteries is None:
        bomb.numBatteries = addBatteries()
    if bomb.numBatteries >= 2:
        print("\n\033[1mCUT\033[0m the wire")
    else:
        print("\nDo \033[1mNOT\033[0m cut the wire")


# ---------------------------------------------------------- #
#                                                            #
#                         MODULES                            #
#                                                            #
# ---------------------------------------------------------- #

def simpleWires(bomb):
    """ Solve the simple wires module on the bomb"""

    # Do-while to get the wire sequence
    while True:
        wires = input("Please input the wire sequence (no spaces) ")
        if isValidSimpleWires(wires):
            break
        print("Invalid wire sequence")

    numWires = len(wires)
    if numWires == 3:
        if 'R' in wires:
            print("\nCut the \033[1mSECOND\033[0m wire\n")
        elif wires[-1] == 'W':
            print("\nCut the \033[1mLAST\033[0m wire\n")
        elif wires.count('B') > 1:
            print("\nCut the \033[1;34mLAST BLUE\033[0m wire\n")
        else:
            print("\nCut the \033[1mLAST\033[0m wire\n")

    elif numWires == 4:
        if bomb.serial is None:
            bomb.serial = addSerial()

        if wires.count("R") > 1 and int(bomb.serial[-1]) % 2 == 1:
            print("Cut the \033[1;31mLAST RED\033[0m wire")
        elif wires[-1] == 'Y' and ('R' not in wires):
            print("Cut the \033[1mFIRST\033[0m wire")
        elif wires.count('B') == 1:
            print("Cut the \033[1mFIRST\033[0m wire")
        elif wires.count('Y') > 1:
            print("Cut the \033[1mLAST\033[0m wire")
        else:
            print("Cut the \033[1mSECOND\033[0m wire")

    elif numWires == 5:
        if bomb.serial is None:
            bomb.serial = addSerial()

        if wires[-1] == 'K' and int(bomb.serial[-1]) % 2 == 1:
            print("Cut the \033[1mFOURTH\033[0m wire")
        elif wires.count('R') == 1 and wires.count('Y') > 1:
            print("Cut the \033[1mFIRST\033[0m wire")
        elif 'K' not in wires:
            print("Cut the \033[1mSECOND\033[0m wire")
        else:
            print("Cut the \033[1mFIRST\033[0m wire")

    elif numWires == 6:
        if bomb.serial is None:
            bomb.addSerial()

        if 'Y' not in wires and int(bomb.serial[-1]) % 2 == 1:
            print("Cut the \033[1mTHIRD\033[0m wire")
        elif wires.count('Y') == 1 and wires.count('W') > 1:
            print("Cut the \033[1mFOURTH\033[0m wire")
        elif 'R' not in wires:
            print("Cut the \033[1mLAST\033[0m wire")
        else:
            print("Cut the \033[1mFOURTH\033[0m wire")

    else:
        raise Exception("len(numWires = " + str(len(numWires)) +
                        " - this is apparently not good!")


def button(bomb):
    """ Solves the button module on the bomb.
        This function is ugly. We've used 'if's and returns rather than
        'elif's, since we are also providing functionality for users to
        supply the bomb data at the last possible moment, and that involves
        provisionally going inside if statements to provide user input."""

    # Two do-while loops to get the button color and word
    validColours = ['R', 'B', 'Y', 'W']
    while True:
        buttonColour = input("Please input the button colour: ").upper()
        if buttonColour in validColours:
            break
        print("Please supply a valid colour from [R, B, Y, W]")

    buttonWord = ""
    validWords = ['A', 'D', 'H', 'P']
    while buttonWord not in validWords:
        buttonWord = input("Please input first letter of word "
                           "on button: ").upper()
        if buttonWord not in validWords:
            print("Please supply a valid letter from [A, D, H, P]")

    releaseString = ("\033[1m------ DO NOT IMMEDIATELY "
                     "RELEASE THE BUTTON ------\033[0m\n\n"
                     "If the strip is \033[1;34mBLUE\033[0m, release the "
                     "button when timer has a \033[1;34m4\033[0m in any "
                     "position\nIf the strip is \033[1;38mYELLOW\033[0m, "
                     "has a \033[1;38m5\033[0m in any position\nOtherwise "
                     "release the button when timer has a 1 in any position\n")

    if buttonColour == 'B' and buttonWord == 'A':
        print("\nHold button\n")
        print(releaseString)
        return

    if (buttonWord == 'D' and
        (bomb.numBatteries is None or bomb.numBatteries > 1)):
        if bomb.numBatteries is None:
            bomb.numBatteries = addBatteries()

        if bomb.numBatteries > 1:
            print("\nPress and release button\n")
            return

    if buttonColour == 'W' and bomb.CAR is not False:
        if bomb.CAR is None:
            bomb.CAR = addCAR()

        if bomb.CAR is True:
            print("\nHold button\n")
            print(releaseString)
            return

    if bomb.numBatteries > 2 and bomb.FRK is not False:
        if bomb.FRK is None:
            bomb.FRK = addFRK()

        if bomb.FRK is True:
            print("\nPress and release button\n")
            return

    if buttonColour == 'Y':
        print("Hold button")
        print(releaseString)
        return

    if buttonColour == 'R' and buttonWord == 'H':
        print("\nPress and release button\n")
        return

    else:
        print("Hold button")
        print(releaseString)
        return


def keypad():
    """ TO DO """
    pass


def simon(bomb):
    """ TO DO """
    pass


def whosOnFirst():
    """ Solves the "Who's on first" module, by outputting the list of
        potential solutions in order. """

    # We keep going until the user wants to stop
    while True:
        # Do-while to get the word on the display
        while True:
            display = input("\nWhat word is on the display? (type "
                            "\"exit\" to cancel): ").upper().replace(' ', '')
            if display == "EXIT":
                print("Exiting\n")
                return
            if display in WOFvalidDisplays:
                break
            print("Please input a valid display entry")

        # Do-while to get the word on the button
        while True:
            button = input("What word is on the "+WOFdisplayDict[display]
                           + " button? ").upper().replace(' ', '')
            if button == "EXIT":
                print("Exiting\n")
                return
            if button in WOFvalidButtons:
                break
            print("Please input a valid button entry")

        print("\nThe button to press is the first valid entry "
              "in the following list: ")
        print(WOFbuttonDict[button])


def memory():
    """ TO DO """
    pass


def morse():
    """ TO DO - allow for passing of partial string? """
    pass


def complicatedWires(bomb):
    """ TO DO - pass one wire at a time? """
    # We keep running until the user wants to stop
    print("Use 'R' for 'red', 'B' for 'blue', 'S' for star, and 'L' for light")

    while True:
        # Do-while to obtain the string representing the wire
        while True:
            wire = input("\nPlease input the string representing "
                         "the wire (type \"exit\" to cancel) "
                         "").upper().replace(' ', '').replace('W', '')
            if wire == "EXIT":
                print("Exiting\n")
                return
            if isValidCompWire(wire):
                break
            print("Invalid wire")
        wire = "".join(sorted(wire))  # Get in alphabetical order

        # Now we have 16 different cases to consider.
        # We use a lookup table which runs the correct printing function.
        compWiresDict = \
            {'': cut, 'B': serialCut, 'BL': pPortCut, 'BLR': serialCut,
             'BLRS': noCut, 'BLS': pPortCut, 'BR': serialCut, 'BRS': pPortCut,
             'BS': noCut, 'L': noCut, 'LR': batteryCut, 'LRS': batteryCut,
             'LS': batteryCut, 'R': serialCut, 'RS': cut, 'S': cut}
        compWiresDict[wire](bomb)


def sequences():
    """ TO DO """
    pass


def maze():
    """ TO DO """
    solve_maze()


def password():
    """ Solves the password module """
    validPasswords = ["ABOUT", "AFTER", "AGAIN", "BELOW", "COULD",
                      "EVERY", "FIRST", "FOUND", "GREAT", "HOUSE",
                      "LARGE", "LEARN", "NEVER", "OTHER", "PLACE",
                      "PLANT", "POINT", "RIGHT", "SMALL", "SOUND",
                      "SPELL", "STILL", "STUDY", "THEIR", "THERE",
                      "THESE", "THING", "THINK", "THREE", "WATER",
                      "WHERE", "WHICH", "WORLD", "WOULD", "WRITE"]
    letterPos = 0
    while (len(validPasswords) > 1):
        # Do-while to obtain the letters
        while True:
            letters = input("Please input the list of letters in position "
                            + str(letterPos+1) + ": ").replace(' ', '').upper()
            if letters == "EXIT" or letters == "QUIT":
                return
            elif letters.isalpha() and len(letters) <= 6:
                break

            print("Invalid letter sequence. Please try again")

        letters = list(letters)

        # We have to copy the password list so we can remove items from the
        # original list whilst still correctly iterating over the list.
        validPasswordsCopy = validPasswords[:]
        for word in validPasswordsCopy:
            if word[letterPos] not in letters:
                validPasswords.remove(word)
        letterPos += 1

    # Now there is at most one word in the list. If there's none, the user
    # made an error and we tell them to try again
    if len(validPasswords) == 0:
        print("Invalid input letters. Please run module again")
    else:
        print("\nThe password is \033[1m"+validPasswords[0]+"\033[0m\n")


def setupBomb():
    # Set up the bomb with a bunch of user input
    serial = addSerial()
    numBatteries = addBatteries()
    parallelPort = addPPort()
    CAR = addCAR()
    FRK = addFRK()
    bomb = Bomb(serial, numBatteries, parallelPort, CAR, FRK)
    return bomb

def parseModule(bomb):
    funcToCall = input("Which module would you like to solve? (type "
                       "\"help\" for options): ").lower().replace(' ', '')
    if funcToCall in ["simplewires", "simple"]:
        simpleWires(bomb)
    elif funcToCall == "button":
        button(bomb)
    elif funcToCall in ["wof", "whosonfirst", "who'sonfirst"]:
        whosOnFirst()
    elif funcToCall in ["comp", "complicated", "complicatedwires"]:
        complicatedWires(bomb)
    elif funcToCall in ["password", "pass"]:
        password()
    elif funcToCall in ["maze", "mazes"]:
        maze()
    elif funcToCall in ["help", "h", "-h", "--help"]:
        help()
    elif funcToCall in ["exit", "quit"]:
        print("\nWe hope your defusal was a success. Come again soon!\n")
        break
    else:
        print("Please try again")

def help():
    print("HELP!")


def main():
    """ Creats the bomb object with the relevant info, then calls the
        desired function based on user input """

    logo = ("\n"
            " _   _______ ___   _   _  _____ \n"
            "| | / /_   _/ _ \ | \ | ||  ___|\n"
            "| |/ /  | |/ /_\ \|  \| || |__  \n"
            "|    \  | ||  _  || . ` ||  __| \n"
            "| |\  \ | || | | || |\  || |___ \n"
            "\_| \_/ \_/\_| |_/\_| \_/\____/ \n"
            "                                \n"
            "                                \n"
            " _____       _                  \n"
            "/  ___|     | |                 \n"
            "\ `--.  ___ | |_   _____ _ __   \n"
            " `--. \/ _ \| \ \ / / _ \ '__|  \n"
            "/\__/ / (_) | |\ V /  __/ |     \n"
            "\____/ \___/|_| \_/ \___|_|     \n")

    print(logo)
    print("Welcome to the KTANE solver!")
    print("We hope you have a successful defusal, with minimal death.\n")
    print("\nYou may configure your bomb now if you wish.")
    print("If you do not, we may ask for additional information later")

    # Do-while for input
    while True:
        user_input = input("Do you wish to configure your bomb now "
                           "(recommended)? (Y/n) ").upper()
        if user_input == "" or user_input[0] == "Y":
            bomb = setupBomb()
            break
        elif user_input[0] == "N":
            bomb = Bomb()
            break
        print("Please select a valid option")

    # Now, we ask the user to supply the name of the module they want to solve

    while True:
        parseModule(bomb)


if __name__ == "__main__":
    main()
