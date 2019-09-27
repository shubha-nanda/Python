x=int(input())
arr=[1,2,3,4,5,6]
n=len(arr)

def linearSearch(arr,n):
    for i in range(0,n):
        if arr[i]==x:
            return i
    return -1

result=linearSearch(arr,n)
print(result)