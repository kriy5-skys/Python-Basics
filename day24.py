# XAMPP

import mysql.connector
# db = mysql.connector.connect(
#     host = "localhost",
#     user = "root"
# ) 
#print(db)

# Here, port can also be defined, but our default port is 3306
#Like;
# db = mysql.connector.connect(
#     host = "localhost",
#     port = 3306,
#     user = "root"
# ) 
# print(db) # Gives the object

# In this, if we stop running the MySQL Database in the XAMPP managerOSx, then error occurs here.abs
# Error: _mysql_connector.MySQLInterfaceError: Can't connect to MySQL server on 'localhost:3306' (61)

# mysql.connector.connect: syntax to connect with the database server


# To connect python with database created in localhost
# db = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     database = "BroadwayPython"
# )
# print(db)

# If name written for database is wrong, then error.
# error:
# mysql.connector.errors.ProgrammingError: 1049 (42000): Unknown database 'BroadwayPythons'

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    database = "BroadwayPython"
)
print(db)
myterminal = db.cursor() # to open the editor panel of MySQL, where codes are written

# to insert, update
insert_query = "INSERT INTO ExchangeRate('date', 'iso3', 'name', 'unit', 'buy', 'sell') VALUES('2026-04-01', 'NEP', 'Nepal', '1', '150', '150');"
myterminal.execute(insert_query)  #To execute the given command to insert
db.commit()  # To insert into the database

