import sqlite3

connection = sqlite3.connect("chinook.db")
# cursor =connection.execute("select * from employees")
# cursor =connection.execute("select FirstName,LastName,Title from employees where City= 'Lethbridge' or city= 'Edmonton'")
# for row in cursor :
#     print("*******")
#     print("FirstName = " + row[0])
#     print("LastName = " + row[1])
#     print("Title = " + row[2])
#     print("*******")

cursor =connection.execute(" select city from e "   )
for row in cursor :
    print("City = " + row )
    # print("Count = " +row))


