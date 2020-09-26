import numpy as np
import networkx as nx
import main as sp


class Centrality:
    def __init__(self, graph):
        # import graph
        if isinstance(graph, str):
            self.graph = nx.from_numpy_matrix(np.loadtxt(graph, skiprows=2))
        elif isinstance(graph, nx.Graph):
            self.graph = graph

    # separate graph into components
    def separate_components(self):
        for c in nx.connected_components(self.graph):
            yield self.graph.subgraph(c)

    def degree_centrality(self):
        if len(self.graph) <= 1:
            return {n: 1 for n in G}
        s = 1 / (len(self.graph) - 1)
        degree_centrality = {n: d * s for n, d in self.graph.degree()}
        return degree_centrality

    def eigen_vector_centrality(self):
        e_centrality = nx.eigenvector_centrality(self.graph)
        return e_centrality

    def betweenness_centrality(self):
        b_centrality = nx.betweenness_centrality(self.graph)
        return b_centrality

    def closeness_centrality(self):
        components = list(self.separate_components())
        if len(components) > 1:
            max_component_degree = 0
            max_component_index = 0
            for i in range(len(components)):
                if components[i].number_of_nodes() > max_component_degree:
                    max_component_index = i
            max_component = sp.ShortestPath(nx.to_numpy_matrix(components[max_component_index]), 1, 0)
        elif len(components) == 1:
            max_component_index = 0
            max_component = sp.ShortestPath(nx.to_numpy_matrix(components[max_component_index]), 1, 0)
        nodes = list(range(self.graph.number_of_nodes()))
        c_centrality = [0] * len(nodes)
        index_max_component = list(sp.ShortestPath(components[max_component_index], 1, 0).graph.nodes)
        for n in range(max_component.graph.number_of_nodes()):
            s_path, s_dis = max_component.dijkstra(n)
            c_centrality[index_max_component[n]] = (max_component.graph.number_of_nodes() - 1) / np.sum(np.array(s_dis))
        c_centrality = dict(zip(nodes, c_centrality))
        return c_centrality

    def show_centrality(self):
        d = self.degree_centrality()
        e = self.eigen_vector_centrality()
        b = self.betweenness_centrality()
        c = self.closeness_centrality()
        nodes = self.graph.nodes
        # create the list of nodes
        print("{:=^126}".format(" CENTRALITY "))
        row = "| {:^10s} | {:^25s} | {:^25s} | {:^25s} | {:^25s} |"
        print(row.format('nodes', 'degree centrality', 'eigenvector centrality', 'betweenness centrality',
                         'closeness centrality'))
        row = "| {:10} | {:25.5f} | {:25.5f} | {:25.5f} | {:25.5f} |"
        for n in nodes:
            print(row.format(n, d[n], e[n], b[n], c[n]))
        print("=" * 126)


if __name__ == "__main__":
    # just for testing the class Centrality
    G = Centrality('3.4.txt')
    G.show_centrality()
