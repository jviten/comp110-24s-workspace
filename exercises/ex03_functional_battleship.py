"""Functional Battleship."""

__author__: str = "730677545"
import random


def input_guess(grid_size: int, row_column_str: str) -> int:
    """Promts user for guess."""
    assert row_column_str == "row" or row_column_str == "column"
    if row_column_str == "row":
        row_guess: int = int(input("Guess a row: "))
        while int(row_guess) >= int(grid_size + 1) or int(row_guess) <= 0:
            row_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        return int(row_guess)
    if row_column_str == "column":
        column_guess: int = int(input("Guess a column: "))
        while int(column_guess) >= int(grid_size + 1) or int(column_guess) <= 0:
            column_guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
        return int(column_guess)


def print_grid(grid_size: int, row_guess: int, column_guess: int, correctness: bool) -> None:
    """Print the Grid with red or white boxes."""
    BLUE_BOX: str = "\U0001F7E6"
    RED_BOX: str = "\U0001F7E5"
    WHITE_BOX: str = "\U00002B1C"

    row_counter: int = 1
    while row_counter <= grid_size:
        row_str: str = ""
        column_counter: int = 1
        while column_counter <= grid_size:
            if row_counter == row_guess and column_counter == column_guess:
                if correctness is True:
                    row_str += RED_BOX
                else:
                    row_str += WHITE_BOX
            else:
                row_str += BLUE_BOX
            column_counter += 1
        print(row_str)
        row_counter += 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """Defining correct guess."""
    return secret_row == row_guess and secret_column == column_guess


def main(grid_size: int, secret_row: int, secret_colum: int) -> None:
    """The actual function that combines past functions."""
    player_turn: int = 1

    while player_turn <= 5:
        print(f"=== Turn {player_turn}/5 ===")
        row_guess: int = input_guess(grid_size, "row")
        column_guess: int = input_guess(grid_size, "column")
        correctness: bool = correct_guess(secret_row, secret_colum, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, correctness)
        if correctness is True:
            print(f"Hit! You won in {player_turn}/5 turns!")
            exit()
        else:
            print("Miss!")
            player_turn += 1
    print("x/5 - Better luck next time")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))