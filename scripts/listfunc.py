listone=["Balaiah","sky","Venkatesh","Chiranjeevi"]
vowels=["a","e","i","o","u"]
result=[]
count=0
countvalue=tuple((k for k in listone for l in k if l in vowels))

count=0
print((countvalue))
abc=set(countvalue)
print(abc)

for i in abc:
    print("for", i,"in List the count is ", countvalue.count(i))

print(type(countvalue))

s={}
print(type(s))