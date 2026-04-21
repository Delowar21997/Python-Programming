num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))
try:
    result=num1/num2
    print(div)
except ZeroDivisionError:
    print('\033[91mError: Python does not allow you to divide a number by zero. Please provide a non-zero divisor.\033[0m')
except NameError:
    print('\033[91mError: Please check your variable names.\033[0m')
print('\033[92mSince the exception is handled, this line will be executed.\033[0m')
print('\033[92mThanks for handling the exception properly.\033[0m')