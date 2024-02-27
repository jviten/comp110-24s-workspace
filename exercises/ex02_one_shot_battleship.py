"""One Shot Battleship EX02."""

__author__: str = "730677545"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


row_guess: int = int(input("Guess a row: "))

while 1 > row_guess or row_guess > 4: 
    row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

column_guess: int = int(input("Guess a column: "))

while 1 > column_guess or column_guess > 4:
    column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

row_counter: int = 1

while row_counter <= grid_size:
    row_str: str = "" 
    column_counter: int = 1
    while column_counter <= grid_size:  
        if row_counter == row_guess and column_counter == column_guess:
            if row_counter == secret_row and column_counter == secret_column:
                row_str += RED_BOX
            else:
                row_str += WHITE_BOX
        else: 
            row_str += BLUE_BOX
        column_counter += 1
    print(row_str)
    row_counter += 1 

if row_guess == secret_row and column_guess != secret_column:
    print("Close! Correct row, wrong column.")
elif row_guess != secret_row and column_guess == secret_column:
    print("Close! Correct column, wrong row.")
elif column_guess == secret_column and row_guess == secret_row:
    print("Hit!")
else:
    print("Miss!")