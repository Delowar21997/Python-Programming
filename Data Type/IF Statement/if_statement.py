# if statement is used to make decisions in code based on certain conditions. It allows you to execute a block of code only if a specified condition is true.   
# The basic syntax of an if statement in Python is as follows:
# if condition:
#     # code to execute if the condition is true    
# Here is an example of an if statement in Python:
fruits = ['apple', 'banana', 'orange']
for i in fruits:
    if i == 'banana':
        print(f'\033[1;6;33m{i.upper()}\033[0m is my favorite fruit!')
    else:
        print(f'\033[1;91m{i.capitalize()}\033[0m, \033[1;37mI love it a lot.\033[0m')