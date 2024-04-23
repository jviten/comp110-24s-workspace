"""Ex05 exercise."""

__author__: str = "730677545"


def invert(input1: dict[str, str]) -> dict[str, str]:
    """Inverts dict."""
    output_dict = {}
    empty_list: list[str] = []
    for input1_keys in input1:
        value = input1[input1_keys]
        for elem in empty_list:
            if value == elem:
                raise KeyError("Error, duplicate value in key!")
        empty_list.append(value)
        output_dict[value] = input1_keys
    return output_dict
    

def favorite_color(colors: dict[str, str]) -> str:
    """Finds the most popular color from a dictionary."""
    color_dict: dict[str, int] = {}
    for elem in colors:
        color = colors[elem]
        if color in color_dict:
            color_dict[color] += 1
        else:
            color_dict[color] = 1
    max: int = 0
    color_max: str = ""
    for component in color_dict:
        if color_dict[component] > max:
            max = color_dict[component]
            color_max = component
    return color_max


def count(given_list: list[str]) -> dict[str, int]:
    """Counts elements and returns number of times it shows up."""
    return_dict: dict[str, int] = {}
    for elem in given_list:
        if elem in return_dict:
            return_dict[elem] += 1
        else:
            return_dict[elem] = 1
    return return_dict


def alphabetizer(given_list: list[str]) -> dict[str, list[str]]:
    """Returns dict that has first letter of word and all the words that start with that letter."""
    return_dict: dict[str, list[str]] = {}
    for word in given_list:
        lowercased_word = word.lower()
        key_letter = lowercased_word[0]
        if key_letter not in return_dict:
            return_dict[key_letter] = []
        return_dict[key_letter].append(word)
    return return_dict


def update_attendance(log: dict[str, list[str]], day: str, attended: str) -> None:
    """Updates log of attendance with days and names."""
    if day in log:
        log[day].append(attended)
    else:
        log[day] = [attended]
