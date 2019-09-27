a=[4,5,6,7,8,9]
key=5

def binarysearch(low,high,key):
    low=low
    high=high
    key=key
    mid=int((low+high)/2)
    if (key < a[mid]):
        high=mid-1
        return binarysearch(low,high,key)
    
    elif(key>a[mid]):
        low=mid+1
        return binarysearch(low,high,key)
    
    elif(key==a[mid]):
        return mid
      

result=binarysearch(0,len(a)-1,key)
if (result==-1):
    print ("element not found")

else:
    print(result)



            