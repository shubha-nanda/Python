a=10
b=20
def swapp(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a, b
a,b=swapp(a,b)

print(a,b)