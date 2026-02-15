my_fruits = ["apple", "banana", "fig", "grape"]
# Copying the list using slicing
friend_fruits = my_fruits[:]
print("My fruits:", my_fruits)
print("Friend's fruits:", friend_fruits)
# Modifying the original list to show that the friend's list is a separate copy
my_fruits.append("date")
# Modifying the friend's list to show that it is a separate copy
friend_fruits.append("cherry")
print("My fruits after modification:", my_fruits)
print("Friend's fruits after modification:", friend_fruits)
# Print the friend's fruits in reverse order
print("Friend's fruits:", friend_fruits[::-1])

print("\n--- Copying the list using assignment operator ---\n")

#This does not work while copying the list using assignment operator
my_numbers = [1, 2, 3, 4, 5]
friend_numbers = my_numbers  # This creates a reference, not a copy
print("My numbers:", my_numbers)
print("Friend's numbers:", friend_numbers)
# Modifying the original list will affect the friend's list
my_numbers.append(6)
friend_numbers.append(7)  # This will also modify my_numbers since it's the same list
print("My numbers after modification:", my_numbers)
print("Friend's numbers after modification:", friend_numbers)  # This will also show the change 