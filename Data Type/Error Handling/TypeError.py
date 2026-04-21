num1=int(input("Enter a number: "))
str1=str(input("Enter a string: "))
try:
    result=num1+str1
    print(result)
except TypeError:
    print('\033[31mPython does not allow you to add an integer and a string together. Please provide compatible data types for addition.\033[0m')
print('\033[32mSince the exception is handled, this line will be executed.\033[0m')