from codecs import encode

from colours import bold
from utils import get_input

COLUMNS = set([("Q", "AT", "LAMBDA", "N", "CAT", "H", "C"),
               ("EURO", "Q", "C", "PHI", "STAR", "H", "QUESTION"),
               ("C", "OMEGA", "PHI", "K", "3", "LAMBDA", "STAR"),
               ("6", "PARAGRAPH", "TB", "CAT", "K", "QUESTION", "FACE"),
               ("PHI", "FACE", "TB", "C", "PARAGRAPH", "3", "STAR"),
               ("6", "EURO", "NOTEQUAL", "AE", "PSI", "N", "OMEGA")])

def _rot13(string):
    """Enable rot-13 encoding of words so my code doesn't have smutty
    words in it.
    """
    return encode(string, "rot_13")


def symbol_parser():
    """Takes a string, and attempts to parse it to match to one of many
    symbols.
    """
    # TODO there'll be an "official" name for these symbols - we could
    # use those? Or else print them out? Are we supporting terminals
    # that don't support full Unicode?

    while True:
        string = get_input("Input your symbol (either a close letter "
                           "or very short description): ").replace("-", "")
        # The list of valid symbols to return is as follows:
        # Q, AT, LAMBDA, N, CAT, H, C, EURO, PHI, STAR, QUESTION,
        # OMEGA, K, 3, 6, PARAGRAPH, TB, FACE, PSI, NOTEQUAL, AE
        # Note that some symbols overlap, but this isn't a problem as they
        # are all in separate columns
        if string in ("Q", "QOPPA", "KOPPA", "WEIRDQ", "LOLLY", "LOLLIPOP",
                      "LOLLYPOP", "POPSICLE"):
            symbol = "Q"
        elif string in ("AT", "TA", "WEIRDA", "A", "PYRAMID", "LADDER"):
            symbol = "AT"
        elif string in ("LAMBDA", "LAMBDALINE", "WEIRDLAMBDA", "LAMBDAWITHLINE"):
            symbol = "LAMBDA"
        elif string in ("N", "WEIRDN", "BACKWARDSN", "LIGHTNING", "BOLT", "LIGHTNINGBOLT",
                        "THUNDER", "THUNDERBOLT", "NWITHHAT", "NHAT", "NSQUIGGLE", "NBREVE"):
            symbol = "N"
        elif string in ("CAT", "KITTY", "JELLYFISH", "WHAT", "WHAT?", "HWITHTRIANGLE",
                        "HTRIANGLE"):
            symbol = "CAT"
        elif string in ("H", "CURLY H", "CURSIVEH", "GOTHICH", "HWITHTAIL", "HTAIL", "WEIRDH"):
            symbol = "H"
        elif string in ("C", "CWITHDOT", "CDOT", "BACKWARDC", "BACKWARDCDOT", "COPYRIGHT",
                        "CINCIRCLE"):
            symbol = "C"
        elif string in ("EURO", "EUROUMLAUT", "EURODOTS", "E", "EDOTS", "BACKWARDSEURO"):
            symbol = "EURO"
        elif string in ("PHI", "SPRING", "COIL", "CURL", "CURLYQ"):
            symbol = "PHI"
        elif string in ("STAR", "WHITESTAR", "BLACKSTAR", "FILLEDINSTAR"):
            symbol = "STAR"
        elif string in ("QUESTION", "QUESTIONMARK", "UPSIDEDOWNQUESTIONMARK",
                        "UPSIDEDOWNQUESTION", "?"):
            symbol = "QUESTION"

        # ROT-13 encoding here because SOME PEOPLE claim that this
        # symbol resembles various bodily parts, the names of which I
        # don't want in my code. IT'S AN OMEGA, EVERYONE!
        elif string in ("OMEGA", "W", "WEIRDW", _rot13("NFF"), _rot13("OHZ"),
                        _rot13("OHGG"), _rot13("OBBGL"), _rot13("OBBOF"),
                        _rot13("OBBOVRF"), _rot13("GVGF"), _rot13("GVGGVRF"),
                        _rot13("ONYYF"), _rot13("GRFGRF"), _rot13("FPEBGHZ"),
                        _rot13("AHGFNPX"), _rot13("AHGF"), "HEADPHONES"):
            symbol = "OMEGA"
        elif string in ("K", "Ж", "ZHE", "KS", "2K", "2KS", "TWOK", "TWOKS", "WEIRDX",
                        "WEIRDK", "Z", "BACKTOBACKK", "BACKTOBACKKS"):
            symbol = "K"
        elif string in ("3", "WEIRD3", "HALF3", "UNFINISHED3", "THREE", "3WITHTAIL",
                        "3WITHHORNS"):
            symbol = "3"
        elif string in ("6", "SIX", "FLAT6", "FLATSIX", "WEIRD6", "WEIRDSIX", "DELTA",
                        "WEIRDDELTA"):
            symbol = "6"
        elif string in ("PARAGRAPH", "P", "WEIRDP", "BOLDP"):
            symbol = "PARAGRAPH"
        elif string in ("TB", "BT", "DT", "TD", "WEIRDB"):
            symbol = "TB"
        elif string in ("FACE", "SMILE", "SMILEY", "SMILEYFACE", "HAPPY",
                        "HAPPYFACE"):
            symbol = "FACE"
        elif string in ("PSI", "TRIDENT", "FORK", "PITCHFORK"):
            symbol = "PSI"
        elif string in ("NOTEQUAL", "NOTEQUALS", "NOTEQUALSIGN", "HASH", "HASHTAG", "POUND",
                        "POUNDSIGN", "WEIGHT", "WEIGHTS", "DUMBBELL", "WEIRDX", "CROSS"):
            symbol = "NOTEQUAL"
        elif string in ("AE", "Æ", "ASH"):
            symbol = "AE"
        else:
            symbol = None
        return symbol

class Symbol:
    def __init__(self):
        print(f"\n{'-'*20} CAUTION {'-'*20}")
        print("This module is hard for a computer to solve.\n"
              "Please try to describe all symbols using a very short "
              "and obvious description.")
        print(f"{'-'*49}", end="\n\n")

    def solve(self):
        """Solves the symbol keypad."""
        symbols = set()
        while len(symbols) < 4:
            string = symbol_parser()
            if string in symbols:
                print("Symbol already added")
            elif string is None:
                print("Symbol not recognised")
            else:
                symbols.add(string)

        for col in COLUMNS:
            if symbols.issubset(set(col)):
                for item in col:
                    if item in symbols:
                        print(bold(item.capitalize()))
                break
        else:
            print("No valid columns. Did you input the symbols correctly?")
