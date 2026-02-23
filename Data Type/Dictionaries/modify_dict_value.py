# Modifying dictionary values
# You can change the value of a specific item by referring to its key name.
my_dict = { 'name': 'Adib', 'age': 5, 'city': 'Dinajpur' }
print(f"Original my_dict: \033[1;97m{my_dict}\033[0m\n")
print(f"Original my_dict: \033[1;92m{my_dict['name'].upper()}\033[0m")
my_dict['name'] = 'Nuhan'
print(f"\nModified my_dict: \033[1;92m{my_dict['name'].capitalize()}\033[0m")
print(f"\nModified my_dict: \033[1;97m{my_dict}\033[0m")
