import mysql.connector
import csv

mydb=mysql.connector.connect(
    host="localhost",
    username="root",
    password="SYSTEM",
    database="world"
)

mycorsor=mydb.cursor()

# sql="insert into employee(Ename, Eid, ECompany) VALUES(%s, %s, %s)"
# mycorsor.executemany(sql,data)
# mydb.commit()

mycorsor.execute("SELECT id,email, ename FROM emailData where Indicator='Y' LIMIT 10") 

data=mycorsor.fetchall()
print(data)
Message_ID=[]
Message_Data=[]
for row in data:
    print("ID:",row[0])
    Message_ID.append(row[0])
    Message_Data.append(row[1])


print(Message_ID)
print(Message_Data)



with open("email.csv","w",newline='') as f:
   w=csv.writer(f) # returns csv writer object
   w.writerow(["Email"])
   n=len(Message_Data)
   for i in range(n):
        emaild=Message_Data[i]
        w.writerow([emaild])

   print("Total Employees data written to csv file successfully")



Message_I=[1]
# for i in Message_ID:\
mycorsor.execute("UPDATE emailData SET Indicator = 'N' WHERE id = %s",(1,))
mydb.commit()

data=mycorsor.fetchall()
print(data) 