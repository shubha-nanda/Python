import re
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="SYSTEM",
  database ="world"
  )

mycursor= mydb.cursor()



sql="insert into emailData(email,ename) values(%s,%s)"

name=input("enter your name ")
emailid=input("Enter email id  ")
matcher=re.search("[a-zA-Z0-9]@gmail.com$",emailid)
if matcher!=None:
    try:
        records=[(emailid,name)]
        mycursor.executemany(sql,records)
        mydb.commit()
        print("valid email",emailid)
    except mysql.connector.Error:
        print("email already exists. Try a new one")
else:
    print("invalid email")
