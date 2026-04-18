#Mathematical comparisons in Python include operators such as
#  < (less than), > (greater than), <= (less than or equal to),
#  >= (greater than or equal to), == (equal to), and != (not equal to).
#  These operators are used to compare values and return a boolean 
# result (True or False) based on the comparison. Here are some examples
# of mathematical comparisons in Python:
# Comparing numbers
a = 10
b = 20
print(f"The value of a is: \033[1;92m{a}\033[0m and the value of b is: \033[1;92m{b}\033[0m\n")
print(f"a < b: \033[92m{a < b}\033[0m")  # Output: True
print(f"a > b: \033[91m{a > b}\033[0m")  # Output: False
print(f"a <= b: \033[92m{a <= b}\033[0m")  # Output: True
print(f"a >= b: \033[91m{a >= b}\033[0m")  # Output: False
print(f"a == b: \033[91m{a == b}\033[0m")  # Output: False
print(f"a != b: \033[92m{a != b}\033[0m")  # Output: True
# Comparing strings
str1 = "Hello"
str2 = "World"  
print(f'The value of str1 is: \033[1;92m"{str1}"\033[0m and the value of str2 is: \033[1;92m"{str2}"\033[0m\n')
print(f"str1 < str2: \033[92m{str1 < str2}\033[0m")  # Output: True (lexicographical order)
print(f"str1 > str2: \033[91m{str1 > str2}\033[0m")  # Output: False
print(f"str1 <= str2: \033[92m{str1 <= str2}\033[0m")  # Output: True
print(f"str1 >= str2: \033[91m{str1 >= str2}\033[0m")  # Output: False
print(f"str1 == str2: \033[91m{str1 == str2}\033[0m")  # Output: False
print(f"str1 != str2: \033[92m{str1 != str2}\033[0m")  # Output: True
# Comparing lists
list1 = [1, 2, 3]
list2 = [1, 2, 4]
print(f"The value of list1 is: \033[1;92m{list1}\033[0m and the value of list2 is: \033[1;92m{list2}\033[0m\n")
print(f"list1 < list2: \033[92m{list1 < list2}\033[0m")  # Output: True (compares element-wise)
print(f"list1 > list2: \033[91m{list1 > list2}\033[0m")  # Output: False
print(f"list1 <= list2: \033[92m{list1 <= list2}\033[0m")  # Output: True
print(f"list1 >= list2: \033[91m{list1 >= list2}\033[0m")  # Output: False
print(f"list1 == list2: \033[91m{list1 == list2}\033[0m")  # Output: False
print(f"list1 != list2: \033[92m{list1 != list2}\033[0m")  # Output: True

