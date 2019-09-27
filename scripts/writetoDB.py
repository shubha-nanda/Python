import mysql.connector
import csv
with open ("samplecsvv.csv","r",newline='') as f:
    w=csv.reader(f)
    data=list(w)
  
mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="SYSTEM",
    database="world"
)

mycorsor=mydb.cursor()

sql="insert into employee(Ename, Eid, ECompany) VALUES(%s, %s, %s)"
mycorsor.executemany(sql,data)
mydb.commit()

mycorsor.execute("select * from employee") 
print(mycorsor.fetchall())
