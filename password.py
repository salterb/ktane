from colours import bold
from utils import get_input

def get_password_input():
    while True:
        letters = get_input(f"Input the letters in position {letter_pos+1}: ")
        if letters in ("EXIT", "QUIT"):
            return None

        if letters.isalpha() and len(letters) <= 6:
            return letters

        print("Invalid letter sequence. Try again")

class Password:
    VALID_PASSWORDS = ["ABOUT", "AFTER", "AGAIN", "BELOW", "COULD",
                       "EVERY", "FIRST", "FOUND", "GREAT", "HOUSE",
                       "LARGE", "LEARN", "NEVER", "OTHER", "PLACE",
                       "PLANT", "POINT", "RIGHT", "SMALL", "SOUND",
                       "SPELL", "STILL", "STUDY", "THEIR", "THERE",
                       "THESE", "THING", "THINK", "THREE", "WATER",
                       "WHERE", "WHICH", "WORLD", "WOULD", "WRITE"]
    def solve(self):
        """Solves the password module."""
        letter_pos = 0
        valid_passwords = self.VALID_PASSWORDS[:]
        while len(valid_passwords) > 1:
            letters = get_password_input()
            if letters is None:  # "EXIT" or "QUIT"
                return
            letters = list(letters)
            valid_passwords_iter = valid_passwords[:]
            # We use the "master" copy of the password list so we can
            # remove items from the copy whilst still correctly iterating
            for word in valid_passwords_iter:
                if word[letter_pos] not in letters:
                    valid_passwords.remove(word)
            letter_pos += 1

        # Now there is at most one word in the list. If there's none, the user
        # made an error and we tell them to try again
        if len(valid_passwords) == 0:
            print("Invalid input letters")
        else:
            print(f"\nThe password is {bold(valid_passwords[0])}\n")
