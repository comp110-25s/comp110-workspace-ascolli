"""Making a game of wordle!"""

__author__: str = "730564797"


def contains_char(longstring: str, singlestring: str) -> bool:
    """Is the charachter in the word?"""
    assert len(singlestring) == 1, f"len('{singlestring}') is not 1"
    idx: int = 0
    while idx < len(longstring):
        if singlestring == longstring[idx]:
            return True
        else:
            idx += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret2: str) -> str:
    """Emoji-fies the Wordle Game!"""
    assert len(guess) == len(secret2), "Guess must be same length as secret"
    idx: int = 0
    baseline: str = ""
    while idx < len(guess):
        if guess[idx] == secret2[idx]:
            baseline += GREEN_BOX
        elif contains_char(longstring=secret2, singlestring=guess[idx]):
            baseline += YELLOW_BOX
        else:
            baseline += WHITE_BOX
        idx += 1
    return baseline


def input_guess(exp: int) -> str:
    """Asks the user for the length of the word!"""
    guess2 = input(f"Enter a {(exp)} character word:")
    while len(guess2) != exp:
        guess2 = input(f"That wasn't {exp} chars! Try again:")
    return guess2


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop:)"""
    TURN: int = 1
    """^^^Keeps track of amount of turns user has used"""
    DIDYOUWIN: int = 0
    while TURN <= 6 and DIDYOUWIN <= 0:
        print(f"=== Turn {TURN}/6 ===")
        """Emojified input is return-value from input_guess"""
        guess = input_guess(exp=len(secret))
        print(emojified(guess, secret2=secret))
        TURN += 1
        """The following if statement keeps track of whether or not game is won. If won, breaks while loop"""
        if guess == secret:
            DIDYOUWIN += 1
    if TURN >= 6:
        print(f"X/6 - Sorry, try again tomorrow!")
    else:
        print(f"You won in {TURN-1}/6 turns!")
    if __name__ == "__main__":
        main(secret="codes")
