import csv
with open ("samplecsvv.csv","r",newline='') as f:
    w=csv.reader(f,delimiter=':', quoting=csv.QUOTE_NONE)       
    data=list(w)
    print(data)