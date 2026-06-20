import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",
    user="root",
    password="Renuka@2001",
    database="ethnotech2"
)
mycursor=mydb.cursor()

mycursor.execute("show tables")
for i in mycursor:
    print(i)