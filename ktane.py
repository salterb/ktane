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
        self.strikes = 0


# ---------------------------------------------------------- #
#                                                            #
#                       BOMB CONFIG                          #
#                                                            #
# ---------------------------------------------------------- #

def setupBomb():
    """ Sets up the bomb with a bunch of user input """
    serial = addSerial()
    numBatteries = addBatteries()
    parallelPort = addPPort()
    CAR = addCAR()
    FRK = addFRK()
    bomb = Bomb(serial, numBatteries, parallelPort, CAR, FRK)
    return bomb


def configBomb(bomb):
    """ Allows later configuration of the bomb in the event of incorrect
        initial input"""
    bomb.serial = addSerial()
    bomb.numBatteries = addBatteries()
    bomb.parallelPort = addPPort()
    bomb.CAR = addCAR()
    bomb.FRK = addFRK()


def strike(bomb):
    """ Adds a strike to the bomb """
    self.strikes += 1


def resetStrikes(bomb):
    """ Resets strikes in case of incorrect strike input """
    self.strikes = 0


# ---------------------------------------------------------- #
#                                                            #
#                         HELPERS                            #
#                                                            #
# ---------------------------------------------------------- #

# Input validator functions
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


def isValidSimon(string):
    """ Helper function to determine if the Simon light sequence is valid """
    if len(string) == 0:
        return False
    for char in string:
        if char not in ['R', 'B', 'Y', 'G']:
            return False
    return True


# Simon functions
def staticSimon(bomb):
    """ Simply prints out the relevant colour conversion list for Simon """
    if set(['A', 'E', 'I', 'O', 'U']).isdisjoint(set(bomb.serial)):
        if bomb.strikes == 0:
            print("\033[1;31mRED\033[0m    -> \033[1;34mBLUE\033[0m")
            print("\033[1;34mBLUE\033[0m   -> \033[1;33mYELLOW\033[0m")
            print("\033[1;32mGREEN\033[0m  -> \033[1;32mGREEN\033[0m")
            print("\033[1;33mYELLOW\033[0m -> \033[1;31mRED\033[0m")

        elif bomb.strikes == 1:
            print("\033[1;31mRED\033[0m    -> \033[1;31mRED\033[0m")
            print("\033[1;34mBLUE\033[0m   -> \033[1;34mBLUE\033[0m")
            print("\033[1;32mGREEN\033[0m  -> \033[1;33mYELLOW\033[0m")
            print("\033[1;33mYELLOW\033[0m -> \033[1;32mGREEN\033[0m")

        elif bomb.strikes == 2:
            print("\033[1;31mRED\033[0m    -> \033[1;33mYELLOW\033[0m")
            print("\033[1;34mBLUE\033[0m   -> \033[1;32mGREEN\033[0m")
            print("\033[1;32mGREEN\033[0m  -> \033[1;34mBLUE\033[0m")
            print("\033[1;33mYELLOW\033[0m -> \033[1;31mRED\033[0m")
        else:
            raise Exception("Invalid strike number: "+str(bomb.strikes))

    else:
        if bomb.strikes == 0:
            print("\033[1;31mRED\033[0m    -> \033[1;34mBLUE\033[0m")
            print("\033[1;34mBLUE\033[0m   -> \033[1;31mRED\033[0m")
            print("\033[1;32mGREEN\033[0m  -> \033[1;33mYELLOW\033[0m")
            print("\033[1;33mYELLOW\033[0m -> \033[1;32mGREEN\033[0m")
        elif bomb.strikes == 1:
            print("\033[1;31mRED\033[0m     -> \033[1;33mYELLOW\033[0m")
            print("\033[1;34mBLUE\033[0m    -> \033[1;32mGREEN\033[0m")
            print("\033[1;32mGREEN\033[0m   -> \033[1;34mBLUE\033[0m")
            print("\033[1;33mYELLOW\033[0m  -> \033[1;31mRED\033[0m")
        elif bomb.strikes == 2:
            print("\033[1;31mRED\033[0m    -> \033[1;32mGREEN\033[0m")
            print("\033[1;34mBLUE\033[0m   -> \033[1;31mRED\033[0m")
            print("\033[1;32mGREEN\033[0m  -> \033[1;33mYELLOW\033[0m")
            print("\033[1;33mYELLOW\033[0m -> \033[1;34mBLUE\033[0m")
        else:
            print('3 or more strikes. Please run "reset strikes" to try again')


