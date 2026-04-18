empty_list = []

for i in range(10):
    dict1 = {'name': 'Sara', 'age': 5, 'city': 'Dinajpur'}
    empty_list.append(dict1)
    #rint(f"The updated list: \033[1;92m{empty_list}\033[0m\n")
for j in empty_list[:3]: # This will print the first three dictionaries in the list.
    if j['name'] == 'Adib':
        j['name'] = 'Sara'
        j['age'] = 10
        j['city'] = 'Dhaka'
    elif j['name'] == 'Sara':
        j['name'] = 'Ali'
        j['age'] = 15
        j['city'] = 'Chittagong'
    #rint(f"First three dictionaries: \033[1;92m{j}\033[0m\n")
for k in empty_list[:7]: # This will print the remaining dictionaries in the list.
    print(f"Remaining dictionaries: \033[1;92m{k}\033[0m")