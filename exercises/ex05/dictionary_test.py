"""Testing our dict function."""

import pytest
from exercises.ex05.dictionary import invert, favorite_color, alphabetizer, count, update_attendance

author: str = "730677545"


def test_invert_use_case_normal_use() -> None:
    """Check if the dictionary is inverted when function is called."""
    test_dict: dict[str, str] = {"First": "2", "Second": "3"}
    inverted_dictionary = invert(test_dict)
    assert inverted_dictionary == {"2": "First", "3": "Second"}


def test_invert_use_case_emptystr() -> None:
    """Check if the output still works with an empty value."""
    test_dict: dict[str, str] = {"": "2", "Second": "3"}
    inverted_dictionary = invert(test_dict)
    assert inverted_dictionary == {"2": "", "3": "Second"}


def test_invert_edge_case_duplicates() -> None:
    """See if the dictionary will still be inverted if there are duplicate values."""
    with pytest.raises(KeyError):
        test_dict: dict[str, str] = {"First": "3", "Second": "3"}
        invert(test_dict)
    assert TypeError
         

def test_favorite_color_use_case() -> None:
    """Test to see if the desired output is returned when normal input is given."""
    test_color_dict: dict[str, str] = {"Victor": "green", "Lily": "green", "Kris": "blue"}
    favorite_color_str: str = favorite_color(test_color_dict)
    assert favorite_color_str == "green"


def test_favorite_color_use_case_capitalization() -> None:
    """Test to see if the desired output is returned when some colors are capitalized."""
    test_color_dict: dict[str, str] = {"Victor": "Green", "Lily": "green", "Kris": "Blue"}
    favorite_color_str: str = favorite_color(test_color_dict)
    assert favorite_color_str == "Green"


def test_favorite_color_edge_case() -> None:
    """Check if favorite color will still be returned if other dicts are empty."""
    test_color_dict: dict[str, str] = {"Victor": "green", "Lily": "green", "Kris": ""}
    favorite_color_str = favorite_color(test_color_dict)
    assert favorite_color_str == "green"


def test_count_use_case_functionality() -> None:
    """Check to see if the function will count the strings correctly."""
    test_dict: list[str] = ["Ipad", "Iphone", "Ipad", "Computer", "Iphone"]
    return_dict = count(test_dict)
    assert return_dict == {"Ipad": 2, "Iphone": 2, "Computer": 1}


def test_count_use_case_capitalization() -> None:
    """Check to see if the function will seperately count str with same spelling but different capitalization."""
    test_dict: list[str] = ["ipad", "Iphone", "Ipad", "computer", "Iphone"]
    return_dict = count(test_dict)
    assert return_dict == {"ipad": 1, "Iphone": 2, "Ipad": 1, "computer": 1}


def test_count_edge_case() -> None:
    """Check to see if the function will work with empty lists."""
    test_dict: list[str] = ["", "Iphone", "Ipad", "Computer", "Iphone", ""]
    return_dict = count(test_dict)
    assert return_dict == {"": 2, "Iphone": 2, "Ipad": 1, "Computer": 1}


def test_alphabetizer_use_case_functionality() -> None:
    """Check if desired output is returned when intended input is given."""
    test_list: list[str] = ["book", "sky", "backpack", "water", "slight"]
    return_dict = alphabetizer(test_list)
    assert return_dict == {"b": ["book", "backpack"], "s": ["sky", "slight"], "w": ["water"]}


def test_alphabetizer_use_case_capitalization() -> None:
    """Check if function still counts string in same letter list even if strings are capitalized and not capitalized."""
    test_list: list[str] = ["Book", "sky", "backpack", "Water", "Slight"]
    return_dict = alphabetizer(test_list)
    assert return_dict == {"b": ["Book", "backpack"], "s": ["sky", "Slight"], "w": ["Water"]}


def test_alphabetizer_edge_case_symbols() -> None:
    """Check if function still works if symbols are in the list instead of letters."""
    test_list: list[str] = ["Book", "sky", "+", "Water", "Slight"]
    return_dict = alphabetizer(test_list)
    assert return_dict == {"b": ["Book"], "s": ["sky", "Slight"], "+": ["+"],"w": ["Water"]}


def test_update_attendance_use_case_functionality() -> None:
    """Test if functionality gives desired output with intended input."""
    test_log: dict = {"Monday": ["Julian"], "Tuesday": ["Odell"]}
    update_attendance(test_log, "Monday", "OC")
    assert test_log == {"Monday": ["Julian", "OC"], "Tuesday": ["Odell"]}


def test_update_attendance_use_case_alternate_input() -> None:
    """Test if functionality gives desired output with str numbers as input."""
    test_log: dict = {"Monday": ["74 customers"], "Tuesday": ["24 customers"]}
    update_attendance(test_log, "Monday", "5 employees")
    update_attendance(test_log, "Tuesday", "2 employees")
    assert test_log == {"Monday": ["74 customers", "5 employees"], "Tuesday": ["24 customers", "2 employees"]}


def test_update_attendance_edge_case_() -> None:
    """Test if functionality gives desired output with empty values."""
    test_log: dict = {"Monday": ["Julian"], "Tuesday": ["Odell"]}
    update_attendance(test_log, "Monday", "")
    assert test_log == {"Monday": ["Julian", ""], "Tuesday": ["Odell"]}
