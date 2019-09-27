class Fibnocci:
    def isFib(self,var):
        self.var=var
        a = 0
        b = 1
        if var==0:
            return a
        elif var==1:
            return b
        else:
            for i in range(2,var):
                c=a+b
                a=b
                b=c
        
        return b
                       
if __name__ == '__main__':
    var=int(input())
    obj=Fibnocci()
    result=obj.isFib(var)
    print(result)

    
