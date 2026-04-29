# Special methods, also known as magic methods or dunder methods (double underscore), 
# are predefined methods in Python that allow you to define the behavior of your objects in specific situations. 
# They enable you to implement custom behavior for built-in operations such as addition, subtraction, string representation, and more.
# The special methods are 
# 1. __init__() is a constructor method that is called when an object is created. It initializes the object's attributes.
# 2. __str__() is a method that defines the string representation of an object. It is called when you use the str() function or print() function on an object.
# 3. __repr__() is a method that defines the official string representation of an object. It is called when you use the repr() function on an object or when you inspect an object in the interactive shell.
# 4. __len__() is a method that defines the behavior of the len() function when called on an object. It should return the length of the object.
# 5. __getitem__() is a method that defines the behavior of the indexing operator ([]) when used on an object. It should return the item at the specified index.
# 6. __contains__() is a method that defines the behavior of the in operator when used to check if an item is in an object. It should return True if the item is found and False otherwise.
# 7. __iter__() is a method that defines the behavior of the iter() function when called on an object. It should return an iterator object that can be used to iterate over the elements of the object. 
# 8. __add__() is a method that defines the behavior of the addition operator (+) when used with objects of a class. It should return the result of adding two objects together.    
# 9. __sub__() is a method that defines the behavior of the subtraction operator (-) when used with objects of a class. It should return the result of subtracting one object from another.
# 10. __mul__() is a method that defines the behavior of the multiplication operator (*) when used with objects of a class. It should return the result of multiplying two objects together.
# 11. __truediv__() is a method that defines the behavior of the division operator (/) when used with objects of a class. It should return the result of dividing one object by another.
# 12. __floordiv__() is a method that defines the behavior of the floor division operator (//) when used with objects of a class. It should return the result of performing floor division on two objects.
# 13. __mod__() is a method that defines the behavior of the modulus operator (%) when used with objects of a class. It should return the result of performing modulus operation on two objects.
# 14. __pow__() is a method that defines the behavior of the exponentiation operator (**) when used with objects of a class. It should return the result of raising one object to the power of another.
# 15. __eq__() is a method that defines the behavior of the equality operator (==) when used with objects of a class. It should return True if the objects are considered equal and False otherwise.
# 16. __ne__() is a method that defines the behavior of the inequality operator (!=) when used with objects of a class. It should return True if the objects are considered not equal and False otherwise.
# 17. __lt__() is a method that defines the behavior of the less than operator (<) when used with objects of a class. It should return True if the object is considered less than another object and False otherwise.
# 18. __le__() is a method that defines the behavior of the less than or equal to operator (<=) when used with objects of a class. It should return True if the object is considered less than or equal to another object and False otherwise.
# 19. __gt__() is a method that defines the behavior of the greater than operator (>) when used with objects of a class. It should return True if the object is considered greater than another object and False otherwise.
# 20. __ge__() is a method that defines the behavior of the greater than or equal to operator (>=) when used with objects of a class. It should return True if the object is considered greater than or equal to another object and False otherwise.
# 21. __call__() is a method that defines the behavior of an object when it is called as a function. It should return the result of calling the object as a function.
# 22. __enter__() and __exit__() are methods that define the behavior of an object when used in a with statement. They should return the result of entering and exiting the context of the with statement, respectively.
# 23. __del__() is a method that defines the behavior of an object when it is about to be destroyed. It should return the result of performing any necessary cleanup before the object is destroyed.
# 24. __getattr__() is a method that defines the behavior of an object when an attribute is accessed that does not exist. It should return the result of handling the missing attribute access.
# 25. __setattr__() is a method that defines the behavior of an object when an attribute is set. It should return the result of handling the attribute assignment.
# 26. __delattr__() is a method that defines the behavior of an object when an attribute is deleted. It should return the result of handling the attribute deletion.
# 27. __dir__() is a method that defines the behavior of the dir() function when called on an object. It should return a list of valid attributes for the object.
# 28. __getattribute__() is a method that defines the behavior of an object when any attribute is accessed. It should return the result of handling the attribute access.
# 29. __setitem__() is a method that defines the behavior of the indexing operator ([]) when used to set an item in an object. It should return the result of handling the item assignment.
# 30. __delitem__() is a method that defines the behavior of the indexing
# 31. operator ([]) when used to delete an item from an object. It should return the result of handling the item deletion.
# 32. __missing__() is a method that defines the behavior of a mapping object when a key is accessed that does not exist. It should return the result of handling the missing key access.
# 33. __format__() is a method that defines the behavior of the format() function when called on an object. It should return the result of formatting the object according to a specified format string.
# 34. __sizeof__() is a method that defines the behavior of the sys.getsizeof() function when called on an object. It should return the size of the object in bytes.
# 35. __hash__() is a method that defines the behavior of the hash() function when called on an object. It should return the hash value of the object.
# 36. __bool__() is a method that defines the behavior of the bool() function when called on an object. It should return True if the object is considered true and False otherwise.
# 37. __index__() is a method that defines the behavior of an object when it is used in a context that requires an integer index. It should return the integer value of the object.
# 38. __instancecheck__() is a method that defines the behavior of the isinstance() function when called on an object. It should return True if the object is an instance of a specified class and False otherwise.
# 39. __subclasscheck__() is a method that defines the behavior of the issubclass() function when called on an object. It should return True if the object is a subclass of a specified class and False otherwise.
# 40. __prepare__() is a method that defines the behavior of a metaclass when preparing the namespace for a class definition. It should return a mapping object that will be used as the namespace for the class definition.
# 41. __class__ is an attribute that holds a reference to the class of an object. It can be used to access class-level attributes and methods from an instance of the class.
# 42. __dict__ is an attribute that holds a dictionary of an object's attributes and their corresponding values. It can be used to access and modify the attributes of an object dynamically.
# 43. __doc__ is an attribute that holds the docstring of a class, method, or function. It can be used to access the documentation for a class, method, or
# 44. __name__ is an attribute that holds the name of a class, method, or function. It can be used to access the name of a class, method, or function for various purposes, such as debugging or logging.
# 45. __module__ is an attribute that holds the name of the module in which a class, method, or function is defined. It can be used to access the module name for various purposes, such as debugging or logging.
#. 46. __bases__ is an attribute that holds a tuple of the base classes of a class. It can be used to access the base classes of a class for various
# 47. __mro__ is an attribute that holds a tuple of the method resolution order for a class. It can be used to access the method resolution order for a class, which determines the order in which methods are looked up when called on an instance of the class.
# 48. __slots__ is an attribute that can be defined in a class to specify a fixed set of attributes for instances of the class. It can be used to optimize memory usage and improve performance by preventing the creation of a __dict__ for each instance of the class.
# 49. __weakref__ is an attribute that holds a list of weak references to an object. It can be used to access the weak references to an object, which allows for the creation of circular references without causing memory leaks.
# 50. __annotations__ is an attribute that holds a dictionary of type annotations for a class, method, or function. It can be used to access the type annotations for a class, method, or function, which can be used for type checking and documentation purposes.
# 51. __closure__ is an attribute that holds a tuple of cells that contain the bindings for the free variables in a function. It can be used to access the closure of a function, which allows for the creation of nested functions and the use of variables from the enclosing scope.
# 52. __code__ is an attribute that holds a code object representing the compiled bytecode of a function. It can be used to access the code object of a function, which contains information about the function's arguments, local variables, and bytecode instructions.
# 53. __defaults__ is an attribute that holds a tuple of default values for the parameters of a function. It can be used to access the default values for a function's parameters, which can be used for various purposes, such as providing default arguments when calling a function.
# 54. __globals__ is an attribute that holds a reference to the global namespace in which a function is defined. It can be used to access the global variables and functions that are available in the scope of a function.
# 55. __kwdefaults__ is an attribute that holds a dictionary of default values for the keyword-only parameters of a function. It can be used to access the default values for a function's keyword-only parameters, which can be used for various purposes, such as providing default arguments when calling a function with keyword arguments.
#These special methods allow you to define how your objects behave in different contexts and can be used to create more intuitive and powerful classes in Python. By implementing these methods, you can customize the behavior of your objects and make them work seamlessly with built-in functions and operators.



class Cart:
   def __init__(self):
       self.items = []

   def add(self, item):
       self.items.append(item)

   def remove(self, item):
       if item in self.items:
           self.items.remove(item)
       else:
           print(f'{item} is not in cart')

   def list_items(self):
       return self.items

   def __len__(self):
       return len(self.items)

   def __getitem__(self, index):
       return self.items[index]

   def __contains__(self, item):
       return item in self.items

   def __iter__(self):
       return iter(self.items)
   

cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
   print(item, end=' ') # Laptop Wireless mouse Ergo keyboard Monitor

print(len(cart)) # 4
print(cart[3]) # Monitor

print('Monitor' in cart) # True
print('banana' in cart) # False

cart.remove('Ergo keyboard')

print(cart.list_items()) # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana') # banana is not in cart