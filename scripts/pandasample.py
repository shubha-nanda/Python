import pandas as pd
import csv
# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']
lsttw = ['asdfa', 'dsfas', 'dsf', 'fds', 
            '5', '6', '7']
tw = ('1', '3', '4', '34', 
            '5', '6', '7')

data = {'Name':['Tom', 'nick', 'krish', 'jack'],
        'Age':[20, 21, 19, 18]}           

 
# Calling DataFrame constructor on list
df = pd.DataFrame(data)
print(df)

with open("emp.csv","w",newline='') as f:
   w=csv.writer(f)
   for i in df:
          w.writerow(df)