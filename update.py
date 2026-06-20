import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",
    user="root",
    password="Renuka@2001",
    database="ethnotech2"
)
mycursor=mydb.cursor()
#mydbupdate="update t3 set name='leo'where id=1" update single data
mydbinsert="update t3 set name=%s where id=%s"  #update multiple data
mydbdata=[('a',2),('b',3),('c',4),('d',5)]
mycursor.executemany(mydbinsert,mydbdata)
mydb.commit()
mycursor.execute("select * from t3")
for i in mycursor:
    print(i)