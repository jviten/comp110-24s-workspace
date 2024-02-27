"""Demonstrate Basic List Syntax"""

#Initialize an empty list

grocery_list: list[str] = list() #<- list constructor

print(grocery_list)

#.append adds an item to the list
grocery_list.append("bananas")
print(grocery_list)

# Create already populated list

grocery_list: list[str] = ["bananas", "milk", "bread"]

# Indexing
print("first element of string")
print(grocery_list[0])

#modiying by index
print("Before Change: ")
grocery_list[1] = "almond milk"
#after change
print(grocery_list)

# Measuring list
print(len(grocery_list))

#Function Name: Display
#parameter: list[str]
# Return nothing, print the list out

def display(the_list: list[str]):
    print(the_list)

display(["this is", "said list", "bozo"])

#create a list
#name: create
#parameters: str and str
# RV: list[str]
# Put both parameters into list and return that list

def create(one_str: str, two_str: str) -> list[str]:
    my_list: list[str] = [one_str, two_str]
    return my_list

print(create("hello", "world"))