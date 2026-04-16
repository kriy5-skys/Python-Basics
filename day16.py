class Test():
    b = 12
    a = 123

obj = Test()
obj.data = "This is obj attributes."

obj1 = Test()
obj1.data = "Obj1 attributes"

obj2 = Test()

print(obj1 == obj2)
print(obj)
print(obj1)
print(obj2)

print(obj.data)
print(obj1.data)


# Accessing class attributes
print("-----"*10)
print(obj1.a)
print(obj2.b)

# class Math():
#     a = 124
#     b = 12
#     def add():    # If parameter for the function is not defined, then TypeError occurs for positional argument.
#         return a + b  # as the function is not able to access the class attribute

#     def sub():
#         return a - b

# obj = Math()
# print(obj.add()) # TypeError: Math.add() takes 0 positional arguments but 1 was given

# For the function to be able to access class attribute, 
# we define a parameter in it that is, "self" (most common)

class Math():
    a = 124
    b = 12
    def add(self):    
        return self.a + self.b 

    def sub(self):
        return self.a - self.b

obj = Math()
print(obj.add())
print(obj.sub())

# Function Call
print("-----"*10)
class Math():
    a = 124
    b = 12
    def add(self):    #"self" is the instance to access other attributes and other function not defined in it.
        return self.a + self.b 

    def sub(self):
        return self.a - self.b
    def result(sel):
        return {
            "add": sel.add(),
            "subtract": sel.sub()
        }
    

obj = Math()
print(obj.result())

# Process: 
# 1st the program comes in line 68 as class is called through object.
# Then, line 69, where it call class Math then it's function "result"
# then the result calls the function add() first, 
# and mind (this is accessed within this "result" function only if we access it defining "self") 
# then the add() takes the class attributes a,b and then, return the statement to "result"

# When object is called, the class firstly only gives the memory place as output.
# Like, <__main__.Test object at 0x1008e0690>
# But to avoid this as output, we define __str__(self) function inside the class, which runs automatically, when the class is called through object.

print("-----"*10)
class StringTest():
    data = "Hi!, Krishnaa"

    def __str__(self):
        return f'{self.data}! This is from str function.'

onj = StringTest()
print(onj)

print("-----"*10)
class ConstTest():
    data = "Testing for Constructor."

    def __init__(self,a,b,c):
        print(f'This is from constructor, {a}')
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        print(self.a + self.b + self.c)

obj = ConstTest(1,2,3)
obj.add()

# Here, a , b and c are only limited to constructor only.

