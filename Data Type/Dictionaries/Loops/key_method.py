# key method is used to access the value of a specific key in a dictionary. 
# You can use the key method to retrieve the value associated with a particular key in a dictionary. 
# Here’s how you can use it:

my_dict = { 'name': 'Adib', 'age': 5, 'city': 'Dinajpur' }
print(f"My dictionary: \033[1;97m{my_dict}\033[0m\n")
# Accessing values using keys
for key in my_dict.keys():
#for key in my_dict: # This is also a valid way to access keys in a dictionary. When you iterate over a dictionary, it returns the keys by default.
    print(f"The key of the dictionary: \033[1;92m{key.capitalize()}\033[0m")
    #print(f"Value of '{key}': \033[1;92m{my_dict[key]}\033[0m")