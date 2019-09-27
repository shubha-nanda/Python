input_string=str(input())
listone=list(str(input_string))

d={}
for i in listone:
    if i in d.keys():
        d[i]=d[i]+1
    else:
        d[i]=1

for i in d.keys():
    if d[i] >1:
        print(i ,":", d[i])

    