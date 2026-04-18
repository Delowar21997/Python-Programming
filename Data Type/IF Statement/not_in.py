# not in is a membership operator in Python that checks 
# if a value is not present in a sequence (like a list, tuple, or string). 
# It returns True if the value is not found in the sequence and False if it is found.
# Example usage of "not in" operator

my_string = "Hello, World!"
print(f"The value of my_string is: \033[1;92m{my_string}\033[0m\n")


my_list = [1, 2, 3, 4, 5]
print(f"The value of my_list is: \033[1;92m{my_list}\033[0m\n")
number = 6
if number not in my_list:
    print(f"\033[1;92m{number}\033[0m is not in the list.")
number2 = 3
if number2 not in my_list:
    print(f"\033[1;92m{number2}\033[0m is not in the list.")
else:
    print(f"\033[1;91m{number2}\033[0m is in the list.")
word = "Python"
print(f"Is 'Python' in my_string? \033[1;92m{word not in my_string}\033[0m")