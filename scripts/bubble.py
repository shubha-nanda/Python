# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product
a=[int(i) for i in list(input().split(' '))]

print(a)
def swapp(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a, b

x=[]

count=0
for i in range(0,len(a)-1):
           if a[i] > a[i+1]:
                        count=count+1
                        m=a[i]
                        n=a[i+1]
                        m,n=swapp(m,n)
                        a.pop(i)
                        a.insert(i,m)
                        a.pop(i+1)
                        a.insert(i+1,n)


print(a)
print(count)
                







