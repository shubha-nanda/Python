from math import sqrt
from sys import argv
class Sample:
    def __init__(self,value):
        self.C=50
        self.H=30
        self.value=value
          
    
    def getString(self):
        self.listone=[]
        for i in self.value:
            self.result=sqrt(2 * self.C * int(i)/self.H)
            self.listone.append(round(self.result))
        print((self.listone))
           

if __name__=='__main__':
    args=(argv[1:])
    val=args[0].split(',')
    print(args[0])
    print(type(args))
    print(type(val))
    obj=Sample(val)
    obj.getString()
    