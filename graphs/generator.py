import networkx as nx
import random

def generate_graph(n, density):
    max_edges = n * (n - 1) // 2
    num_edges = int(density * max_edges)
    G = nx.DiGraph()
    G.add_nodes_from(range(n))
    edge_list = []

    for i in range(n):
        for j in range(i + 1, n):
            edge_list.append((i, j))

    random.shuffle(edge_list)

    for i in range(num_edges):
        edge = edge_list[i]
        G.add_edge(edge[0], edge[1])

        if nx.is_directed_acyclic_graph(G):
            continue
        else:
            G.remove_edge(edge[0], edge[1])

    return (n, num_edges), list(G.edges())