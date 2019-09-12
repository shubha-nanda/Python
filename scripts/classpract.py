class Sample:
    def __init__(self):
        self.strings=""
    
    def getString(self):
        self.strings=input()
        
    
    def printString(self):
        print(self.strings)
    

if __name__=='__main__':

    obj=Sample()
    obj.getString()
    obj.printString()
    