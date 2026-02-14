# remove() method removes the first occurrence of a specified value from the list.
my_list = ['apple', 'banana', 'cherry', 'date', 'banana']
print("Original list:", my_list)
favocuirt_fruit = my_list.remove('banana')  # Removing the first occurrence of 'banana'
print("After removing the first occurrence of 'banana':", my_list)
# the remove method does not return the removed element, it returns None
print("My favorite fruit is:", favocuirt_fruit)  # Output: My favorite fruit is: None