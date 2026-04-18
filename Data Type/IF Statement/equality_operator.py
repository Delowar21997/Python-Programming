#Equality operator
#The equality operator (==) is used to compare two values for equality. It returns True
#if the values are equal and False if they are not. The equality operator can be used with various data types, including numbers, strings, lists, and more.
#Here are some examples of using the equality operator in Python:
# Comparing numbers
a = 5
b = 5
print(f"a == b: \033[92m{a == b}\033[0m")  # Output: True
# Comparing strings
str1 = "Hello"
str2 = "Hello"
print(f"str1 == str2: \033[92m{str1 == str2}\033[0m")  # Output: True
# Comparing lists
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"list1 == list2: \033[92m{list1 == list2}\033[0m")  # Output: True
# Comparing different types
num = 10
str_num = "10"
print(f"num == str_num: \033[91m{num == str_num}\033[0m")  # Output: False
# Comparing with None
value = None
print(f"value == None: \033[92m{value == None}\033[0m")  # Output: True

car = "Toyota"
car.lower() == "toyota"  # Output: True
print(f"car.lower() == 'toyota': \033[92m{car.lower() == 'toyota'}\033[0m")  # Output: True