#!/usr/bin/env python3
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



def isValidSimpleWires(wires):
    """ Helper function to determine if the wire arrangement specified
    is valid """
    if len(wires) < 3 or len(wires) > 6:
        return False
    for chr in wires:
        if chr not in ['K','B','Y','R','W']:
            return False
    return True

def simpleWires(bomb):
    """ Solve the simple wires module on the bomb"""
    
    # Use a "do-while" to get the wire sequence
    while True:
        wires = input("Please input the wire sequence (no spaces) ")
        if isValidSimpleWires(wires):
            break
        print("Invalid wire sequence")

    numWires = len(wires)
    if numWires == 3:
        if 'R' in wires:
            print("Cut the --- SECOND --- wire")
        elif wires[-1] == 'W':
            print("Cut the --- LAST --- wire")
        elif wires.count('B') > 1:
            print("Cut the --- LAST BLUE --- wire")
        else:
            print("Cut the --- LAST --- wire")

    elif numWires == 4:
        if wires.count("R") > 1 and bomb.serial[-1] % 2 == 1:
            print("Cut the --- LAST RED --- wire")
        elif wires[-1] == 'Y' and ('R' not in wires):
            print("Cut the --- FIRST --- wire")
        elif wires.count('B') == 1:
            print("Cut the --- FIRST --- wire")
        elif wires.count('Y') > 1:
            print("Cut the --- LAST --- wire")
        else:
            print("Cut the --- SECOND --- wire")

    elif numWires == 5:
        if wires[-1] == 'K' and bomb.serial[-1] % 2 == 1:
            print("Cut the --- FOURTH --- wire")
        elif wires.count('R') == 1 and wires.count('Y') > 1:
            print("Cut the --- FIRST --- wire")
        elif 'K' not in wires:
            print("Cut the --- SECOND --- wire")
        else:
            print("Cut the --- FIRST --- wire")

    elif numWires == 6:
        if 'Y' not in wires and bomb.serial[-1] % 2 == 1:
            print("Cut the --- THIRD --- wire")
        elif wires.count('Y') == 1 and wires.count('W') > 1:
            print("Cut the --- FOURTH --- wire")
        elif 'R' not in wires:
            print("Cut the --- LAST --- wire")
        else:
            print("Cut the --- FOURTH --- wire")
    
    else:
        raise Exception("len(numWires = "+str(len(numWires))+
                        " - this is apparently not good!")

def button(bomb):
    """ Solves the button module on the bomb """

    # Two do-while loops to get the button color and word
    validColours = ['R','B','Y','W']
    while True:
        buttonColour = input("Please input the button colour ")
        if buttonColour in validColours:
            break
        print("Please supply a valid colour from [R, B, Y, W]")

    buttonWord = ""
    validWords = ['A','D','H','P']
    while buttonWord not in validWords:
        buttonWord = input("Please input first letter of word on button ")
        if buttonWord not in validWords:
            print("Please supply a valid letter from [A, D, H, P]")
    releaseString = ("------ DO NOT IMMEDIATELY RELEASE THE BUTTON ------\n\n"
                     "If the strip is BLUE, release the button when timer "
                     "has a 4 in any position\n"
                     "If the strip is YELLOW, release the button when timer "
                     "has a 5 in any position\n"
                     "Otherwise release the button when timer "
                     "has a 1 in any position")
                     
    if buttonColour == 'B' and buttonWord == 'A':
        print("Hold button")
        print(releaseString)
    elif bomb.numBatteries > 1 and buttonWord == 'D':
        print("Press and release button")
    elif buttonColour == 'W' and bomb.CAR == True:
        print("Hold button")
        print(releaseString)
    elif bomb.numBatteries > 2 and bomb.CAR == True:
        print("Press and release button")
    elif buttonColor == 'Y':
        print("Hold button")
        print(releaseString)
    elif buttonColor == 'R' and buttonWord == 'H':
        print("Press and release button")
    else:
        print("Hold button")
        print(releaseString)

def keypad():
    """ TO DO """
    pass

def simon(bomb):
    """ TO DO """
    pass

def whosOnFirst():
    """ TO DO """
    pass

def memory():
    """ TO DO """
    pass

def morse():
    """ TO DO - allow for passing of partial string? """
    pass

def complicatedWires(bomb):
    """ TO DO - pass one wire at a time? """
    pass

def sequences():
    """ TO DO """
    pass

def maze():
    """ TO DO """
    pass

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
        # Do-while for input
        while (True):
            letters = input("Please input the list of letters in position "
                            +str(letterPos+1)+": ").strip().upper()
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
        letterPos+=1
    
    # Now there is at most one word in the list. If there's none, the user
    # made an error and we tell them to try again
    if len(validPasswords) == 0:
        print("Invalid input letters. Please run module again")
    else:
        print("The password is "+validPasswords[0])

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
    print("\nFirst, we need to get some info about your bomb\n")
    
    # Set up the bomb with a bunch of user input
    while True:
        serial = input("Please input the bomb's serial number: ").upper()
        if serial.isalnum() and len(serial) == 6:
            break
        print("Invalid serial number. Please try again using only 6 "
              "alphanumeric characters")

    while True:
        numBatteries = input("Please input the number of batteries "
                             "on the bomb: ")
        if numBatteries.isdigit():
            break
        print("Invalid number of batteries. Please try again")

    while True:
        parallelPort = input("Does the bomb have a parallel port? (Y/N) ")
        if len(parallelPort) > 0 and parallelPort[0] in ['y','Y','n','N']:
            break
        print("Invalid input. Please try again")

    while True:
        CAR = input("Is there a lit indicator with label \"CAR\"? (Y/N) ")
        if len(CAR) > 0 and CAR[0] in ['y','Y','n','N']:
            break
        print("Invalid input. Please try again")

    while True:
        FRK = input("Is there a lit indicator with label \"FRK\"? (Y/N) ")
        if len(FRK) > 0 and FRK[0] in ['y','Y','n','N']:
            break
        print("Invalid input. Please try again")
    
    # The bomb object with all relevant extraneous info from the bomb
    bomb = Bomb(serial, numBatteries, parallelPort, CAR, FRK)
    
    # Now, we ask the user to supply the name of the module they want to solve
    
    while (True):
        funcToCall = input("Which module would you like to solve? "
                           "(type \"help\" for options) ").lower()
        if funcToCall == "password":
            password()
        if funcToCall in ["exit", "quit"]:
            print("\nWe hope your defusal was a success. Come again soon!\n")
            break 

if __name__ == "__main__":
    main()