"""Recursion Functions."""

author = "730677545"


def f(n: int, k: int) -> int:
    """Recursively defining n*k function."""
    if n == 0:
        return 0
    else:
        return n * k
    