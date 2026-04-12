# Tuples, e.g. (1,2,3,4,5)
print("------"*10)
print("Data Type: Tuples")
a = (1, 2, 3, 4, 5, 6)
print(type(a))

print(a)

# a[0] = 100  //Cannot be changed as tuples.
# print(a) //TypeError occurs.

# Type casting:
b = list(a)
b[0] = 100
print(b)

a = tuple(b)
print(a)

# Duplicates:
data = ("Kri","Kri",1,1,2,2)
print(data)
print(type(data))
print(data[0])

# Set
print("------"*10)
print("Data Type: Set")
data = {1,2,1,2,3,2,1,"hello","hi","hello"}
print(data)
print(type(data))

# To remove duplicate data from list, we typecast to "set" and back to list.
li = [1,2,1,2,3,2,1,"hello","hi","hello"]
print(li)
a = set(li)
print(a)
print(type(a))
li = list(a)
print(li)
print(type(li))

# Function
print("------"*10)
print("Function")
def test(): 
    print("This is testing")
    return 1

# When you don't return anything, just "return" then None comes,
# and if there is no "return" explicitly written, then also None comes.

def test1(): 
    print("This is testing")
    return

test()
print(test())
print(test1())

def plus():
    a = 100
    b = 2
    add = a + b
    return add, a, b  #This has the output returned in tuple.
    return (add, a, b)  #this is not the same as above, but single data entry only, not multiple.

print(plus())

def plus1():
    a = 100
    b = 2
    add = a + b
    return (add, a, b)

print(plus1())  # This is single data only.

def add_list():
    a = [1,2,3,4,5,6]
    ad = 0
    for i in a:
        ad = ad + i
    return ad

print(add_list())