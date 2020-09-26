import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import sys
import heap
import centrality


class ShortestPath:
    def __init__(self, graph, method, root):
        # import graph
        if isinstance(graph, str):
            self.graph = nx.from_numpy_matrix(np.loadtxt(graph, skiprows=2))
        elif isinstance(graph, nx.Graph):
            self.graph = graph
        elif isinstance(graph, np.matrix):
            self.graph = nx.from_numpy_matrix(graph)
        self.method = method
        self.root = root

    # imported from centrality.py to calculate the centrality measures
    def show_centrality(self):
        centrality.Centrality(self.graph).show_centrality()

    # tabulate shortest path results
    def print_sp(self, s_dis, s_path, root):
        print('{:=^60}'.format(" Shortest Path "))
        row = " {:^10} | {:^17} | {:^20}"
        print(row.format('ending nodes', 'shortest distance', 'shortest path'))
        row = " from {} to {:^2} | {:^17.2f} | {} "
        for n in range(self.graph.number_of_nodes()):
            path = [n]
            p = n
            try:
                tempo = s_dis[root]
            except IndexError:
                print(row.format(root, n, s_dis[n], path))
                print('=' * 60)
                return
            while p != self.root:
                path.insert(0, s_path[p])
                p = s_path[p]
            print(row.format(root, n, s_dis[n], path))
        print('=' * 60)

    # get index of minimal distance
    def min_dis_array(self, s_dis, perm_set):
        min_dis = float('inf')  # initialise minimal distance to be infinity
        for n in range(self.graph.number_of_nodes()):
            if not perm_set[n] and s_dis[n] < min_dis:
                min_dis = s_dis[n]
                min_index = n
        return min_index

    # used to implement Dijkstra's algorithm
    def dijkstra(self, root):  # array method
        s_dis = [float('inf')] * self.graph.number_of_nodes()  # initialise shortest distance to be infinity
        perm_set = [False] * self.graph.number_of_nodes()  # initialise the permanent set
        s_path = [False] * self.graph.number_of_nodes()  # initialise the shortest path
        try:
            s_dis[root] = 0  # distance from root to root is 0
        except IndexError:
            return s_path, s_dis
        s_path[self.root] = self.root
        if nx.number_connected_components(self.graph) > 1:
            print("This graph has more than 1 component, thus having no spanning tree")
            sys.exit()

        for i in range(self.graph.number_of_nodes()):
            # to test if the graph contains only one node, if it has no adjacency list, return
            try:
                tempo = self.graph.adj[i]
            except KeyError:
                return s_path, s_dis

            u = self.min_dis_array(s_dis, perm_set)
            perm_set[u] = True
            # relaxation
            for v in list(self.graph.adj[u]):
                if not perm_set[v] and (s_dis[v] > s_dis[u] + self.graph[u][v]['weight']):
                    s_dis[v] = s_dis[u] + self.graph[u][v]['weight']
                    s_path[v] = u
        return s_path, s_dis

    # used to implement Tarjan's algorithm
    def tarjan(self, root):  # heap method
        s_dis = [float('inf')] * self.graph.number_of_nodes()  # initialise shortest distance to be infinity
        tempo_set = [True] * self.graph.number_of_nodes()  # initialise the temporary set
        tempo_set[self.root] = False
        s_path = [False] * self.graph.number_of_nodes()  # initialise paths
        try:
            s_dis[root] = 0  # distance from root to root is 0
        except IndexError:
            return s_path, s_dis
        s_path[self.root] = self.root

        if nx.number_connected_components(self.graph) > 1:
            print("This graph has more than 1 component, thus having no spanning tree")
            sys.exit()

        s = heap.Heap()  # heap initialisation
        s.insert([root, s_dis[root]])
        while any(tempo_set):
            u, dis = s.popmin()
            tempo_set[u] = False
            # to test if the graph contains only one node, if it has no adjacency list, return
            try:
                tempo = self.graph.adj[u]
            except KeyError:
                return s_path, s_dis

            for v in self.graph.adj[u]:
                if s_dis[v] > s_dis[u] + self.graph[u][v]['weight']:
                    s_dis[v] = s_dis[u] + self.graph[u][v]['weight']
                    s_path[v] = u
                    if v not in [e[0] for e in s.elements]:
                        s.insert([v, s_dis[v]])
                    else:
                        s.siftup([e[0] for e in s.elements].index(v))
        return s_path, s_dis


# Calculate total number of time taken to calculate shortest path
def test(nodes, edges_per_node):
    # use preferential attachment to generate graph
    graph = nx.barabasi_albert_graph(nodes, edges_per_node)
    for u, v in graph.edges():
        graph[u][v]['weight'] = random.randint(1, 50)

    start_time_array = time.time()
    for i in range(graph.number_of_nodes()):
        a = ShortestPath(graph, 1, i)
        a.dijkstra(i)
    end_time_array = time.time()
    running_time_array = end_time_array - start_time_array  # total running time of Dijkstra(array) method

    start_time_heap = time.time()
    for i in range(graph.number_of_nodes()):
        a = ShortestPath(graph, 2, i)
        a.tarjan(i)
    end_time_heap = time.time()
    running_time_heap = end_time_heap - start_time_heap  # total running time of Tarjan(heap) method

    print("total running time:\narray: {} seconds\nheap: {} seconds".format(running_time_array, running_time_heap))


# visualise graph
def show_graph(G):
    # set the layout
    pos = nx.spring_layout(G)
    # draw the graph
    nx.draw(G, pos, with_labels=True, node_color='pink', node_size=500, alpha=1, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.show()


def main():
    goal = input('Please input what do you want to run:\nfor Shortest Path: 1\nfor Centrality: any other number\n')
    if goal == '1':
        f_path = input('Please input the path of the graph(i.e. 3.3.txt):\n')
        # open file
        try:
            file = open(f_path, "r")
        except OSError:
            print("Could not open or read file\n", f_path)
            sys.exit()
        g_root = int(input('Please input the root of the shortest spanning tree(starting from 0):\n'))
        method = int(input('Please input the number to choose the method,\n1: array\n2: heap\n'))

        visualisation = input('Input 1 to visualise graph, any other number to pass:\n')
        if visualisation == '1':
            G = ShortestPath(f_path, 1, 0)
            show_graph(G.graph)

        start_time = time.time()

        G = ShortestPath(f_path, method, g_root)

        if G.method == 1:
            s_path, s_dis = G.dijkstra(g_root)  # call array method
        elif G.method == 2:
            s_path, s_dis = G.tarjan(g_root)  # call heap method
        print('Shortest Path Spanning Tree Rooted at node {}:\n{}'.format(g_root, s_path))
        print('Shortest Distance:\n{}'.format(s_dis))

        end_time = time.time()

        running_time = end_time - start_time
        print('\nRunning time is {} second(s)\n'.format(running_time))

        tab = input('Input 1 to tabulate the results, any other number to exit:\n')
        if tab == '1':
            G.print_sp(s_dis, s_path, g_root)
        else:
            sys.exit()

    else:
        f_path = input('Please input the path of the graph(i.e. 3.4.txt):\n')
        # open file
        try:
            file = open(f_path, "r")
        except OSError:
            print("Could not open or read file\n", f_path)
            sys.exit()

        visualisation = input('Input 1 to visualise graph, any other number to pass:\n')
        if visualisation == '1':
            G = ShortestPath(f_path, 1, 0)
            show_graph(G.graph)

        G = ShortestPath(f_path, 1, 0)
        G.show_centrality()  # call centrality function


if __name__ == "__main__":
    main()
    # test(300, 1)
    # test(300, 100)