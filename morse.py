"""Morse

The Morse module consists of a flashing light that repeats a word in
Morse code, and a display to set a frequency.
"""

from colours import bold
from utils import get_input

class Morse:
    """Class to represent the Morse module. Solving requires getting
    the Morse characters appearing on the light to decode the Morse into
    a word. Each word has a corresponing frequency, which must be
    inputted and transmitted.
    """
    VALID_WORDS = {"SHELL":  3.505,
                   "HALLS":  3.515,
                   "SLICK":  3.522,
                   "TRICK":  3.532,
                   "BOXES":  3.535,
                   "LEAKS":  3.542,
                   "STROBE": 3.545,
                   "BISTRO": 3.552,
                   "FLICK":  3.555,
                   "BOMBS":  3.565,
                   "BREAK":  3.572,
                   "BRICK":  3.575,
                   "STEAK":  3.582,
                   "STING":  3.592,
                   "VECTOR": 3.595,
                   "BEATS":  3.600}
    MORSE_LETTERS = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
                     ".": "E", "..-.": "F", "--.": "G", "....": "H",
                     "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
                     "--": "M", "-.": "N", "---": "O", ".--.": "P",
                     "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
                     "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
                     "-.--": "Y", "--..": "Z"}

    def get_morse_input(self):
        """Prompt a user to input a single Morse code letter, and return
        a single character representing that letter.
        """
        while True:
            morse_sequence = get_input("Input a morse code letter (. = dot, - = dash): ")
            if morse_sequence in ("EXIT", "QUIT"):
                return None

            try:
                return self.MORSE_LETTERS[morse_sequence]
            except KeyError:
                print("Invalid morse sequence. Please try again")

    def solve(self):
        """Solves the Morse module."""
        # Make a copy to remove words from when ruled out.
        valid_words = dict(self.VALID_WORDS)
        while len(valid_words) > 1:
            morse_character = self.get_morse_input()
            if morse_character is None:  # "EXIT" or "QUIT"
                return

            # Make a copy to iterate over, since we modify valid_words
            valid_words_iter = dict(valid_words)
            for word in valid_words_iter:
                if morse_character not in word:
                    del valid_words[word]

        # Now we have at most one valid word
        if len(valid_words) == 0:
            print("Morse inputs do not match any known word. Please run module again.")
        else:
            word, freq = valid_words.popitem()
            print(f"\nThe word is {word}")
            freq_str = f"{freq:.3f}"  # Pad with zeroes
            print(f"The frequency is {bold(freq_str)} MHz\n")
