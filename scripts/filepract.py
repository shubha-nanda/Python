import csv
with open ("samplecsvv.csv","w+",newline='') as f:
    w=csv.writer(f)
    a=[["ename","EmpID","Ecompany"]]
    w.writerows(a)
    n=int(input("Enter Number of Employees:"))
    b=[]

    for i in range(n):
        print("enter employee name,id ,company")
        ename=string(int(input()))
        eid=input()
        ecompany=input()
        t=ename,eid,ecompany
        b.append(t)

with open ("samplecsvv.csv","a",newline='') as f:
    w=csv.writer(f)       
    w.writerows(b)     

print(b)


with open ("samplecsvv.csv","r",newline='') as f:
    w=csv.reader(f)       
    data=list(w)
    

print(data)
for i in data:
    print(i)


   
print("writing done")


