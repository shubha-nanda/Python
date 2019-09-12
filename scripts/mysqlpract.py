import mysql.connector
import csv

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="SYSTEM",
  database ="sakila"
  )
mycursor = mydb.cursor()

mycursor.execute("select * from city ")

with open("citycsvtwo.csv","w",newline='') as f:
   w=csv.writer(f) 
   w.writerow(["city_id","city","country_id","last_update"])# returns csv writer object
   for x in mycursor:
       w.writerow(x)