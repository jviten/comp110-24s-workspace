"""Splitting a dictionary into two lists."""

__author__: str = "730677545"


#def get_keys(input1: dict[str, int]) -> list[str]:
 #   """Get the keys and turn it into list."""
  #  keylist: list[str] = []
   # if len(input1) == 0:
    #    return keylist
   # for keys in input1:
    #    keylist.append(keys)
    #return keylist


def get_values(dictionary: dict[str, int]) -> list[int]:
    """Get the values from a dict and put it in a list."""
    val_list: list[int] = []
    if len(dictionary) == 0:
        return val_list
    for keys in dictionary:
        val_list.append(dictionary[keys])
    return val_list
