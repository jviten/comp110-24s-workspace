"""Functions that implement sorting algorithms."""

__author__ = "739677545"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    counter = len(x)
    for sorted in range(1, counter): #Idxs 1->len(x) skip 0
        current_element = x[sorted]
        initial = sorted
        while initial > 0 and x[initial - 1] > current_element:
            x[initial] = x[initial - 1]
            initial -= 1
        x[initial] = current_element
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    min_counter = len(x)
    for elem in range(min_counter):
        min_idx = elem
        for counter in range(elem + 1, min_counter):
            if x[counter] < x[min_idx]:
                min_idx = counter
        
        x[elem], x[min_idx] = x[min_idx], x[elem]
    return None