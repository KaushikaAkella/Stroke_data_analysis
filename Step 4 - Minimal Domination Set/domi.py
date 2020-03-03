import pickle
with open('tx.txt','rb') as f:
    clus=pickle.load(f)
#for cl in clus:
    #print(cl)
import json
with open ('newwords.json','r') as json_data:
    data12=json.load(json_data)
#myclus=clus[1]
import networkx as nx
newdict={}
#for c in range(len(clus)):
myclus=clus[39]
G=nx.Graph()
for o in range(len(myclus)):
    for p in range(o+1,len(myclus)):
        if len(set(myclus[o]).intersection(set(myclus[p])))>= 1:
               G.add_edge(str(myclus[o]),str(myclus[p]))
               newdict.update({str(myclus[o]):myclus[o]})
               newdict.update({str(myclus[p]):myclus[p]})
        else:
            G.add_node(str(myclus[o]))
            G.add_node(str(myclus[p]))
            newdict.update({str(myclus[o]):myclus[o]})
            newdict.update({str(myclus[p]):myclus[p]})
#nx.draw(G)

print(str(G.number_of_edges()))

if(len(myclus)>1):
    my=list(nx.dominating_set(G))
    #print(my)
    print(G.degree(my))
support=[]

#with open("resultfinal.txt",'wb') as f:
    
for anode in my:
    for d in data12:
        if set(newdict[anode])==set(d['items']):
            print(d["items"],d["support"])
            #final.append(d["items"],d["support"],d["confidence"],d["lift]")
            support.append(d['support'])
            
print(1,': ',my)

#import matplotlib.pyplot as plt;
#plt.rcdefaults()
#import numpy as np
#import matplotlib.pyplot as plt
#objects=tuple(my)
#objects = ('excess hair','blood, harmone, test','100mg,clomid','milk, water','mood swing','carb, protein','bleed, irregular, period','eat, lose, weight','diagnosed, irregular period','birth control diagnosed','contracept pill','birth control period','diagnose excess hair')
#y_pos = np.arange(len(objects))
#support = [0.011615628299894404,0.00501583949313622,0.006599788806758183,0.004487856388595565,0.00501583949313622,0.004487856388595565,0.004223864836325237,0.00791974656810982,0.016103484688489968,0.010559662090813094,0.007391763463569166,0.012143611404435059,0.005279831045406547]
#plt.bar(y_pos, support, align='center', alpha=0.5)
#plt.xticks(rotation=90)
#plt.xticks(y_pos,objects)
#plt.ylabel('Support')
#plt.title('PCOS Results cluster 3')
#plt.show()

