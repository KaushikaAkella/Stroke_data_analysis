import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import simplejson as json

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

#dataset = pd.read_csv('H://tocsvdata.csv',error_bad_lines = False)
#row_count = sum(1 for row in dataset)
#col_count = sum(1 for column in dataset)
 
#print(row_count,col_count)
#row_count=row_count-1;
#col_count=col_count-1;
data1 = []
data=[]
import csv
with open('out.csv','r',encoding='utf-8') as f:
    rdr = csv.reader(f)
    data1 = list(rdr)

for d in data1:
    data.append(list(set(d)- {''}))
print(data[0])
#for row in range(0,):
 #   print(data)
  #  data.append([str(dataset.values[row,col]) for col in range(0,1555)])
    
from apyori import apriori
rules = apriori(data, min_support = 0.0028,min_confidence = 0.0028,min_length=1)
print(rules)
results = list(rules)
print(len(results))

import apyori
output=[]
f = open("newwords.json","w")
for RelationRecord in results:
        #o=StringIO()
    #print("in")
    apyori.dump_as_json(RelationRecord,f)
    #output.append(json.loads(f.getvalue()))
#data_df = pd.DataFrame(output)

f.close()
#print(output)

#print(results)

"""f = open("results.txt",'w',encoding='utf-8')
for i in results:
    f.write(str(i))
    f.write("\n")
    #print(str(i))
f.close()"""
