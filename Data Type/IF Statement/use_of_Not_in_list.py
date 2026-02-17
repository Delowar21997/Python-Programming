#The use of the "not in" operator is used to check if a value does not exist in a sequence (like a list, tuple, or string). It returns True if the value is not found in the sequence and False otherwise. Here are some examples of using the "not in" operator in Python:
# Checking if a value is not in a list
my_list = [1, 2, 3, 4, 5]
print(f"The value of my_list is: \033[1;92m{my_list }\033[0m\n")
print(f"6 not in my_list: \033[92m{6 not in my_list}\033[0m")  # Output: True
print(f"3 not in my_list: \033[91m{3 not in my_list}\033[0m")  # Output: False
# Checking if a value is not in a string
my_string = "Hello, World!"
print(f"The value of my_string is: \033[1;92m{my_string}\033[0m\n")
print(f"'Python' not in my_string: \033[92m{'Python' not in my_string}\033[0m")  # Output: True
print(f"'Hello' not in my_string: \033[91m{'Hello' not in my_string}\033[0m")  # Output: False
# Checking if a value is not in a tuple
my_tuple = (1, 2, 3, 4, 5)
print(f"The value of my_tuple is: \033[1;92m{my_tuple}\033[0m\n")
print(f"6 not in my_tuple: \033[92m{6 not in my_tuple}\033[0m")  # Output: True
print(f"3 not in my_tuple: \033[91m{3 not in my_tuple}\033[0m")  # Output: False
# Checking if a character is not in a string
char = 'x'
print(f"The value of char is: \033[1;92m'{char}'\033[0m\n")
print(f"'{char}' not in my_string: \033[92m{char not in my_string}\033[0m")  # Output: True
char2 = 'o' 
print(f"The value of char2 is: \033[1;92m'{char2}'\033[0m\n")
print(f"'{char2}' not in my_string: \033[91m{char2 not in my_string}\033[0m")  # Output: False  
print("\n" + "_&_*" * 15 + "\n")  # Separator for clarity
fruits = ["apple", "banana", "cherry"]
x = "grape"
if x not in fruits:
    print(f"\033[1;92m{x.title()}\033[0m is not in the list of fruits, it's a delicious choice!")   
