class Person: 
    def __init__(self, name, age): 
        self.name = name
        self.age = age

person = Person('John Doe', 30)

# Get the attribute name from user input.
attr_name = input('Enter the attribute you want to see: ').lower()
print(getattr(person, attr_name, 'Attribute not found'))