import sorts
import utils
import networkx as nx
import random
from timeit import default_timer as timer
import numpy as np

def generate_graph(n):
    # Stworzenie pustego grafu skierowanego
    G = nx.DiGraph()
    # Dodanie wierzchołków do grafu
    G.add_nodes_from(range(n))
    # Maksymalna liczba krawędzi w DAG
    max_edges = n * (n - 1) // 2
    # Liczba krawędzi, które chcemy dodać
    num_edges = max_edges // 2
    
    edges_added = 0
    while edges_added < num_edges:
        # Losowanie dwóch różnych wierzchołków
        u, v = random.sample(range(n), 2)
        # Dodanie krawędzi jeśli jeszcze nie istnieje i nie tworzy cyklu
        if not G.has_edge(u, v) and not G.has_edge(v, u):
            G.add_edge(u, v)
            # Sprawdzenie, czy nie powstał cykl
            if nx.is_directed_acyclic_graph(G):
                edges_added += 1
            else:
                # Usunięcie krawędzi jeśli powstał cykl
                G.remove_edge(u, v)

    return (n, len(G.edges)), list(G.edges)


n_values = list(range(100, 151, 10))
k = 1500

def tarjan_ln_test(in_values):
    
    for value in in_values:
        times= []
        for _ in range(10):

            dim, edge_list = generate_graph(value)
            start = timer()
            ln = utils.build_consequent_list(dim[0], edge_list)
            sorts.tarjan_ln(ln)
            end = timer()
            times.append(start-end)
        
        print(f"Elements: {value}, execution time: {np.mean(times)} deviation: {np.std(times)}\n")
    print("---------------------------------------------------------------------------------------------------------")

def tarjan_ms_test(in_values):

    for value in in_values:
        times= []
        for _ in range(10):

            dim, edge_list = generate_graph(value)
            start = timer()
            matrix = utils.build_adjacency_matrix(dim[0], edge_list)
            sorts.tarjan_ms(matrix)
            end = timer()
            times.append(start-end)
        
        print(f"Elements: {value}, execution time: {np.mean(times)} deviation: {np.std(times)}\n")
    print("---------------------------------------------------------------------------------------------------------")

def khan_ms_test(in_values):

    for value in in_values:
        times= []
        for _ in range(10):

            dim, edge_list = generate_graph(value)
            start = timer()
            matrix = utils.build_adjacency_matrix(dim[0], edge_list)
            sorts.kahn_ms(dim[0], matrix)
            end = timer()
            times.append(start-end)
        
        print(f"Elements: {value}, execution time: {np.mean(times)} deviation: {np.std(times)}\n")
    print("---------------------------------------------------------------------------------------------------------")

def khan_ln_test(in_values):

    for value in in_values:
        times= []
        for _ in range(10):

            dim, edge_list = generate_graph(value)
            start = timer()
            ln = utils.build_consequent_list(dim[0], edge_list)
            sorts.kahn_ln(ln)
            end = timer()
            times.append(start-end)
        
        print(f"Elements: {value}, execution time: {np.mean(times)} deviation: {np.std(times)}\n")

    print("---------------------------------------------------------------------------------------------------------")



def run_tests():

    print("Tarjan ms test: \n")
    tarjan_ms_test(n_values)

    print("Tarjan ln test: \n")
    tarjan_ln_test(n_values)

    print("Khan ms test: \n")
    khan_ms_test(n_values)

    print("Khan ln test: \n")
    khan_ln_test(n_values)
    

    



run_tests()


