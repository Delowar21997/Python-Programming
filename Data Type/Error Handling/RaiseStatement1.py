age=int(input("Enter your age: "))
try:
    if age<0 or age==0:
        raise ValueError("Age cannot be negative or zero. Please provide a valid age.")
    print(f'\033[33mYour age is {age}.\033[0m')
except ValueError as e:
    print(f'\033[31mError: {e}\033[0m')

print(f'\033[32mThanks for handling the exception properly.\033[0m')