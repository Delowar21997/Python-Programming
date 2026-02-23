# del statement is use for removing an item from a dictionary by referring to its key name.
my_dict = { 'name': 'Adib', 'age': 5, 'city': 'Dinajpur' }
print(f"Original my_dict: \033[1;97m{my_dict}\033[0m\n")
del my_dict['city']
print(f"After deleting 'city': \033[1;92m{my_dict}\033[0m")