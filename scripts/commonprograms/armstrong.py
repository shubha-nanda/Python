
def armstrong(n):
    sum=0
    for i in n:
        val=i**len(n)
        sum=sum+val
 
    return sum

input_value=input()
n=[int(i) for i in input_value]

result=armstrong(n)

if result == int(input_value):
    print("armstrong")
else:
    print("not armstrong")
