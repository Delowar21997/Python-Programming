age=int(input("Enter your age: "))
try:
    if age<0 or age==0:
        raise ValueError
    print(f'\033[32mYour age is {age}.\033[0m')
except ValueError:
    print('\033[31mError: Age cannot be negative or zero. Please provide a valid age.\033[0m')

print(f'\033[32mThanks for handling the exception properly.\033[0m')