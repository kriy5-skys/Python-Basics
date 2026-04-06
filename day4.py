# Comparison Operators
print("Comparison Operators")
print("........."*10)
a = 12
b = 10

print("a == b is:", a == b)  # equal to
print("a != b is:", a != b)  # not equal to
print("a > b is:", a > b)    # greater than
print("a < b is:", a < b)    # less than
print("a >= b is:", a >= b)  # greater than or equal to
print("a <= b is:", a <= b)  # less than or equal to

a = "String"
b = 5

print("string == integer is:", a == b)
print("string != integer is:", a != b)
# print(a<=b)
# If we compare this with greater or less than, typeError occurs

# Logical Operators
# AND OR NOT
print("Logical Operators")
print("AND OR NOT")
print("........."*10)

age = 21
citizen = True
print(age >= 18 and citizen)  # True

a = True
b = False

print(a or b)  # True

a = "Krishnaa"
b = "Yagol"
print(not (a == b))
# a==b is false, but not false: true

# INPUT Function
print("........." * 10)
print("INPUT FUNCTION")
# Here, In this function, the type is always string,
# so typecasting needed

# a = input("Enter a number:")
# b = input("Enter another number:")
# print("Add: ", int(a) + int(b))

# If string entered, then error after the entry only.
# So, regarding typecast at start.
# Here, error is handled after the input only which will be string.

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print("Add: ", a + b)
# Here, error is handled during the input only,
# as input will directly be integer.

# String Formatting
print("........." * 10)
print("String Formatting")

name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")

# As we use, print("My name is " + name + " and my age is " + age +
# " and i live in " + address), but easy version is using: f-string.

output = f"My name is {name} and my age is {age} and I live in {address}."
print(output)

# Conditional Statement
print("........." * 10)
print("Conditional Statement")

"""
Syntax
if(condition):
    this runs if condition is true
else:   (cannot have any conditions)
    This runs if condition is false
"""

if 1 == 1 and 2 == 2:
    print("data")
    print("I am inside the if block")
else:
    print("I am in the else condition")

print("I am outside if block in overall.")

# Even or Odd Program
n = int(input("Enter a number: "))  # typecasted
if n % 2 == 0:
    print(f"Number {n} is even.")
else:
    print(f"Number {n} is odd.")
