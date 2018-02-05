# This contains the necessary methods to add detail about the bomb.
# These functions will only return the relevant data - these must be
# added to the bomb manually

def addSerial():
    while True:
        serial = input("Please input the bomb's serial number: ").upper()
        if serial.isalnum() and len(serial) == 6:
            break
        print("Invalid serial number. Please try again using only 6 "
              "alphanumeric characters")
    return serial

def addBatteries():
    while True:
        numBatteries = input("Please input the number of batteries "
                             "on the bomb: ")
        if numBatteries.isdigit():
            break
        print("Invalid number of batteries. Please try again")
    return int(numBatteries)

def addPPort():
    while True:
        parallelPort = input("Does the bomb have a parallel port? "
                             "(Y/N) ").lower()
        if len(parallelPort) > 0 and parallelPort[0] == 'y':
            parallelPort = True
            break
        elif len(parallelPort) > 0 and parallelPort[0] == 'n':
            parallelPort = False
            break
        print("Invalid input. Please try again")
    return parallelPort

def addCAR():
    while True:
        CAR = input("Is there a lit indicator with label "
                    "\"CAR\"? (Y/N) ").lower()
        if len(CAR) > 0 and CAR[0] == "y":
            CAR = True
            break
        elif len(CAR) > 0 and CAR[0] == "n":
            CAR = False
            break
        print("Invalid input. Please try again")
    return CAR
    
def addFRK():
    while True:
        FRK = input("Is there a lit indicator with label "
                    "\"FRK\"? (Y/N) ").lower()
        if len(FRK) > 0 and FRK[0] == "y":
            FRK = True
            break
        elif len(FRK) > 0 and FRK[0] == "n":
            FRK = False
            break
        print("Invalid input. Please try again")
    return FRK
