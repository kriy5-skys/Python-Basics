print("Data types")
a = 2
print(type(a))

a = "Kri"
print("type is: ", type(a))  # string can be in both single or double quote

a = "testing"
print(type(a))

a = 3.918282828
print(type(a))

# Multi-line String
b = '''
Hello, My name is Krishnaa Yagol
'''
print(b)

a = 1.1
print("type is: ", type(a))

a = True
a = False   # or can be written as 1 or 0
print("type is: ", type(a))

a = 2 + 3j
print("type is: ", type(a))

a = None  # NoneType: doesnot take memory space
print(type(a))
a = ""  # Empty string: takes memory space
print("type is: ", type(a))

# Arithmetic operators
print("........" * 10)
print("Arithmetic Operators")
a = 10
b = 3
print("Addition is:", a + b)
print("Subtraction is:", a - b)
print("Multiplication is:", a * b)
print("Division is:", a / b)

print("Floor Division is:", a // b)  
# floor division: returns lowest whole number

print("Modulus Division is:", a % b)  # modulus; returns remainder
print("Exponentiation is:", a**b)  # exponentiation: a takes power of b

# String
print("........" * 10)
print("For Strings")
a = "Kri"
b = "shnaa"

print(a + b)  # String Concatenate

''' TASK '''
name = "Hari"
surname = "Sharma"
space = " "  # Output should be Hari Sharma

'''Solution'''
print(name + space + surname)
print(name + " " + surname)

# String multiplication
print("........" * 10)
name = "Kri"
value = 4
print(name * value)  # Cannot multiply string to string


# Type casting: to convert the data type of the variables
a = "10"
b = int(a)
print(type(a))
print(type(b))

a = 100 
b = str(a)
print(str(a))
print(type(a))
print(type(b))

# Like, a = ""what is this?"", is it string: "what is this?" or string: what is this?
# Answer: as it is already string, it doesnot come in four quotations, 
# remains string after typecast too

a = "1.25"
print(a)
print(type(a))
print(type(float(a)))

a = 1.23
b = int(a)  #Here, it changes but excludes the decimal point.
print("Change from float as", a,"to integer:",b)
print(type(a),type(b))

# a = "1.21"
# b = int(a)
# print(type(b)) #ValueError

a = 1
print(type(a))
b = bool(a)  # 0 or 1 are also considered boolean expressions
print(type(b))

# isinstance
print("........" * 10)
print("ISINSTANCE Function")
print(isinstance(10, str))  # isinstance: to check the data type; returns true or false
print(isinstance("20", str))

print(isinstance(1, float))
