"""Summing the elements of a list using different loops."""

__author__: str = "730677545"


def w_sum(vals: list[float]) -> float:
    """While loop function."""
    idx: int = 0
    sum: float = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """For loop function."""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """For in loop function with ranges."""
    sum: float = 0.0
    for idx in range(0, len(vals)):
        sum += vals[idx]
    return sum