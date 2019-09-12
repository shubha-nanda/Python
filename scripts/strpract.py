from sys import argv
class StringPract:
    
    def disp(self,*n):
        product=1
        listone=[]
        for n1 in n:
            product=product*n1
            listone.append(product)



 

obj=StringPract()
obj.disp(10,20)
obj.disp(10)
obj.disp(10)
print(obj.disp.listone)
