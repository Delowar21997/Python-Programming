#The use in operator is used to check if a value exists in a sequence (like a list, tuple, or string). It returns True if the value is found in the sequence and False otherwise. Here are some examples of using the "in" operator in Python:
# Checking if a value is in a list
my_list = [1, 2, 3, 4, 5]
print(f"The value of my_list is: \033[1;92m{my_list}\033[0m\n")
print(f"3 in my_list: \033[92m{3 in my_list}\033[0m")  # Output: True
print(f"6 in my_list: \033[91m{6 in my_list}\033[0m")  # Output: False
# Checking if a value is in a string    
my_string = "Hello, World!"
print(f"The value of my_string is: \033[1;92m{my_string}\033[0m\n")
print(f"'Hello' in my_string: \033[92m{'Hello' in my_string}\033[0m")  # Output: True
print(f"'Python' in my_string: \033[91m{'Python' in my_string}\033[0m")  # Output: False    
# Checking if a value is in a tuple
my_tuple = (1, 2, 3, 4, 5)
print(f"The value of my_tuple is: \033[1;92m{my_tuple}\033[0m\n")
print(f"3 in my_tuple: \033[92m{3 in my_tuple}\ 033[0m")  # Output: True
print(f"6 in my_tuple: \033[91m{6 in my_tuple}\033[0m")  # Output: False
