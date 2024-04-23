"""Creating a funct for quiz 3."""




"""short words function"""
def short_words(the_word: list[str]) -> list[str]:
    """returns a list of words that are shorter than 5 charecters."""
    return_list: list[str] = []
    for elem in the_word:
        if len(elem) < 5:
            return_list.append(elem)
        else:
            print(f"{elem} is too long!")
    return return_list

my_list: list[str] = ("I swear", "to", "Fucking", "god", "I'll", "turn", "this", "Car", "around you fuckface")
print(short_words(my_list))