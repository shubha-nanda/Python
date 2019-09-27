class Prime:
    def isPrime(self,var):
        self.var=var
        if (var<=1):
            return False
        
        for i in range(2,var):
            if(var%i==0):
                return False
           
        return True


if __name__ == '__main__':
    var=int(input())
    obj=Prime()
    result=obj.isPrime(var)
    print(result)

    
