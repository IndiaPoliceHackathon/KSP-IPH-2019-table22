import twint
import os
import subprocess
import sys
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

# c = twint.Config()


name = sys.argv[1]
# lim = sys.argv[2]
# limit = input()
tweets = 'twint -u ' + name + ' --profile-full -o output.csv --csv'
# tweets = 'twint -u realDonaldTrump --retweets -o tweets4.csv'
followers = 'twint -u ' + name + ' --followers -o followers.csv --csv'
following = 'twint -u ' + name + ' --following -o following.csv --csv'



os.system(tweets)
# flag = 1
# while (flag == 1):
#     try:
#         os.system(followers)
#     except:
#         flag = 0


# os.system(following)


# data=pd.read_csv("output.csv")


# list1=[]
# list2=[]
# list3=[]
# list4=[]
# for i in data['mentions']:
# #     i=i.strip()
#     i = i.strip('[]')
#     if i:
#         list1.append(i.strip('[]'))
# # print(list1)
# # for i in list1:
# #     if len(i)==0:
# #         pass
# #     else:
# #         list2.append(i)
# for i in list1:
#     i = i.split(",")
# #     print(i.split(","))
#     for j in i:
#         j = j.split()
#         list3.append(j)

# final_dict=dict()

# for i in list3:
#     if(len(i)>1):
#         for x in i:
#             x.strip()
#             if x not in list(final_dict.keys()):
#                 final_dict[x]=1
#             else:
#                 final_dict[x]+=1
#     else:
#         if i[0] not in list(final_dict.keys()):
#             final_dict[i[0]]=1
#         else:
#             final_dict[i[0]]+=1       

# def Reverse(lst): 
#     return [ele for ele in reversed(lst)] 


# a=Reverse(sorted(final_dict, key=final_dict.get))

# s=0
# for i in a:
#        s+=final_dict[i]
# print(s)
# k=[]
# for i in a:
#     k.append(final_dict[i]/s)
# # G=nx.Graph()
# G = nx.MultiGraph()


# for i in range(10):
#        G.add_edge(name ,a[i], weight = (k[i]/s)*100)
# # print(a[:10])
# # for i in a:
# #     for num in range(0,final_dict[i]):
# #         G.add_edge("realDonaldTrump",i,weight=0.1*final_dict[i])


# # G1=Network()
# # G1.from_nx(G)
# # #G1.enable_physics(True)
# # G1.show("mygraph.html")

# elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.01]
# esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.01]

# pos = nx.spring_layout(G)  # positions for all nodes

# # nodes
# nx.draw_networkx_nodes(G, pos, node_size=700)

# # edges
# nx.draw_networkx_edges(G, pos, edgelist=elarge,
#                        width=6)
# nx.draw_networkx_edges(G, pos, edgelist=esmall,
#                        width=6, alpha=0.5, edge_color='b', style='dashed')

# # labels
# nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

# plt.axis('off')
# plt.show()

# G=nx.MultiGraph()


# for i in range(10):
#    G.add_edge(name,a[i])

# G1=Network()
# G1.from_nx(G)
# G1.show("graph.html")