def interactiveSimon(bomb):
    """ Prompts the user for the Simon input, and displays the correct output
    """

    # Repeat the process until the user wants to exit
    while True:
        # Do-while for input
        while True:
            lights = input("Please input the light sequence (type \"exit\" "
                           "to exit): ").upper().replace(' ', '')
            if lights == "EXIT":
                return
            if isValidSimon(lights):
                print("")  # Blank line
                break
            print("Invalid color sequence. Use one letter per colour")

        if set(['A', 'E', 'I', 'O', 'U']).isdisjoint(set(bomb.serial)):
            if bomb.strikes == 0:
                colourDict = {'R': 'B', 'B': 'Y', 'G': 'G', 'Y': 'R'}
            elif bomb.strikes == 1:
                colourDict = {'R': 'R', 'B': 'B', 'G': 'Y', 'Y': 'G'}
            elif bomb.strikes == 2:
                colourDict = {'R': 'Y', 'B': 'G', 'G': 'B', 'Y': 'R'}
            else:
                raise Exception("Invalid strike number: "+str(bomb.strikes))
        else:
            if bomb.strikes == 0:
                colourDict = {'R': 'B', 'B': 'R', 'G': 'Y', 'Y': 'G'}
            elif bomb.strikes == 1:
                colourDict = {'R': 'Y', 'B': 'G', 'G': 'B', 'Y': 'R'}
            elif bomb.strikes == 2:
                colourDict = {'R': 'G', 'B': 'R', 'G': 'Y', 'Y': 'B'}
            else:
                raise Exception("Invalid strike number: "+str(bomb.strikes))

        for char in lights:
            colour = colourDict[char]
            if colour == 'R':
                print("\033[1;31mRED\033[0m")
            elif colour == 'B':
                print("\033[1;34mBLUE\033[0m")
            elif colour == 'G':
                print("\033[1;32mGREEN\033[0m")
            elif colour == 'Y':
                print("\033[1;33mYELLOW\033[0m")
            else:
                raise Exception("Invalid colour: "+colour)
        print("")  # Blank line


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
    """ Solve the simple wires module on the bomb. The user inputs the sequence
        of wires, and the function tells the user which one to cut.
    """

    # Do-while to get the wire sequence
    while True:
        wires = input("Please input the "
                      "wire sequence: ").upper().replace(' ', '')
        if isValidSimpleWires(wires):
            break
        print("Invalid wire sequence. Use one letter per wire (black = 'K')")

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
    print("")  # Blank line


