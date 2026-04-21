class ConstTest():
    data = "Testing for Constructor."
    def __init__(self,a,b,c):
        print(f'This is from constructor, {a}')
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        self.d = 1000
        print(self.a + self.b + self.c)

obj = ConstTest(1,2,3)
obj.add()  # Function Call so, no error.
print(obj.d) 
# If the function "add" is not called, 
# AttributeError: 'ConstTest' object has no attribute 'd' occurs

print("------"*10)
print(
'''Create a class ATM:
-> Constructor initializes balance
-> Methods: deposit and withdraw. ''')
print("------"*10)

class ATM():
    def __init__(self):
        self.balance = 10000

    def deposit(self, deposited):
        if deposited < 0:
            return "The deposited amount should be positive.\n"
        
        self.balance += deposited
        return(f'''You deposited {deposited} amount, 
and your current balance becomes {self.current_balance()}\n''')
    
    def withdraw(self, withd):
        if withd > self.balance:
            return "Limit Exceeded!.\n"

        self.balance = self.balance - withd

        return(f'''You withdrew {withd} amount 
and current balance becomes {self.current_balance()}.\n''')

    def current_balance(self):
        return self.balance
    
obj = ATM()
print(obj.deposit(1900))
print(obj.withdraw(1000))
print(obj.withdraw(190000))
print(obj.deposit(-12002))

print("------"*10)
print('''Create a class Temperature()
-> Constructor takes Celsius
-> Convert to Fahrenheit. ''')
print("------"*10)
class Temperature():
    def __init__(self, celsius):
        self.celsius = float(celsius)
    
    def conv(self):
        fahrenheit = (self.celsius * (9/5)) + 32
        return f'The converted fahrenheit is {fahrenheit}.'
        
obj = Temperature(9)
print(obj.conv())

print("------"*10)
print('''Create a class ShoppingCart()
-> Constructor initialized item list
-> Method to add items and calculate total.''')
print("------"*10)
class ShoppingCart():
    def __init__(self, item_list):
        self.item_list = item_list
    
    def addtotal(self):
        total = 0
        for i in self.item_list:
            total += i['Price']
        return f'The total price for your purchase is: {total}'

item = [{"Item": "Apple", "Price": 100},
        {"Item": "Phone", "Price": 10000}, 
        {"Item": "Bottle", "Price": 400},
        {"Item": "Chocolate", "Price": 100}]

obj = ShoppingCart(item)
print(obj.addtotal())

print("------"*10)
print('''Create a class Time()
-> Constructor takes hours and minutes
-> Method to display HH:MM format.''')
print("------"*10)
class Time():
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def change(self):
        ans = 0
        ans = self.minutes/60
        self.hours = self.hours + int(ans)
        self.minutes = self.minutes - (60*int(ans))
    
    def pm(self):
        self.hours = self.hours - 12
        return f'''TIME IS -> {self.hours}:{self.minutes}PM'''
    
    def display(self):
        if self.minutes >= 60:
            self.change()

        if self.hours > 12:
            self.pm()
        
        return f'''TIME IS -> {self.hours}:{self.minutes}AM'''


hour = 1
minutes = 138
obj = Time(hour, minutes)
print(obj.display())

print("------"*10)
print('''Create a class PasswordManager()
-> Constructor sets password
-> Method to check if entered password is correct.''')
print("------"*10)
class PasswordManager():
    def __init__(self):
        self.password = "Krishnaay11"
    
    def check(self, passw):
        if passw == self.password:
            return f'You have entered CORRECT PASSWORD.'
        else:
            return f'You have entered WRONG PASSWORD.'

obj = PasswordManager()
password = "Krishnaay11"
print(obj.check(password))


print("------"*10)
print('''Create a class Order()
Constructor takes:
customer name
list of items (dictionary: item ->price)

Inside Constructor
Calculate total cost
Apply discount: 1000 -> 10% discount.''')

print("------"*10)
class Order():
    def __init__(self, name, items):
        self.name = name
        self.items = items
        self.total = 0
        if isinstance(items, list):
            for i in items:
                self.total += i['Price']
        else:
            print('Item must be in list.')

        if self.total >= 1000:
            self.discount = 0.1 * self.total
            self.total -= self.discount

    def summary(self):
        return (f'''
Your discount amount is: {self.discount}.
Your total cost is: {self.total}.''')

item = [{"Item": "Apple", "Price": 100},
        {"Item": "Phone", "Price": 10000}, 
        {"Item": "Bottle", "Price": 400},
        {"Item": "Chocolate", "Price": 100}
]
obj = Order("Krishnaa", item)
print(obj.summary())

print("------"*10)
print('''
3. Student Management System
Create a class Student():
-> Constructor takes: name, roll number, list of marks.
-> Inside Constructor: Calculate total, average, grade
-> Method: display report''')
print("------"*10)

class Student():
    def __init__(self, name, rollnum, marks_list):
        self.name, self.rollnum = name, rollnum
        self.marks = marks_list
        self.total = 0
        if isinstance(marks_list, list):
            for i in marks_list:
                if i['Mark'] <= 100:
                    self.total += i['Mark']
            self.average = self.total/len(marks_list)
            self.gpa = (self.average/100) * 4.0

    def grade(self):
        if (self.gpa > 3.6 and self.gpa <= 4.0):
            return("A+")
        elif (self.gpa > 3.2 and self.gpa <= 3.6):
            return("A")
        elif (self.gpa > 2.8 and self.gpa <= 3.2):
            return("B+")
        elif (self.gpa > 2.4 and self.gpa <= 2.8):
            return("B")
        elif (self.gpa > 2.0 and self.gpa <= 2.4):
            return("C+")
        elif (self.gpa > 1.6 and self.gpa <= 2.0):
            return("C")
        elif (self.gpa > 0.8 and self.gpa <= 1.6):
            return("D")
        elif (self.gpa > 0 and self.gpa <= 0.8):
            return("E")
        else:
            return("It is an invalid grade for the system.")

    def display(self):
            return(f'''
  Full Name:   {self.name}
Roll Number:   {self.rollnum}
 Total mark:   {self.total}
        GPA:   {self.gpa}\n
      Grade:   {self.grade()}\n''')

marks = [{"Subject": "Maths", "Mark": 90},
        {"Subject": "Science", "Mark": 89}, 
        {"Subject": "English", "Mark": 75},
        {"Subject": "Nepali", "Mark": 72},
        {"Subject": "Social", "Mark": 82}        
]

obj = Student("Krishnaa", 12, marks)
print(obj.display())



# Inheritance:
# Single Inheritance:
print("------"*10)
print("Inheritance")
print("Single Inheritance\n")

class Parent():
    data = "Broadway"

    def add(self):
        return "This is method from parent class."
    
class Child(Parent):
    a = 100

obj = Child()
print(obj.data)
print(obj.add())

# @staticmethod vs classmethod

class Parent():
    data = "Broadway"

    @staticmethod
    def add(self):
        return "This is method from parent class."

    @classmethod
    def data1(cls, a):
        ...
    
class Child(Parent):
    a = 100

obj = Child()
print(obj.data)