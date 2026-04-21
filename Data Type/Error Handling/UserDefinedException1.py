"""class InvalidCitizenError(Exception):
    def __init__(self, message="You must be at least 18 years old for this application."):
        self.message = message
        super().__init__(self.message)  """ # We can use both.

class InvalidCitizenError(Exception):
    def __init__(self):
        print("You must be at least 18 years old for this application.")
    pass
try:
    age=int(input("Enter your age: "))
    if age<18:
        raise InvalidCitizenError
    print(f'\033[35mYour age is {age}.\033[0m')
except InvalidCitizenError as e:
    print(f'\033[31mError: {e}\033[0m')
print(f'\033[33m{15*"*"}Rest of the program{15*"*"}\033[0m')