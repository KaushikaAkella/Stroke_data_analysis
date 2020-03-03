hyperg={}
allwords=[]
import nltk
from nltk.tokenize import word_tokenize

listofnodes=[]
import json
with open ('newwords.json','r') as json_data:
    data=json.load(json_data)
    for d in data:
        listofnodes.append(d["items"])
        for word in d["items"]:
            allwords.append(word)
setofwords=list(set(allwords))
rank={}

for index in setofwords:
    rank.update({index:0})
dictofwords={i:setofwords[i] for i in range(0,len(setofwords))}
import json
with open ('newwords.json','r') as json_data:
    data=json.load(json_data)
    for i in range(len(data)):
        words=[]
        for key,word in dictofwords.items():
            if word in (data[i]["items"]):
                #listofnodes.append(data[i]["items"])
                words.append(word)
                #rank[key]+=1
        hyperg.update({i:words})


import networkx as nx
G=nx.Graph()
#G.add_nodes_from(listofnodes)
for node1 in range(len(listofnodes)):
    for node2 in range(node1+1,len(listofnodes)):
        newset = []
        #if(node1 is not node2):
        if(len(set(listofnodes[node1]).intersection(set(listofnodes[node2])))>=1):
            G.add_edge(str(listofnodes[node1]),str(listofnodes[node2]))
            newset = list(set(listofnodes[node1]).intersection(set(listofnodes[node2])))
            for sin in newset:
                rank[sin]+=1
        else:
            G.add_node(str(listofnodes[node1]))
            G.add_node(str(listofnodes[node2]))
    #print(node1," inytersects ",node2," ",newset)

                
#dicofwords={i:newset[i] for i in range(0,len(newset))}
import matplotlib.pyplot as plt
nx.draw(G)
plt.show()


sorted_words = sorted(rank.items(), key=lambda x: x[1], reverse=True)
for doc,vertices in sorted_words:
    print(doc,": ",vertices)

#for kk,jj in .items():
#    print(kk,": ", jj)
"""
n=40
import sklearn.cluster as sc
MP=nx.adjacency_matrix(G).toarray()
spec=sc.spectral_clustering(affinity=MP,n_clusters=n,eigen_solver='arpack')
#spec=sc.AffinityPropagation(damping=0.5, max_iter=200, convergence_iter=15, copy=True, preference=None, affinity='euclidean', verbose=False).fit_predict(X=MP)
#spec=sc.AgglomerativeClustering(n_clusters=15, affinity='euclidean', memory=None, connectivity=None, compute_full_tree='auto', linkage='complete').fit_predict(X=MP)
#changes here
clus=[]
for num in range(n):
    clus.append([])

#this and
    
mylist=G.nodes()

import matplotlib.colors as mc
color_list=mc.get_named_colors_mapping()
colors=[]


for k,v in color_list.items():
    colors.append(v)	
colors=colors[:n]
node_dict={i:spec[i] for i in range(len(mylist))}
color_map=[]
print(node_dict)
for kk,c in node_dict.items():
    color_map.append(colors[c])
    clus[c].append(listofnodes[kk])
    
#print (mylist[1])
for cl in clus:
    print(cl)

import pickle
#pos=nx.spectral_layout(G)
with open("tx.txt","wb") as f:
    pickle.dump(clus,f)
nx.draw(G,node_color=color_map,node_size=30)
plt.show()
#print(str(rank))
mywordsdict={dictofwords[mm]:pp for mm,p in sorted_words}
import pickle
with open ('rankedhypergraph.txt','wb') as file:
    pickle.dump(mywordsdict,file)
"""

    
