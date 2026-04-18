#Nested if_elif_else statements.

county = input("Enter the county you live in: ")

if county.lower() == "bangladesh":
    print(f"You are a citizen of \033[1;92m{county.title()}\033[0m.")
    age = float(input("Enter your age: "))
    if age >=18:
        print(f"You are \033[1;92m{age}\033[0m years old and you are old enough to vote.")
    else:
        print(f"You are \033[1;91m{age}\033[0m years old and you are not old enough to vote.")
elif county.lower() == "india":
    print(f"You are a citizen of \033[1;92m{county.title()}\033[0m.")
    age = float(input("Enter your age: "))
    if age >=18:
        print(f"You are \033[1;92m{age}\033[0m years old and you are old enough to vote.")
    else:
        print(f"You are \033[1;91m{age}\033[0m years old and you are not old enough to vote.")
elif county.lower() == "usa":
    print(f"You are a citizen of \033[1;92m{county.title()}\033[0m.")
    age = float(input("Enter your age: "))
    if age >=18:
        print(f"You are \033[1;92m{age}\033[0m years old and you are old enough to vote.")
    else:
        print(f"You are \033[1;91m{age}\033[0m years old and you are not old enough to vote.")
else:
    if county.lower() == county.lower():
        print(f"You are a citizen of \033[1;91m{county.title()}\033[0m and you may not be able to vote in Bangladesh, India, or USA.")
        age = float(input("Enter your age: "))
        if age >=18:
            print(f"You are \033[1;92m{age}\033[0m years old and you may be old enough to vote in \033[1;92m{county.title()}\033[0m.")
        else:
            print(f"You are \033[1;91m{age}\033[0m years old and you may not be old enough to vote in your country.")



print("\n"+"\033[1;92m*"*15+ f" You are an aware citizen of {county.title()}."+"*"*15+"\033[0m\n")
