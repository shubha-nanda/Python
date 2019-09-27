import collections 
  
# initializing deque 
de = collections.deque([1,2,3,4,5]) 

n=int(input())
de.rotate(-n)
for i in de:
    if(i!=n):
        print(i,end=" ")
           

            