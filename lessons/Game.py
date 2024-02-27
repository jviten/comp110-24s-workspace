"""Number guessing game"""

from random import randint

SECRET: int = randint(1,10)
correct: bool = False
while correct == False:
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right {guess} is the secret number")
        correct = True
    else: 
        print ("Wrong number dickhead")
    if guess <= 0:
        print ("Too low asshole.")
    if guess >= 11:
        print ("Too high cocksucker")
    


