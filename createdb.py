import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",
    user="root",
    password="Renuka@2001"
)
print(mydb,"connected")
mycursor=mydb.cursor()
mycursor.execute("create database something")
print("db created successfully")