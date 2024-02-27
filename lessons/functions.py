"""Example functions to learn definition and calling syntax"""

def my_max(num1: int, num2: int) -> int:
    """Returns max value out of both numbers"""
    if num1 >= num2:
        return num1 + 0
    else: #number 1 < number2
        return num2
    
max: int = my_max(1,12)
other_max: int = my_max(13,3)
print(other_max)