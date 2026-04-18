# sorted() function is used to sort the items of a dictionary by key or by value.   
# By default, sorted() sorts the items by key. 
# To sort by value, you can use the key parameter with a lambda function.
my_dict = { 'name': 'Adib', 'age': 5, 'city': 'Dinajpur' }
print(f"Original my_dict: \033[1;97m{my_dict}\033[0m\n")
# Sorting by key
for key in sorted(my_dict.keys()):
    print(f"Sorted by key: \033[1;92m{key.capitalize()}\033[0m")
print(f"\nList of sorted keys: \033[1;92m{list(sorted(my_dict.keys()))}\033[0m\n")
print(f"Sorted() func does not change the original dictionary: \033[1;97m\n{my_dict}\033[0m")
# Sorting by value
'''print("\nAfter sorting by value:")
for value in sorted(my_dict.values()):
    print(f"Sorted by value: \033[1;92m{value.capitalize()}\033[0m")'''