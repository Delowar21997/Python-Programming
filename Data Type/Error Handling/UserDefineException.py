class InvalidCitizenError(Exception):
    pass
try:
    age=int(input("Enter your age: "))
    if age<18:
        raise InvalidCitizenError("You must be at least 18 years old for this application.")
    print(f'\033[35mYour age is {age}.\033[0m')
except InvalidCitizenError as e:
    print(f'\033[31mError: {e}\033[0m')
print(f'\033[33m{15*"*"}Rest of the program{15*"*"}\033[0m')