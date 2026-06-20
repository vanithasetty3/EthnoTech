import mysql.connector as myconn
mydb=myconn.connect(
    host="localhost",
    user="root",
    password="Renuka@2001",
    database="ethnotech2"
)
mycursor=mydb.cursor()
mydbinsert="insert into t3(id,name,email)values(%s,%s,%s)"
mydblist=[(3,"laddu","skeleton@gmail.com"),(4,"vanitha","vanitha11@gmail.com"),(5,"gurl","gurl1908@gmail.com")]
mycursor.executemany(mydbinsert,mydblist)
mydb.commit()
print(mycursor.rowcount,"data inserted")
mycursor.execute("select * from t3")
for i in mycursor:
    print(i)