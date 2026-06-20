import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",
    user="root",
    password="Renuka@2001"
)
print(mydb,"connected")


mycursor=mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)

