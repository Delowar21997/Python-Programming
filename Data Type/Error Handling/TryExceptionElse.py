num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))
try:
    result=num1/num2
    print(result)
except ZeroDivisionError as e:
    print(f'\033[91mError: {e}.\033[0m')
else:
    print('\033[93mThere is no exception error.\033[0m')
print('\033[92mThanks for handling the exception properly.\033[0m')