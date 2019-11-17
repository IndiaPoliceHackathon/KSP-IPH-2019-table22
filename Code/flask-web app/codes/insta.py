import networkx as nx

G=nx.MultiGraph()

G.add_edge(1,2)

G.add_edge(1,2)

nx.write_dot(G,'multi.dot')

