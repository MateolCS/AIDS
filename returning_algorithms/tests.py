import algos
import utils
import networkx as nx
import random
from timeit import default_timer as timer
import numpy as np

def generate_graph(n, density=0.5):
    # Ensure density is within the valid range
    if not (0 <= density <= 1):
        raise ValueError("Density must be between 0 and 1")
    
    # Create an empty directed graph
    G = nx.DiGraph()
    # Add nodes to the graph
    G.add_nodes_from(range(n))
    # Maximum number of edges in a DAG
    max_edges = n * (n - 1) // 2
    # Number of edges to add based on the density
    num_edges = int(density * max_edges)
    
    edges_added = 0
    while edges_added < num_edges:
        # Randomly select two different nodes
        u, v = random.sample(range(n), 2)
        # Add the edge if it doesn't exist and doesn't create a cycle
        if not G.has_edge(u, v) and not G.has_edge(v, u):
            G.add_edge(u, v)
            # Check if a cycle is created
            if nx.is_directed_acyclic_graph(G):
                edges_added += 1
            else:
                # Remove the edge if a cycle is created
                G.remove_edge(u, v)

    return (n, len(G.edges)), list(G.edges)



n_values = list(range(100, 151, 10))
densities = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
k = 1500

def robert_test(in_values, densities):
    
    for value in in_values:
        times= []
        for i in range(9):

            dim, edge_list = generate_graph(value, densities[i])
            start = timer()
            adjacency_matrix = utils.build_adjacency_matrix(dim[0], edge_list)
            algos.robert_flores_ms(adjacency_matrix)
            end = timer()
            times.append(end-start)
        
        print(f"Elements: {value}, execution time: {np.mean(times)} deviation: {np.std(times)}\n")
    print("---------------------------------------------------------------------------------------------------------")

def fury_test(in_values, densities):

    for value in in_values:
        times= []
        for i in range(9):

            dim, edge_list = generate_graph(value, densities[i])
            start = timer()
            matrix = utils.build_adjacency_matrix(dim[0], edge_list)
            algos.fury_ms(matrix)
            end = timer()
            times.append(end-start)
        
        print(f"Elements: {value}, execution time: {np.mean(times)} deviation: {np.std(times)}\n")
    print("---------------------------------------------------------------------------------------------------------")



def run_tests():

    print("fury ln test: \n")
    fury_test(n_values, densities)
    
    print("Robert ms test: \n")
    robert_test(n_values, densities)



run_tests()


