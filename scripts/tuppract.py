from sys import argv
class Tuppract:
    def __init__(self,value):
        self.values=value

    def displayList(self):
        print(self.values)
    
    def displaytuple(self):
        print(tuple(self.values))

if __name__=='__main__':
    args=(argv[1:])
    val=args[0].split(',')
    print(args[0])
    print(type(args))
    
    obj=Tuppract(val)
    obj.displayList()
    obj.displaytuple()