# Increment dictionary value
my_dict = {}
my_dict['name'] = input("Enter name: ").capitalize()
my_dict['age'] = float(input("Enter age: "))
my_dict['city'] = input("Enter city: ").capitalize()

print(f"Original my_dict: \033[1;97m{my_dict}\033[0m\n")
print(f"Original age is: \033[1;92m{my_dict['age']}\033[0m\n")

if my_dict['city'] == 'Dinajpur':
    new_age = 10
elif my_dict['city'] == 'Dhaka':
    new_age = 3
elif my_dict['city'] == 'Chittagong':
    new_age = 4
else:
    new_age = 20
my_dict['age'] = my_dict['age'] + new_age
print(f"Modified age is: \033[1;92m{my_dict['age']}\033[0m\n")
print(f"Modified my_dict: \033[1;97m{my_dict}\033[0m\n")
