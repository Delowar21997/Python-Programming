#The range() function is used to generate a sequence of numbers. It can take one, two, or three arguments: start, stop, and step. The start argument is the number at which the sequence starts (inclusive), the stop argument is the number at which the sequence ends (exclusive), and the step argument is the difference between each number in the sequence.
# Here’s how you can use the range() function in a for loop:
# Using range() with one argument (stop)
empty_list = []
for dict_num in range(10):
    dict1 = {'name': 'Adib', 'age': 5, 'city': 'Dinajpur'}
    empty_list.append(dict1)
    print(f"The updated list: \033[1;92m{empty_list}\033[0m\n")

for i in empty_list[:3]: # This will print the first three dictionaries in the list.
    print(f"First three dictionaries: \033[1;92m{i}\033[0m\n")

print(f"The length of the empty_list: \033[1;92m{len(empty_list)}\033[0m\n")