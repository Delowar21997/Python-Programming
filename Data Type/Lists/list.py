# Lists define the ordered collection of items in Python.
# They are mutable, meaning their contents can be changed after creation.
# Lists are defined using square brackets [] and can contain items of different data types.
# Example of creating a list
my_list = [1, 2, 3, 'apple', 'banana', 4.5]
print("Original list:", my_list)
# Accessing elements in a list
first_item = my_list[0]  # Accessing the first item
last_item = my_list[-1]  # Accessing the last item
# Modifying elements in a list
my_list[1] = 'orange'  # Changing the second item to 'orange'
# Adding elements to a list
my_list.append('grape')  # Adding 'grape' to the end of the list
my_list.insert(2, 'kiwi')  # Inserting 'kiwi' at index 2
# Removing elements from a list
my_list.remove('apple')  # Removing 'apple' from the list
popped_item = my_list.pop()  # Removing and returning the last item
# Slicing a list
sub_list = my_list[1:4]  # Getting a sub-list from index 1 to 3
# Iterating through a list
for item in my_list:
    print(item)
# Getting the length of a list
list_length = len(my_list)  # Getting the number of items in the list
# Sorting a list
numbers = [4, 2, 9, 1]
numbers.sort()  # Sorting the list in ascending order
# Reversing a list
numbers.reverse()  # Reversing the order of the list
# Copying a list
copied_list = my_list.copy()  # Creating a shallow copy of the list
# Clearing a list
my_list.clear()  # Removing all items from the list
# Printing the final state of the lists
print("Final my_list:", my_list)
print("Final numbers list:", numbers)
