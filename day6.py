print("Changing data through index")
# Changing data through index
data = [1,"testing, 3, 3, 5"]
print(data[0])
print(data)

#Changing with indexing:
data[0] = "changed"
print(data)

# Add Operations in List
# To add data in the list: 4 ways
print("....."*10)
print("Add Operations in List")
'''
append: add at last of the list
insert: add at any index with syntax: listname.insert(index, value)
extends: join two lists and not create new variable but just only joins.
concat: join two lists creating completely new variable.
'''

# Append
print("....."*10)
print("Append Operation")
a = [1,2,2,2,3,4,5]
print(a)
a.append(1)
a.append("testing")
print(a)

b = [] 
print(b)  # can be added in empty list
b.append("this is list")
print(b)

# Insert
print("....."*10)
print("Insert Operation")

data = ["hello","hi",1,2,3]
print(data)
data.insert(0,"1")
print(data)

data.insert(60,"new")
data.insert(59,"new1")      
#No matter what the data is stored at last if the index is not there
print(data)

# Extends
print("....."*10)
print("Extends Operation")
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

a.extend(b)
print(a)

b.extend(a)
print(b)

c = b.extend(a)
print(c)

# Concat
print("....."*10)
print("Concate Operation")
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = a + b
print(a, b)
print(c)

# Slicing
print("....."*10)
print("Slicing")
data = [1,2,3,4,5,6,7,8]
print(data)
print(data[2:4])
print(data[:4])
print(data[2:])

print(data[:])

c = data[1:]
print(c)

print(data[2:-5]) #no error though, but abnormal.

# Delete Operations in List
# To delete data in the list: 4 ways
print("....."*10)
print("Delete Operations in List")
'''
delete: delete the whole variable of list, and even index's value
remove: delete the value given to it
pop: in default, pop the last value, and even the index's value
clear: clears the list to make it empty list
'''

# Delete
print("....."*10)
print("Delete Operation")
data = [1,2,3,4,5,6,7,2,6]
#del data: deletes whole variable and list.
print(data)
del data[1]
print(data)

# Remove
print("....."*10)
print("Remove Operation")
data = [1,2,3,4,5,6,7,8,9]
print(data)
data.remove(2)  # to remove the value 2 in index 1.
print(data)

data = [1,2,3,4,5,6,7,2,8,9] #Only removes the first one, not both
print(data)
data.remove(2)  # does not work in duplicate values.
print(data)

# Pop
print("....."*10)
print("Pop Operation")
data = [1,2,3,4,5,6,7,8,9]
a = data.pop()
b = data.pop(0)  

print(data)
print(a,b)

# b = []
# b.pop()
# print(b)  This brings IndexError.

# Clear
print("....."*10)
print("Clear Operation")
data.clear()  # clear the list removing all values.
print(data)

# Other Methods:
print("....."*10)
print("Other Methods")

# Count
print("Count")
data = ["Kri","Jay","hari","Ya","Kri", "Kri"]
count_data = data.count("Kri")
print(count_data)

# Index
print("Index")
data = ["Kri","Jay","hari","Ya","Kri"]
print(data.index("Jay"))

# Reverse
print("Reverse")
data = ["Kri","Jay","hari","Ya","Kri"]
data.reverse()
print(data)

# Sort
print("Sort")
data = ["Kri","Jay","hari","Ya","Kri"]
data.sort()  # By default, ascending
print(data)

data.sort(reverse = True)  # Descending 
print(data)