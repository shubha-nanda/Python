class bureaucrat:
    def __init__(self,name,grade):
       self.name=name
       self.grade=grade
    

 

x,y = input("Enter 3 float numbers :").split(' ')
print("{p.name} grade: {p.grade}".format(p=bureaucrat(x,y)))
