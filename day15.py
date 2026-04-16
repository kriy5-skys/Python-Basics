a, b = 1, 100

# Also, this can be used when the function is called.

# Palindrome: Reverse.

# Passing arguments:
# Hierarchy: Positional, Arbitrary positional, Arbitrary keyword

def testargs(a, *args, **kwargs):
    return a, args, kwargs

print(testargs(1,2222,22,2,2,2,2,2,name = "Krishnaa", address = "Nepal"))

# But if we dont pass args then, it becomes empty.
# Also, if we dont pass 'a' then, it occurs error.

print(testargs(1,name = "Krishnaa", address = "Nepal"))

# print(testargs(name = "Kri", address = "Nepal"))

# Bill Task
'''
Takes multiple food prices (`*args`)
Takes extra details like tax and service charge (`**kwargs`)
Returns total bill
'''

def bill(*args, **kwargs):
    total = 0
    for i in args:
        total= total + i
    
    for j in kwargs.values():
        if isinstance(j, (int,float)):
            total += j
    
    return total

print(bill(560, 340, 120, 350, tax = "13%", service_charge = 105))



# Class and Objects
# Class: It is like a 
# Constructor: doesnot require return.
# In python, the constructor is "__init__" method.








