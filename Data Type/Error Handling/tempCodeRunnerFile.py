
#print('Hello, World!)
#print("This line will not be executed due to the exception above.")

try:
    exec('print("Hello, World!"')
except SyntaxError as e:
    print(f'\033[31mError: {e}.\033[0m')
print("Thanks for handling the exception properly.")