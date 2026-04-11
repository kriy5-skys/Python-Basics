'''
for i in <str, list, dict, range>  # no integer as multiple value required
    print(i)
'''
# Loop in String
for i in "Krishnaa":
    print(i)

# Loop in List
for i in [1,2,3,4,5,6,7,8,9]:
    print(i, end = " ")  # This gives 

# Loop in Dictionary
data = {'name': 'kri', 'number': 98737223, 'address': 'bagbazaar'}
for i in data:
    print(i)  # returns keys of the dictionary only.

for i in data.values():
    print(i)

# Printing both key-values pair
for i in data:
    print(f'{i} = {data[i]}')

for i in [1,2,3,4,5,6,7,8,9]:
    if i%2==0:
        print(f'{i} is even.')
    else:
        print(f'{i} is odd.')

# range(start,stop,step)
# range(1,100,1) and range(1,100) -> same

for i in range(100,10,-5):
    print(i)

for i in range(1,100,1):
    if i%2==0:
        print(f'{i} is even.')
    

# break: exits from the loop only
# continue: skips the part if the condition is true. Is required 


a = [1,2,"hello","test",1.2, "broadway"]

for i in a:
    # if type(i)== str:
    #   print(i)
    if not(isinstance(i,str)):
        continue
    print(i)

for i in a:
    pass
for i in a:...

# Nested Loop
for i in [1,2,3]:
    for j in [4,5]:
        print(i,j)

# Membership Operator
# in: membership operator

# Create a program that counts vowels in a string using a loop
a = "My name is Krishnaa Yagol"
vowels = [ "a","e","i","o","u"]
count = 0
for i in a:
    if i in vowels:
        count = count + 1
print(count)

# in; Membership operator