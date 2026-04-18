# Del statement is use to remove an element from a list by specifying its index.
my_list = ['apple', 'banana', 'cherry', 'date', 'fig']
print("Original list:", my_list)
del my_list[1]  # Deleting the element at index 1 ('banana')
print("After deleting the element at index 1:", my_list)
my_list1 = ['apple', 'banana', 'cherry', 'date', 'fig']
print("Original list:", my_list1)
del my_list1[0:2]  # Deleting elements from index 0 to 1 ('apple' and 'banana')
print("After deleting elements from index 0 to 1:", my_list1)
my_list2 = ['apple', 'banana', 'cherry', 'date', 'fig']
print("Original list:", my_list2)
del my_list2[2:] # Deleting all elements from index 2 onwards
print("After deleting all elements from index 2 onwards:", my_list2)  
my_list3 = ['apple', 'banana', 'cherry']
print("Original list:", my_list3)   
del my_list3[:]  # Deleting all elements in the list
print("After deleting all elements, the list is:", my_list3)  # Output: After deleting all elements, the list is: []    

