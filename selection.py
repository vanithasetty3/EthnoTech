import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",
    user="root",
    password="Renuka@2001",
    database="ethnotech2"
)
mycursor=mydb.cursor()
mycursor.execute("select * from t3")
for i in mycursor.fetchmany(2):
    print(i)