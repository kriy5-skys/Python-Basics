# Nested List
print("....."*10)
print("Nested list")
data = [1,2,3,4,5,[6,7,8,9,10]]
a =["Krishnaa"]

print(type(data))
print(data[-1][-1]) # To extract value from list inside list

data = [1, 2, 3, 4, 5, [6,7,8,9,10], "Krishnaa"]
print((data))
print(data[-1][-1])

a = "Krishnaa"
print(a[-3])  # Indexing and len() work in string as well

# Data type: Dictionary
print("....."*10)
print("Data type: Dictionary")

a = ["Krishnaa","Yagol",22, 920203]  # list
data = {
    "name":["Krishnaa","Yagol"],
    "age":22,
    "Number":12211,
    }
print(data)
print(type(data))

data = {
    "name":["Krishnaa","Yagol"],
    "age":22,
    "Number":12211,
    "name":"Krishnaa"
    } # If duplicate keys, then the 1st is replaced by the latest.

print("Length of the dictionary is: ",len(data))  # Shows the number of key-value pairs.

# in-built polymorphism: Like in len(), it works differently in list, string and dictionary data type.
# So, in-built polymorphism

print("....."*10)
print("Add operations in Dictionary") # only 2 ways
data = {
    "name":["Krishnaa","Yagol"],
    "age":22,
    "Number":12211,
    }
print(data)

data["age"] = 56  # Change 'age' key's value.
data["number1"] = 98737223  
# add key to the existing dict, even if the key doesnot exist in it.
print(data)

data.update(
    {"name":"kri","number1":9102,"address":"bagbazaar","age":25}
)  # updates multiple data at once
print(data)

# Functions in Dictionary
print("....."*10)
print("Funtions in Dictionary")

print("Indexing")
data1 = {'name': 'kri', 'age': 25, 'Number': 12211, 'number': 98737223, 'number1': 9102, 'address': 'bagbazaar'}
print(data1["age"])  # Indexing but must have key as index.
# Prints value of the given index (key)
# print(data1['nepal']) 
# //KeyError occurs as key doesnot exist, but not makes new key.

# data2 = {'name': 'kri', 'Number': 12211, 'number': 98737223, 'number1': 9102, 'address': 'bagbazaar'}
# print(data2['age'])  //KeyError
print("....."*10)
print("Keys and Values")
data1 = {'name': 'kri', 'age': 25, 'Number': 12211, 'number': 98737223, 'number1': 9102, 'address': 'bagbazaar'}
a = data1.keys()  # to list keys of the dictionary.
print(a,"\n")

print(type(a)) # Output: <class 'dict_keys'>
# print(a[0]) # TypeError occurs as this doesnot returns the value, and is not a list.
# So, requires typecasting.

print(data1.values())  # to list values of the dictionary.
b = list(data1.values())[0]
print(b)
print(list(data1.values())[0])  # Requires typecasting

# Delete operations in Dictionary
print("....."*10)
print("Delete Operations in Dictionary")

data1 = {'name': 'kri', 'age': 25, 'Number': 12211, 'number': 98737223, 'number1': 9102, 'address': 'bagbazaar'}
# del: to delete the key given.
del data1['age']
print(data1)

# pop(): to delete the key and value pair by giving the key.a
# Can store the popped data.
a = data1.pop('name')
print("\nPopped data is: ",a)

# popitem: delete last item
b = data1.popitem()
print("Pop_item data is: ", b)  #//last key-value deleted.
print(data1)

# clear: clear the dictionary into empty.
data1.clear()
print("The dictionary is cleared!!: ",data1)

data2 = {'name': 'kri', 'Number': 12211, 'number': 98737223, 'number1': 9102, 'address': 'bagbazaar'}
# print(data2['age'])

number = data2.get('numbers',"key not found")
num = data2.get('numbers')  # it shows nonetype
name = data2.get('name')

print(num, number, name)
print(type(num))  # As this is NoneType, it is required to have a msg to avoid error.
# Rather than NoneType, it is need to have msg 
# because NoneType creates more error.

# Nested Dictionary
print("....."*10)
print("Nested Dictionary")
data3 = {
    "phone":{
        "NTC":"98272",
        "Ncell":{
            "type": "Prepaid",
            "balance": 1233
        }
    }
}
print(data3)

# Single line output
print(f'The balance is: {data3['phone']['Ncell']['balance']}')

phone = data3['phone']
ncell = phone['Ncell']
balance = ncell['balance']
print(f'The balance is: {balance}')

# Task
print("....."*10)
print("Task")
user = {
    "name":"Hari",
    "phone":[
        {
            "type":"NTC",
            "number":"9844"
        },
        {
            "type":"NCELL",
            "number":"980"
        }
    ]
}

print(f'''
{user['name']} {user['phone'][1]['type']} number is {user['phone'][1]['number']}
{user['name']} {user['phone'][0]['type']} number is {user['phone'][0]['number']}
''')

name = user['name']
phone = user['phone']

Ncell = phone[1]
type1 = Ncell['type']
number1 = Ncell['number']

NTC = phone[0]
type2 = NTC['type']
number2 = NTC['number']

print(f'''
{name} {type1} number is {number1}.
{name} {type2} number is {number2}.
''')

# output
'''
Hari NCELL number is 980
Hari NTC number is 9844
'''