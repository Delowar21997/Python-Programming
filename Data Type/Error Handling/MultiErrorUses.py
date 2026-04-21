import sys
num1=int(input('Enter the first number: '))
num2=int(input('Enter the second number: '))
try:
    result=num1/num2
    print(resul)
except (ZeroDivisionError, NameError) as e:
    print(f'\033[91mError:{e}.\033[0m')
    print(e.__class__)          # This will print the full class name of the exception, including the module name.
    print(e.__class__.__name__) # This will print the name of the exception class without the module name.
    print(e.args)               # This will print a tuple containing the arguments passed to the exception when it was raised.
    print(sys.exc_info())       # This will print a tuple containing the exception type, value, and traceback information. The first element is the exception type, the second element is the exception instance (which contains the error message), and the third element is the traceback object that provides information about where the exception occurred in the code.
    print(sys.exc_info()[1])    # This will print the exception instance (which contains the error message).
print('\033[92mSince the exception is handled, this line will be executed.\033[0m')
print('\033[92mThanks for handling the exception properly.\033[0m')