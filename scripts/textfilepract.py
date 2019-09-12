with open("sample.txt","r",newline='') as f:
        data=f.readline()
        num_lines=0
        listone=[]
        for line in data:
            num_lines += 1
            
        print(num_lines)
        for i in  range(0,num_lines):
            value=f.readline()
            listone.append(value)
            print(value)
  

            