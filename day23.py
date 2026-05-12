# error handling
# It can only handle the errors defined in python, which is dynamic, and it doesnt handle user-defined error.

# Syntax except, can only be written once
# Though, except with the specific error as defined, can be written multiple times.abs

# Task: file handling, and error handling.
# to have 

try:
    a = 10
    print(b)
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

except NameError as e:
    with open("error.txt","a") as fi:
        fi.write(f"{e}")

except IndexError as l:
    with open("error.txt", "a") as fi:
        fi.write(f'{l}.\n')
except:
    print("try again")

fi.close()