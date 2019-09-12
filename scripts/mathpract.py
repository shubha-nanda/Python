import math

number=list(range(200,320))
listone=[]
for i in number:
    if(((i%7)==0) and ((i%5)!=0)):
        listone.append(i)


print(listone)
