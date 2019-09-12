import pandas as pd
import numpy as np
from xml.dom import minidom
import csv 
import xmltodict
import json
# df = pd.read_csv('.\Orders.csv', low_memory=False, verbose=1)
# json_value=df.to_json(orient='table',index=False)
# json_loads=json.loads(json_value)
# print(json.dumps(json_loads, indent=4, sort_keys=True))

mydoc = minidom.parse('.\sample.xml')

items = mydoc.getElementsByTagName('country')
for elem in items:
    #xmls= mydoc.getElementsByTagName('')
    if elem.attributes['name'].value == "UK1" :
        print(True)
    else:
        print(False)
    
e = ''
result = xmltodict.parse(e)
print(result)