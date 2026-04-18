# The get() method returns the value of the item with the specified key.
# If the key does not exist, it returns None (or you can specify a default value).
my_dict = { 'name': 'Adib', 'age': 5, 'city': 'Dinajpur' }
print(f'my_dict.get("name"): {my_dict.get("name").upper()}')  # Output: ADIB
print(f'my_dict.get("age"): {my_dict.get("age")}')   # Output: 5
print(f'my_dict.get("city"): {my_dict.get("city").capitalize()}')  # Output: Dinajpur
print(f'my_dict.get("country"):\033[1;91m {my_dict.get("country", "Not Found!").upper()}\033[0m')  # Output: NOT FOUND