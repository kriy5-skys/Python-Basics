# Dynamic Function:
# To change the variable, not static.

# When calling a function, you say the arguments,
# when the function is defined, it is called parameters.ab

# Positional arguments and keyword arguments
# Should pass the data as defined, i.e. if function has 3 parameters, then 3 arguments should be passed.abs
# In positional, the position of the parameters passed matter, 
# as if 3 is given in first parameter when the function is called, then, it is considered to be 1st variable.

def test(a,b,c):
    return a

print(test("Krishnaa",1,2))  # As in this function, the 1st argument is "Krishnaa", it is stored in variable 'a'.

# Any data type could be passsed in the parameters, or arguments.

def sum_data(a,b,c):
    return a+b+c

print(sum_data(1,2,3))
print(sum_data(1,23,43))

def add_list(data):
    ad = 0
    for i in data:
        ad = ad + i
    return ad

print(add_list([1,2,3,4,5,6]))
print(add_list([]))
print(add_list([438,342,23,23,23]))

# Drawback of positional arguments:
# It is just about the position, that when 1st parameter is always considered in 1st argument, and followed by others.

# This is solved by the keyword argument.

# Key argument: It is only used when the function is called, every other thing is same.
# It just explicitly defines the parameters' name in the function call, when arguments are passed.

# Extra keyword

def user_info(fname, lname):
    data = f'fname is {fname} and lname is {lname}'
    return data

print(user_info("Yagol","Krishnaa"))  # Here as fname is printed as Yagol, this is wrong.and
# But using keyword arguments,
print(user_info(lname="Yagol",fname = " Krishnaa"))

# Task:

'''
1 positional args
str/ check the value is string or not, if not a string, throw error

if string
count vowel letter
'''

def count_vowel(word):
    global letters
    letters = ["a","e","i","o","u"]
    count = 0
    if not(isinstance(word, str)):
        return "WRONG INPUT"
    word = word.lower()
    for i in word.lower():
        if i in letters:
            count = count + 1
    return count

print(count_vowel("AAA"))  # Should consider the error for Capitalization also.
print(count_vowel(1))
    
# a = "krishnaa"
# for i in a:
#     print(i)


# Sir's Code
# def count_vowe(word):
#     if isinstance(word, str):
#         count = 0
#         word = word.lower()
#         for i in word:
#             if i in letters:
#                 count = count + 1
#         return count
#     else:
#         return "WRONG INPUT! Not a String."

# print(count_vowe("AAA"))  # Should consider the error for Capitalization also.
# print(count_vowe(1))

# Default Argument
# In this, the variable has a defined value when the function is defined, like in parameters only.abs

# Example:

def user_info(fname, lname = "Yagol"):
    data = f'fname is {fname} and lname is {lname}'
    return data

print(user_info("Krishnaa"))  
# If the 'lname' argument is not written, then the default argument is printed automatically.

print(user_info("Sam",lname="Shrestha"))
# If the 'lname' argument is written, then the default argument is not printed, 
# but the given value is printed.


# print(user_info(lname="Yagol", "Krishnaa"))
# Error occurs as: Positional argument follows keyword argument.


# Arbitrary Positional Arguments (* args)
# Multiple data/values can be stored in a single parameter/variable.
# When function is defined, the parameter should contain "*" in its variable.abs
# The values are stored in a tuple.

# Arbitrary Keyword Arguments: (** kwargs)
# Multiple data/values can be stored in a single parameter/variable, and defined using a new parameter.
# When function is defined, the parameter should contain "**" in its variable.
# The values are stored in a dictionary.

def sum_num(*args):
    add = 0
    for i in args:
        add = add + i
    return add

print(sum_num(1))
print(sum_num(1,2,3,4,5))

print(sum_num(1,23,23))

def test_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(kwargs['address'])

test_kwargs(name = "Krishnaa",address = "Nepal")