def button(bomb):
    """ Solves the button module on the bomb.
        This function is ugly. We've used 'if's and returns rather than
        'elif's, since we are also providing functionality for users to
        supply the bomb data at the last possible moment, and that involves
        provisionally going inside if statements to provide user input.
    """

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
                     "button when timer has a \033[1m4\033[0m in any "
                     "position\nIf the strip is \033[1;33mYELLOW\033[0m, "
                     "has a \033[1m5\033[0m in any position\nOtherwise "
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

    if (bomb.FRK is not False and
        (bomb.numBatteries is None or bomb.numBatteries > 2)):
        if bomb.numBatteries is None:
            bomb.numBatteries = addBatteries()
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
    """ Solves the "Simon" module, in one of two ways. Either prints out the
        colour map, or enters "interactive mode", where the user inputs a
        color string and we print out the correct sequence of colors to press.
    """
    # Check strike validity
    if bomb.strikes not in [0, 1, 2]:
        print("You have " + str(bomb.strikes) + "strikes. "
              "Please run \"reset strikes\" to try again")
        return

    if bomb.serial is None:
        bomb.serial = addSerial()
    while True:
        user_input = input("Do you want interactive Simon? (Y/n) ").upper()
        if user_input == "" or user_input[0] == "Y":
            interactiveSimon(bomb)
            print("")  # Blank line
            return
        elif user_input[0] == "N":
            staticSimon(bomb)
            print("")  # Blank line
            return
        print("Please select a valid option")


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
    """ Solves the morse module. The user inputs morse characters until
        there is only one valid word left
    """
    validWords = ["SHELL", "HALLS", "SLICK", "TRICK", "BOXES", "LEAKS",
                  "STROBE", "BISTRO", "FLICK", "BOMBS", "BREAK", "BRICK",
                  "STEAK", "STING", "VECTOR", "BEATS"]
    freqs = [3.505, 3.515, 3.522, 3.532, 3.535, 3.542, 3.545, 3.552, 3.555,
             3.565, 3.572, 3.575, 3.582, 3.592, 3.595, 3.600]
    morseFreqs = dict(zip(validWords, freqs))
    morseLetters = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
                        ".": "E", "..-.": "F", "--.": "G", "....": "H",
                        "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
                        "--": "M", "-.": "N", "---": "O", ".--.": "P",
                        "-.--": "Q", ".-.": "R", "...": "S", "-": "T",
                        "..-": "U", "...-": "V", ".--": "W", "-.--": "X",
                        "-.--": "Y", "--..": "Z"}

    while len(validWords) > 1:
        while True:
            morse = input("Please input a morse code letter "
                          "(. = dot, - = dash): ").replace(' ', '').upper()
            if morse == "EXIT" or morse == "QUIT":
                return
            else:
                # Test whether the input has valid morse characters
                validMorse = True
                for char in morse:
                    if char not in ['.', '-']:
                        validMorse = False
                if len(morse) == 0 or len(morse) > 4:
                    validMorse = False
                if validMorse:
                    break

            print("Invalid morse sequence. Please try again")

        validWordsCopy = validWords[:]
        for word in validWordsCopy:
            if morseLetters[morse] not in word:
                validWords.remove(word)

    # Now we have at most one valid word
    if len(validWords) == 0:
        print("Morse inputs do not match any known word. "
              "Please run module again.")
    else:
        print("\nThe word is "+validWords[0])
        freqStr = "{:.3f}".format(morseFreqs[validWords[0]])  # Pad with zeroes
        print("The frequency is \033[1m"
              + freqStr + " MHz\033[0m\n")


def complicatedWires(bomb):
    """ Solves the complicated wires module. The user inputs the wire detail
        one wire at a time, and the function tells the user whether to cut the
        wire or not
    """
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
    """ Calls the external maze solver from a separate module """
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
    while len(validPasswords) > 1:
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


def parseModule(bomb):
    while True:
        funcToCall = input("Which module would you like to solve? (type "
                           "\"help\" for options): ").lower().replace(' ', '')
        if funcToCall in ["simplewires", "simple"]:
            simpleWires(bomb)
        elif funcToCall in ["button"]:
            button(bomb)
        elif funcToCall in ["simon", "simonsays"]:
            simon(bomb)
        elif funcToCall in ["wof", "whosonfirst", "who'sonfirst"]:
            whosOnFirst()
        elif funcToCall in ["comp", "complicated", "complicatedwires"]:
            complicatedWires(bomb)
        elif funcToCall in ["morse"]:
            morse()
        elif funcToCall in ["password", "pass"]:
            password()
        elif funcToCall in ["maze", "mazes"]:
            maze()
        elif funcToCall in ["strike"]:
            strike(bomb)
        elif funcToCall in ["resetstrike", "resetstrikes"]:
            resetStrikes(bomb)
        elif funcToCall in ["config", "conf"]:
            configBomb(bomb)
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

    parseModule(bomb)


if __name__ == "__main__":
    main()
