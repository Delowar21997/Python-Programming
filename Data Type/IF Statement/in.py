# in is a membership operator in Python 
# that checks if a value is present in a sequence 
# (like a list, tuple, or string). It returns True if the value 
# is found in the sequence and False otherwise.
# Example usage of "in" operator
my_list = [1, 2, 3, 4, 5]
print(f"The value of my_list is: \033[1;92m{my_list}\033[0m\n")
number = 3
if number in my_list:
    print(f"\033[1;92m{number}\033[0m is in the list.")
number2 = 6
if number2 in my_list:
    print(f"\033[1;92m{number2}\033[0m is in the list.")
else:
    print(f"\033[1;91m{number2}\033[0m is not in the list.")

my_string = "Hello, World!"
print(f"The value of my_string is: \033[1;92m{my_string}\033[0m\n")
word = "Hello"
if word in my_string:
    print(f"\033[1;92m'{word}'\033[0m is in the string.")
else:
    print(f"\033[1;91m'{word}'\033[0m is not in the string.")
word2 = "Hello"
print(f"Is '{word2}' in my_string? \033[1;92m{word2 in my_string}\033[0m")
