"""Mutating functions."""
__author__: str = "730677545"


def manual_append(added: list[int], number: int) -> None:
    """Add an integer to a list."""
    added.append(number)


def double(twice: list[int]) -> None:
    """Double every element in a list."""
    counter: int = 0
    while counter < len(twice):
        twice[counter] *= 2
        counter += 1