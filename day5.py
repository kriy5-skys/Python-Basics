# IF...ELSE Condition

if (1 == 1):
    print("This is true")
else:
    print("False")

if (True):
    print("This is true")
else:
    print("False")
# else condition is not reached as condition is written as True.

# IF..ELIF..ELSE Condition
'''Example of IF...ELIF Condition'''
''' TASK '''
print("....."*10)
print("IF..ELIF..ELSE Condition")
gpa = float(input("Enter your GPA?: "))

if (gpa > 3.6 and gpa <= 4.0):
    print("Congratulations! You have got an A+.")
elif (gpa > 3.2 and gpa <= 3.6):
    print("Congratulations! You have got an A.")
elif (gpa > 2.8 and gpa <= 3.2):
    print("Congratulations! You have got a B+.")
elif (2.0 <= gpa < 2.4):  # Range in conditions as given also work.
    print("Congratulations! You have got a B.")
elif (gpa > 2.0 and gpa <= 2.4):
    print("Congratulations! You have got a C+.")
elif (gpa > 1.6 and gpa <= 2.0):
    print("Congratulations! You have got a C.")
elif (gpa > 0.8 and gpa <= 1.6):
    print("Congratulations! You have got a D.")
elif (gpa > 0 and gpa <= 0.8):
    print("Sorry! You have got an E and have failed SEE.")
else:
    print("It is an invalid grade for the system.")

# NESTED IF...ELSE Condition
'''Example of NESTED IF Condition'''
''' TASK '''
print("....."*10)
print("NESTED IF...ELSE Condition")
gpa = float(input("Enter your GPA?: "))

if (gpa > 3.6 and gpa <= 4.0):
    print("Congratulations! You have got an A+.")

    if gpa == 4.0:
        print("You are a Nepal Topper.")
    elif gpa == 3.61:
        print("So lucky with getting an A+.")
    elif gpa > 3.65 and gpa <= 3.8:
        print("Good job!")

elif (gpa > 3.2 and gpa <= 3.6):
    print("Congratulations! You have got an A.")
elif (gpa > 2.8 and gpa <= 3.2):
    print("Congratulations! You have got a B+.")
elif (gpa > 2.4 and gpa <= 2.0):
    print("Congratulations! You have got a B.")
elif (gpa > 2.0 and gpa <= 2.4):
    print("Congratulations! You have got a C+.")
elif (gpa > 1.6 and gpa <= 2.0):
    print("Congratulations! You have got a C.")
elif (gpa > 0.8 and gpa <= 1.6):
    print("Congratulations! You have got a D.")
elif (gpa > 0 and gpa <= 0.8):
    print("Sorry! You have got an E and have failed SEE.")
else:
    print("It is an invalid grade for the system.")

'''Example of IF...ELIF Condition'''
'''TASK done by Sir: Percentage with Divisions.'''

print("....."*10)
print("To check from which division the user is passed.")

percent = float(input("Enter your percentage: "))

if (percent >= 80 and percent <= 100):
    print(f'''Congratulations! As your percentage is {percent}%.
You have got a Distinction.''')
elif (percent >= 60 and percent < 80):
    print(f'''Congratulations! As your percentage is {percent}%.
You have got a First Division.''')
elif (percent >= 50 and percent < 60):
    print(f'''Congratulations! As your percentage is {percent}%.
You have got a Second Division.''')
elif (percent >= 40 and percent < 50):
    print(f'''Congratulations! As your percentage is {percent}%.
You have got a Third Division.''')
elif (percent > 0 and percent < 40):
    print(f'''As your percentage is {percent}%. You are FAILED.''')
else:
    print("Invalid Percentage Given.")

'''Example of NESTED IF Condition'''
'''TASK done by Sir: Percentage with Divisions.'''
print("....."*10)
print("Checking from which division the user is passed using Nested IF.")

maths = int(input("Enter marks of MATHS: "))
science = int(input("Enter marks of SCIENCE: "))
english = int(input("Enter marks of ENGLIGH: "))
nepali = int(input("Enter marks of NEPALI: "))

if (maths > 100 or science > 100 or english > 100 or nepali > 100):
    print("Marks should not be more than 100 as full mark is 100.")
else:
    total = maths + science + english + nepali
    percent = (total / 400) * 100
    if (percent >= 80):
        print(f'''Congratulations! As your percentage is {percent}%.
You have got a Distinction.''')
    elif (percent >= 60 and percent < 80):
        print(f'''Congratulations! As your percentage is {percent}%.
You have got a First Division.''')
    elif (percent >= 50 and percent < 60):
        print(f'''Congratulations! As your percentage is {percent}%.
You have got a Second Division.''')
    elif (percent >= 40 and percent < 50):
        print(f'''Congratulations! As your percentage is {percent}%.
You have got a Third Division.''')
    elif (percent > 0 and percent < 40):
        print(f'''As your percentage is {percent}%. You are FAILED.''')
    else:
        print("Invalid result")

# Single Line IF Condition
print("....."*10)
print("Single Line IF condition")

gender = "M"
if gender == "M":
    print("Male")
else:
    print("Female")

data = "Male" if gender == "M" else "Female"
print(data)

# LIST
print("....."*10)
print("LIST")

data = [1, 2, 3, 3, 5]
print(data)

print("....."*10)
print("Positive Indexing")
# Positive Indexing
print(data[0])
print(data[3])
a = data[1]
print(a)

# print(data[6]); 
# In above eg, as 6 is not within range, IndexError
print("....."*10)
print("Negative Indexing")
# Negative Indexing
print(data[-3])
print(data[-5])
print(data[-1]) #start from last

print("....."*10)
print("Negative Zero")
print(data[-0]) 
# returns first as zero is neither +ve nor -ve.

print("....."*10)
print("")
data = []  # empty list
print("Type is: ",type(data))

data = [1, "testing", 3, 3, 5, 9]
print(data)
print(len(data))
print(data[1])
