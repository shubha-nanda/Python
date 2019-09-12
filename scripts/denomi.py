
def coin_denominations(denominations, amount):
   denomi = denominations
   amt= amount
   max_num=max(denomi)
   min_num=min(denomi)
   listone=[]
   if amt in denomi:
       return 1
             
   elif amt>max_num:
        for i in denomi:
            if amt%i==0:
                listone.append(int(amt/i))
        return min(listone)
        
        
        a=int(amt/max_num)
        diff=int(amt%max_num)
        if diff == 0:
            return a                          
        else:
            if diff in denomi:
                return a+1
                
            else:
                var= coin_denominations(denomi,diff)
                return a+var  
            
   elif(amt>min_num and amt<denomi[1]):
        val=int(amt/min_num)
        diff=int(amt%min_num)
        if diff == 0:
            return val                          
        else:
            if diff in denomi:
                return val+1
                
            else:
                var= coin_denominations(denomi,diff)
                return val+var  
       
   elif(amt>denomi[1] and amt<max_num):
        val=int(amt/denomi[1])
        diff=int(amt%denomi[1])
        if diff == 0:
            return val                          
        else:
            if diff in denomi:
                return val+1
                
            else:
                var= coin_denominations(denomi,diff)
                return val+var  
    
   else:
        return 0              



  
  # IMPORTANT:
  # 1. Write your solution in this function
  # 2. Do not make changes to the function signature
  # 3. Use the 'pip-install' command in the IDE, to install any requirements. This takes a few seconds.
  # 4. Use the 'run' command in the IDE, to run the main method. You can also invoke the main method from the terminal.
  # 5. Use the 'run-tests' command in the IDE, to run unit tests. The 'pip-install' command must be run before this.
    


def main():
  denominations =[1, 5, 7]
  amount = 11
  no_of_coins = coin_denominations(denominations, amount)
  message = 'Given coins of denominations {0}, no of coins used to create change for amount {1} is {2}\n'.format(
    denominations, amount, no_of_coins)
  print(message)


if __name__ == '__main__':
  main()
