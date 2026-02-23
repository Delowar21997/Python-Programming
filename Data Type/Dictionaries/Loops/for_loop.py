# For loop in dictionary is used to iterate over the keys, values, or key-value pairs of a dictionary.
# Here are some examples of using for loops with dictionaries:

my_dict = { 'name': 'Adib', 'age': 5, 'city': 'Dinajpur' }
print(f"My dictionary: \033[1;97m{my_dict}\033[0m\n")

for key, value in my_dict.items():
    print(f"Keys with their corresponding values: \033[1;92m{key.capitalize()}\033[0m \033[1;91m:\033[0m \033[1;92m{value}\033[0m")