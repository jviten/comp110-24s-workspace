"""List Utility Functions."""

__author__: str = "730677545"


def all(same: list[int], given_num: int) -> bool:
    """See if every element in the list is the same."""
    if len(same) == 0:
        return False
    for number in same:
        if number == given_num:
            return True
        else:
            return False


def max(largest: list[int]) -> int:
    """Find the maximum."""
    if len(largest) == 0:
        raise ValueError("max() arg is and empty List")
    biggest_number: int = largest[0]
    for numbers in largest:
        if numbers > biggest_number:
            biggest_number = numbers
    return biggest_number


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """See if all the elements are the same."""
    if len(input1) == 0 or len(input2) == 0:
        return False
    if len(input1)!= len(input2):
        return False
    for elem1 in input1:
        for elem2 in input2:
            if elem1 == elem2:
                return True
            else:
                return False


def extend(input1: list[int], input2: list[int]) -> None:
    """Add input2 to the end of input1."""
    for input2_nums in input2:
        input1.append(input2_nums)     