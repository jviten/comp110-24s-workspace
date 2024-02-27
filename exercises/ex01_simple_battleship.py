"""Simple Battleship excercise."""
__author__: str = "730677545"

P1_guess: int = int(input("Pick a secret boat location between 1 and 4: "))


if (P1_guess < 1):
    print(f"Error! {P1_guess} too low!")
    exit()
if (P1_guess > 4):
    print(f"Error! {P1_guess}  too high!")
    exit()


P2_guess: int = int(input("Guess a number between 1 and 4: "))


if (P2_guess < 1):
    print(f"Error! {P2_guess} too low!")
    exit()
if (P2_guess > 4):
    print(f"Error! {P2_guess}  too high!")
    exit()


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


if P1_guess == P2_guess:
    if P1_guess == 1:
        print(f"{RED_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
    if P1_guess == 2:
        print(f"{BLUE_BOX}{RED_BOX}{BLUE_BOX}{BLUE_BOX}")
    if P1_guess == 3:
        print(f"{BLUE_BOX}{BLUE_BOX}{RED_BOX}{BLUE_BOX}")
    if P1_guess == 4:
        print(f"{BLUE_BOX}{BLUE_BOX}{RED_BOX}{BLUE_BOX}")
    print("Correct! You hit the ship.")
else:  
    if P2_guess == 1:
        print(f"{WHITE_BOX}{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}")
    if P2_guess == 2:
        print(f"{BLUE_BOX}{WHITE_BOX}{BLUE_BOX}{BLUE_BOX}")
    if P2_guess == 3:
        print(f"{BLUE_BOX}{BLUE_BOX}{WHITE_BOX}{BLUE_BOX}")
    if P2_guess == 4:
        print(f"{BLUE_BOX}{BLUE_BOX}{BLUE_BOX}{WHITE_BOX}")
    print("Incorrect! You missed the ship.")