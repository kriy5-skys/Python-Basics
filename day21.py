# # File Handling
# # To handle any file

# # Reading file: It prints everything in the mentioned file.
# f = open('day20.py','r')
# print(f.read())

# # Writing file: It overwrites to the given command, if the file exists.
# # f = open('task1.py','w')
# # f.write("This is from 'w' mode from file handling.")
# # f.close() # If you open file to write, you need to close it.

# # Append file: It adds the given command, for the exisiting filr
# f = open('day20.py','a')
# f.write("This is from 'a' mode from file handling.")
# f.close()

# # In both 'w', and 'a', if the file does not exist, then it creates new file.

# f = open('test.txt','w')
# f.write("This is a new file from 'w' mode in file handling.")
# f.close()

import csv

# with open("data.csv", "r") as file:
#     reader = csv.reader(file)
#     print(reader)
#     for index,row in enumerate(reader):
#         print(index+1,row)

a = {}
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)

print(a)


