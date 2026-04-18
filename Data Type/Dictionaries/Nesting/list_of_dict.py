#List of dictionaries is a data structure that allows you to store multiple dictionaries in a single list.
#  Each dictionary can contain key-value pairs, and you can access and manipulate the dictionaries within 
# the list as needed. This is useful for organizing and managing related data in a structured way.
dict1 = {'name': 'Adib', 'age': 5, 'city': 'Dinajpur'}
dict2 = {'name': 'Sara', 'age': 6, 'city': 'Dhaka'}
dict3 = {'name': 'Ali', 'age': 7, 'city': 'Chittagong'}
dict_list = [dict1, dict2, dict3]
print(f"List of dictionaries: \033[1;97m{dict_list}\033[0m\n")
# Accessing dictionaries in the list
for i in dict_list:
    print(f"Name: \033[1;92m{i['name']}\033[0m, Age: \033[1;92m{i['age']}\033[0m, City: \033[1;92m{i['city']}\033[0m")