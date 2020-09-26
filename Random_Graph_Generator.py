import networkx as nx
import random
import numpy as np

# Set up a graph with random edges and weights

nodes = 500
edges = 200

G = nx.barabasi_albert_graph(nodes, edges)
for u,v in G.edges():
    G[u][v]['weight'] = random.randint(1, 100)
    
path = str(nodes) + '.txt'

a = nx.to_numpy_matrix(G)
np.savetxt(path, a)

with open(path, 'r+') as f:
    old = f.read()
    f.seek(0, 0)
    f.write('A\n' + str(nodes) + '\n' + old)