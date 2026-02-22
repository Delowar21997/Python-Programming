# if_elif_else is used to make decisions in code based on multiple conditions. 
# It allows you to execute different blocks of code based on whether certain conditions are true or false.
# The basic syntax of an if-elif-else statement in Python is as follows:
# if condition1:
#     # code to execute if condition1 is true   
# elif condition2:
#     # code to execute if condition2 is true
# else:
#     # code to execute if all conditions are false
# Here is an example of an if-elif-else statement in Python:
age = int(input("Please enter your age: "))
if age>=0 and age<18:
    print(f"\033[1;92m{age}\033[0m is a minor.")
elif age>=18 and age<65:
    print(f"\033[1;92m{age}\033[0m is an adult.")
else:
    print(f"\033[1;92m{age}\033[0m is a senior citizen.")