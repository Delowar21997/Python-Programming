# pop () method removes and returns the last item from the list. 
# It can also remove an item at a specified index.
# We also use remove items anywhere in the list
my_list = ['apple', 'blueberry','date', 'cherry']
empty_popped_list = []
print("Original list:", my_list)
print("My empty popped list is:", empty_popped_list)
empty_popped_list.append(my_list.pop())  # Removing the last item ('cherry') and 
#dding it to empty_popped_list
print("After popping the last item, the original list is:", my_list)
print("The empty popped list is:", empty_popped_list)
# Popping an item at a specified index (index 1, which is 'blueberry')
print(f"My favorite fruit is {my_list.pop(1).title()}")  # Output: My favorite fruit is Blueberry
print("After popping the item at index 1, the original list is:", my_list)