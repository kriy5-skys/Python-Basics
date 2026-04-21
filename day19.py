# Single inheritance
class Parent():
    a = 100
    b = 1000
    def add(self):
        return self.a + self.b

class Child(Parent):
    def result(self):
        return self.add()

obj = Child()
print(obj.result())

# To call constructor from both levels
print("------"*10)
class Parent():
    def __init__(self):
        print("This is cons from parent")

    a = 100
    b = 1000
    def add(self):
        return self.a + self.b

class Child(Parent):
    def __init__(self):
        print("This is cons from child.")  
        # Here, the constructor inside Child is called only, 
        # because it gives itself the priority.
        # Also, if we need to call the constructor in the Parent as well, we can use the syntax: Parent.__init__(self)
        #Or, which is more preferred. 
        super().__init__()  
        # This is used in all types of inheritance, and all the constructor of the given parent are executed.
    def result(self):
        return self.add()

obj = Child()
print(obj.result())

# To call constructor from both levels and how to pass arguments:
print("------"*10)
class Parent():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("This is cons from parent")
    def add(self):
        return self.a + self.b

class Child(Parent):
    def __init__(self,a,b):
        print("This is cons from child.")  
        super().__init__(a,b)
    def result(self):
        return self.add()

obj = Child(11,12)
print(obj.result())

# Multilevel Inheritance
print("------"*10)
class Parent():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("This is cons from parent")
    def add(self):
        return self.a + self.b

class Child(Parent):
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("This is cons from child.")  
    def result(self):
        return self.add()

class GrandChild(Child):
    def summary(self):
        return self.result()       

# Without the super()

obj = GrandChild(1,2)
print(obj.summary())

'''
Create person()
'''
print("-----"*10)
class Person():
    name = "Krishnaa"
    age = 19
    def __init__(self, language = "EN"):
        self.language = language.upper()

    def display_info(self):
        return (f'''Details of the Person:\n  Name: {self.name}\n   Age: {self.age}''')
    
    def display_infonp(self):
        return (f'''Manche ko bibaran:\n        Naam: {self.name}\n        Umer: {self.age}''')

class Student(Person):
    id = 12345
    def display_student(self):
        return(f'{self.display_info()}\n    ID: {self.id}')
    
    def display_studentnp(self):
        return(f'{self.display_infonp()}\nParichayaNo.: {self.id}')


class Graduate(Student):
    thesis = "Data Structure"
            
    def display_detailnp(self):
        return(f'''{self.display_studentnp()}\n Thesis Naam: {self.thesis}''')

    def display_detail(self):
                return(f'''{self.display_student()}\nThesis: {self.thesis}''')

    def summary(self):
        if self.language == "NP":
            return (self.display_detailnp())
        else:
            return (self.display_detail())

lan = "np"
obj = Graduate(lan)
print(obj.summary())

# Multiple Inheritance:
# class test(student, graduate): 
# Here, student is the 1st priority.
# This class has more than one parent class, and inherits properties and methods from them.

# This is used for code reuse, to functionally combine more in one class
class Parent:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        print("This is cons from parent")
    def add(self):
        return "Hi"

class Father:
    def __init__(self):
        pass
    def skill1(self):
        return "Driving"

class Mother:
    def skill2(self):
        return "Cooking"

class Child(Father, Mother,Parent):
    def skill3(self):
        return("Coding", self.skill1(), self.skill2(), self.add())

c = Child()
print(c.skill3())

