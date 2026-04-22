#This code is defining a class named MyClass.
#A class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. 
#In this code, the MyClass class has an __init__ method that initializes the attributes name, ID, and age when an object is created. 
class MyClass:      
    def __init__(self,name,ID,age):
        self.name = name  
        self.ID = ID
        self.age = age

 #This code is defining the method under the MyClass class.
    def sample_method(self):  
        if self.name ==person1.name:
            print(f"\033[1;32mMy name is {self.name} and I am {self.age} years old. My ID is \033[1;4;33m{self.ID}.\033[0m")
        elif self.name ==person2.name:
            print(f"\033[1;36mMy name is {self.name} and I am {self.age} years old. My ID is \033[1;4;33m{self.ID}.\033[0m")

#An object is an instance of a class. It's used to what the class is designed to represent. Here person1 and person2 are the objects.
#This code is creating two objects by using the MyClass class as object constructor.
person1=MyClass("Adil",19712024,8)
person2=MyClass("Alia",19712025,7)
#This code is make the relationship between the objects and the method of the class.
person1.sample_method()
person2.sample_method()