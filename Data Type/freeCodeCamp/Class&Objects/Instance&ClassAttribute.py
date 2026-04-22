class StudentClass:
    # Class attribute
    university_name = "Begum Rokeya University"
    def __init__(self, name, ID, department):
        # Instance attributes
        self.name = name
        self.ID = ID
        self.department = department
# Creating instances of the StudentClass
    def student_info(self):
        if self.name == student1.name:
            print(f"\033[1;32mMy name is {self.name}, my ID is \033[1;33m{self.ID} \033[1;32mand I am from the {self.department} department.I study at \033[1;91m{StudentClass.university_name}.\033[0m")
        elif self.name == student2.name:
            print(f"\033[1;36mMy name is {self.name}, my ID is \033[1;33m{self.ID} \033[1;36mand I am from the {self.department} department.I study at \033[1;91m{StudentClass.university_name}.\033[0m")
        elif self.name == student3.name:
            print(f"\033[1;34mMy name is {self.name}, my ID is \033[1;33m{self.ID} \033[1;34mand I am from the {self.department} department. I study at \033[1;91m{StudentClass.university_name}.\033[0m")
        else:
            print(f"\033[1;37mMy name is {self.name}, my ID is \033[1;33m{self.ID} \033[1;37mand I am from the {self.department} department. I study at \033[5;1;91m{StudentClass.university_name}.\033[0m")
student1 = StudentClass("Adil", 19712024, "CSE")
student2 = StudentClass("Alia", 19712025, "EEE")
student3 = StudentClass("Sara", 19712026, "BBA")
student4 = StudentClass("Nuhan", 19712027, "CSE")   #else condition is for student4 because his name is different from the other three students.
student1.student_info()
student2.student_info()
student3.student_info()
student4.student_info()         #This code is calling the student_info method for each student object to display their information.
