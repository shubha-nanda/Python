a=[int(i) for i in list(input().split(' '))]
count=0
b=[]
for i in a:
    if a.count(i) > 2:
            b.append(i)

print(a)
print(list(set(b)))