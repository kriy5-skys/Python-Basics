# # Multiple Inheritance

# # MRO
# # Method Resolution Order
# # It is the way in which the method defines the order 
# # in which the multiple inheritance access the data/or order of the class used in it.

# class test():
#     def testy(self):
#         return "Ok"

# class test1():
#     def testing(self):
#         return "Hello"

# class Child(test,test1):
#     def ok(self):
#         return ("Hi", self.testy(), self.test1())

# obj = Child()
# print(Child.__mro__)


# # @staticmethod and @classmethod: IMP

# # Task: Employee Management System

# print("-----"*10)

# class Person():
#     name = "Krishnaa"
#     age = 21

#     def displayPerson(self):
#         return f"Name: {self.name}, Age: {self.age}"
    
# class Job:
#     jobTitle = "Analyst"
#     salary = 50000

#     def displayJob(self):
#         return f"Job Title: {self.jobTitle}, Salary: {self.salary}"

#     def displayHigher(self):
#         if self.salary > 40000:
#             return "Higher Salary."
#         else:
#             return "Average Salary."

# class Employee(Person, Job):

#     def displayEmployee(self):
#         return f"{self.displayPerson()}, {self.displayJob()}, {self.displayHigher()}"

# obj = Employee()
# print(obj.displayEmployee())

# # class Higher(Job):
# #     def displayHigher(self):
# #         if self.salary > 40000:
# #             return "Higher Salary."
# #         else:
# #             return "Average Salary."

# # obj1 = Higher()
# # print(obj1.displayHigher())


# #Employee management system

# class Person:

#     def setPerson(self,name,age):
#         self.name = name
#         self.age = age
    
#     def display_person(self):
#         return f"name = {self.name}, age = {self.age}"

# class Job:

#     def setJob(self,jobTitle):
#         self.jobTitle = jobTitle

#     def setSalary(self,salary):
#         self.salary = salary

#     def display_job(self):
#         return f"job title = {self.jobTitle} , salary = {self.salary}"

# class Employee(Person,Job):
    
#     def isHighEarner(self):
#         if self.salary > 45000:
#             return "High earner"
#         else:
#             return "Low earner"


#     def display_employee(self):
#         return f'{self.display_person()} , {self.display_job()} , {self.isHighEarner()}'
    

# employee = Employee()
# employee.setPerson("hari",12)
# employee.setJob("pyython")
# employee.setSalary(20000)
# print(employee.display_employee())

# print("-----"*10)
# class Person():
#     def setPerson(self, name, age):
#         self.name = name
#         self.age = age

#     def displayPerson(self):
#         return (f'Name: {self.name}, Age: {self.age}')
    
# class Job:
#     def setJob(self, jobtitle, salary):
#         self.jobtitle = jobtitle
#         self.salary = salary

#     def displayJob(self):
#         return f'Job Title: {self.jobtitle}, Salary: {self.salary}'

#     def displayHigher(self):
#         if self.salary > 40000:
#             return "Higher Salary."
#         else:
#             return "Average Salary."
# class Employee(Person, Job):
#     def displayEmployee(self):
#         return (self.displayPerson(), self.displayJob(), self.displayHigher())

# obj = Employee()

# name =input("Enter name: ")
# age = int(input("Enter age: "))
# jobtitle = input("Enter Job Title: ")
# salary = int(input("Enter salary: "))

# obj = Employee()
# obj.setPerson(name, age)
# obj.setJob(jobtitle, salary)

# print(obj.displayEmployee())

# Encapsulation
# Data access modifier
# Public, Protected, private

class Modifier():
    a = 100
    b = 10000
    _c = 190
    __d = 1290

    print(_c)

    f = __d

print("----"*10)
class Test(Modifier):
    e = 2
    print(Modifier.a)
    print(Modifier._c)

obj = Test()
print(obj.b)    #Public, so accessed anywhere
print(obj._c)   # Protected, can be access through object

print("-----"*10)
obj1 = Modifier()
print(obj1.a)
print(obj1._c)
# print(obj1.__d)     # Private, so not accessed through class object as well.
print(obj1.f)       # as 'f' is public, it can access the private data through it.

# Task:
''' Secure Banking System (Multilevel Inheritance)
Design a system with three levels of inheritance: 
1. Class Account
-> Private data members: accountNumber, balance
-> Public methods: 
# setAccount() → input account number and balance
# deposit(amount) → add money
# getBalance() → return balance
# displayAccount() → show account number and balance

2. Class SavingsAccount (inherits from Account)
-> Private data member: interestRate
-> Public methods:
# setSavingsDetails() → input interest rate
# calculateInterest() → compute interest using balance; interest = balance * rate / 100
# displaySavings() → display all account + interest info

3. Class PremiumSavings (inherits from SavingsAccount)
-> Private data member: bonus
-> Public methods:
# setBonus() → input bonus amount
# calculateTotalBalance() → total = balance + interest + bonus
# displayPremiumDetails() → display full details
'''
class Account():
    # __accountNum = "12345"
    # __balance = 10000
    # accountnum = __accountNum
    
    def setAccount(self, accountNum, inBalance):
        __acc_name = accountNum
        __balance = inBalance

        self.name = __acc_name
        self.balance = __balance

    def deposit(self, amount):
        amount = amount + self.balance
        self.amount = amount
    
    def getBalance(self):
        return self.amount
    
    def displayAccount(self):
        return f'''--- Account Info ---
Account Number: {self.name}
Balance: {self.amount}
'''

class SavingsAccount(Account):
    def setSavingsDetails(self, interest):
        __interestRate = interest
        self.rate = __interestRate + 0

    def calculateInterest(self):
        inte = self.getBalance() * (self.rate/100)
        return inte
    
    def displaySavings(self):
        return f'''--- Savings Info --- 
Interests: {self.calculateInterest()}
'''
    
class PremiumSavings(SavingsAccount):

    def setBonus(self, bonus_amount):
        __bonus = bonus_amount
        self.bonuses = __bonus + 0

    def CalculateTotalBonus(self):
        self.total = self.getBalance() + self.calculateInterest() + self.bonuses
        self.amount = self.total
        return self.total

    def checkStatus(self):
        if self.total > 20000:
            return "VIP Customer"
        else:
            return "Regular Customer"

    def displayPremium(self):
        return f'''
{self.displayAccount()}
{self.displaySavings()}
--- Premium Info ---
Bonus is: {self.bonuses}
Total Balance: {self.CalculateTotalBonus()}

You are our {self.checkStatus()}
'''

accountm = input("Enter your account number?: ")
balances = int(input("Enter your initial balance?: "))
interestRate = int(input("Enter your interest rate?: "))
bonus_amt = int(input("Enter bonus amount?: "))

obj = PremiumSavings()

obj.setAccount(accountm, balances)
obj.deposit(1000)

obj.setSavingsDetails(interestRate)
obj.setBonus(bonus_amt)
obj.deposit(1000)

print(obj.displayPremium())
print(obj.getBalance())
# This is from 'a' mode from file handling.
# This is from 'a' mode from file handling.