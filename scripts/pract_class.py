class Sample:
   '''This is sample class '''
   staticvar = "static"
   def __init__(self):
       self.a=10
       b=20
       print("inside constructor",b)
       
   def printFunc(self):
       self.c=100
       del self.a
       print("Method execution")


objectsample=Sample()
print(objectsample.__dict__)
objectsample.printFunc()
print(objectsample.__dict__)
print(Sample.staticvar)
print(objectsample.__dict__)

