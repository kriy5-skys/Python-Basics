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
print("-----"*10)
def bill(*args, **kwargs):
    total = 0
    for i in args:
        total= total + i
    
    for j in kwargs.values():
        if isinstance(j, (int,float)):
            total += j
    
    return total

print(bill(560, 340, 120, 350, tax = "13%", service_charge = 105))

'''
Write a function that:
Accepts numbers (*args)
Accepts operation type (**kwargs, e.g., operation="sum" or "multiply")
'''
print("-----"*10)
print("Operations are addition, multiply?: ")
def test_num(* args, **kwargs):
    for i in kwargs.values():
        if i == "addition":
            add = 0
            for j in args:
                add += j
            return add
        elif i == "multiply":
            mul = 1
            for j in args:
                mul *= j
            return mul
    
print(test_num(1,2,3,4,5,operation = "addition"))
print(test_num(1,2,3,9,operation = "multiply"))

''' 
12. Delivery System

Function should:
* Take multiple items (*args)
* Take delivery info (**kwargs: address, phone, priority)

Challenge:
* If priority="high", add extra charge.
'''
def delivery_system(*args, **kwargs):
    li = []
    total_charge = 0
    for i in args:
        li.append(i)
    print(list(kwargs.values()))
    return(li)

print(delivery_system(1,23,23,7, priority = "high"))

# Class and Objects
# Class: It is like a 
# Constructor: doesnot require return.
# In python, the constructor is "__init__" method.








