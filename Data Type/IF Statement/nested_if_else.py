# take input from the user that can be a number or a string and check if the input is a number or a string using the "in" operator and "not in" operator.   
age = float(input("Enter your age: "))
if age >=18:
    print(f"Your age is \033[1;92m{age}\033[0m and you are old enough to vote.")
    country = input("Enter your country: ")
    if country.lower() == "bangladesh":
        print(f"You are from \033[1;92m{country.title()}\033[0m and you can vote in Bangladesh.")
    else:
        print(f"You are from \033[1;91m{country.title()}\033[0m and you may not be able to vote in Bangladesh.")
else:
    print(f"Your age is \033[1;91m{age}\033[0m and you are not old enough to vote.")