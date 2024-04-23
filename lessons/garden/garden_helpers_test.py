"""Test my garden functions."""

__author__: str = "730677545"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_use_case() -> None:
    """Test if item is added in the correct place."""
    tester_list1: dict[str, list[str]] = {"Red": ["Rose", "Poppy"], "Yellow": ["Sunflower, Daisy"]}
    add_by_kind(tester_list1, "Blue", "Salvia")
    assert tester_list1 == {"Red": ["Rose", "Poppy"], "Yellow": ["Sunflower, Daisy"], "Blue": ["Salvia"]}


def test_add_by_kind_edge_case() -> None:
    """Test if an error will be raised if types are incorrect."""
    tester_list2: dict[str, list[str]] = {"Red": ["Rose", "Poppy"], "Yellow": ["Sunflower, Daisy"]}
    add_by_kind(tester_list2, "Blue", 6)
    assert TypeError


def test_add_by_date_use_case() -> None:
    """Test if plant is put in the correct place."""
    tester_list3: dict[str, list[str]] = {"June": ["Rose", "Poppy"], "July": ["Sunflower, Daisy"]}
    add_by_date(tester_list3, "August", "Cornflower")
    assert tester_list3 == {"June": ["Rose", "Poppy"], "July": ["Sunflower, Daisy"], "August": ["Cornflower"]}


def test_add_by_date_edge_case() -> None:
    """Test if the function will raise an error if the incorrect type is given."""
    tester_list4: dict[str, list[str]] = {"June": ["Rose", "Poppy"], "July": ["Sunflower", "Daisy"]}
    add_by_date(tester_list4, "July", 6)
    assert TypeError


def test_lookup_by_kind_and_date_use_case() -> None:
    """Check if the correct output is given."""
    plants_by_kind_dict: dict[str, list[str]] = {"Red": ["Rose", "Poppy"], "Yellow": ["Sunflower", "Daisy"]}
    plants_by_date_dict: dict[str, list[str]] = {"June": ["Rose", "Poppy"], "July": ["Sunflower", "Daisy"]}
    ret_value: str = lookup_by_kind_and_date(plants_by_kind_dict, plants_by_date_dict, "Red", "June")
    assert ret_value == "Reds to plant in June: ['Rose', 'Poppy']"


def test_lookup_kind_and_date_edge_case() -> None:
    """Check if an error will arise if the month is incorrect."""
    plants_by_kind_dict: dict[str, list[str]] = {"Red": ["Rose", "Poppy"], "Yellow": ["Sunflower", "Daisy"]}
    plants_by_date_dict: dict[str, list[str]] = {"June": ["Rose", "Poppy"], "July": ["Sunflower", "Daisy"]}
    lookup_by_kind_and_date(plants_by_kind_dict, plants_by_date_dict, "Red", "June")
    assert AssertionError
