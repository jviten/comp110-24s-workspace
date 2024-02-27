"""Practice with Dictionaries."""

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
ice_cream["mint"] = 3
ice_cream.pop("vanilla")
print(ice_cream)

#Accessing
print(f"The number of mint orders is {ice_cream['mint']}")

ice_cream["strawberry"] += 3
print (f"The new amount of strawberry orders is {ice_cream['strawberry']}")

#checking if something is in the dictionary
print("mint" in ice_cream)