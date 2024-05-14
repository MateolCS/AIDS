import utils

def robert_flores_ms(adj_matrix):
    def dfs(v, O, Path, start, visited, k):
        O[v] = True
        visited[0] += 1
        for i in range(len(adj_matrix)):
            if adj_matrix[v][i] == 1:
                if i == start and visited[0] == len(O):
                    return True
                if not O[i]:
                    if dfs(i, O, Path, start, visited, k):
                        Path[k[0]] = v
                        k[0] += 1
                        return True
        O[v] = False
        visited[0] -= 1
        return False

    n = len(adj_matrix)
    O = [False] * n
    Path = [0] * n
    start = 0
    visited = [0]
    k = [1]
    if dfs(start, O, Path, start, visited, k):
        Path.append(Path[0])
        return f"Cykl istnieje: {Path[:k[0]]}"
    else:
        return f"Cykl nie istnieje"


def hamiltonian(v, graph, visited, path, start):
    visited[v] = True
    visited_count = sum(visited.values())
    
    for i in graph[v]:
        if i == start and visited_count == len(graph):
            return True
        
        if not visited[i]:
            if hamiltonian(i, graph, visited, path, start):
                path.append(v)
                return True
                
    visited[v] = False
    return False

def Hcycle(graph, n):
    visited = {v: False for v in range(1, n+1)}
    path = [0] * (n + 1)
    path[1] = start = 1
    visited_count = 0
    
    if hamiltonian(start, graph, visited, path, start):
        return True, path[::-1]
    else:
        return False, []

def robert_flores_ln(graph, n):
    found, hamiltonian_cycle = Hcycle(graph, n)
    if found:
        return f"Znaleziono cykl Hamiltona: {hamiltonian_cycle[1:]}"
    else:
        return "Nie znaleziono cyklu Hamiltona."


def fury_ms(adj_matrix):
    num_vertices = len(adj_matrix)

    # Check if the graph is Eulerian
    for i in range(num_vertices):
        if sum(adj_matrix[i]) % 2 != 0:
            print("Graf nie ma cyklu Eulera")
            return []

    # Copy the adjacency matrix to avoid modifying the original
    adj_copy = [row[:] for row in adj_matrix]

    # Initialize an empty list to store the Eulerian cycle
    euler_cycle = []

    # Choose the starting vertex arbitrarily
    start_vertex = 0

    # Inner function to find the Eulerian cycle
    def find_euler_cycle(vertex):
        while True:
            # Find the next vertex to visit
            next_vertex = None
            for i in range(len(adj_copy[vertex])):
                if adj_copy[vertex][i] > 0:
                    next_vertex = i
                    break

            # If there are no more edges from the current vertex, return
            if next_vertex is None:
                break

            # Remove the edge between the current vertex and the next vertex
            adj_copy[vertex][next_vertex] -= 1
            adj_copy[next_vertex][vertex] -= 1

            # Visit the next vertex
            find_euler_cycle(next_vertex)

        # Add the current vertex to the Eulerian cycle
        euler_cycle.append(vertex)

    # Find the Eulerian cycle
    find_euler_cycle(start_vertex)

    # Print the Eulerian cycle
    print("Cykl Eulera:", euler_cycle)
    return euler_cycle

def fury_ln(successor_list):
    num_vertices = len(successor_list)

    # Check if the graph is Eulerian
    for vertex, successors in successor_list.items():
        if len(successors) % 2 != 0:
            print("Graf nie ma cyklu Eulera")
            return []

    # Copy the successor list to avoid modifying the original
    successor_copy = {vertex: list(successors) for vertex, successors in successor_list.items()}

    # Initialize an empty list to store the Eulerian cycle
    euler_cycle = []

    # Choose the starting vertex arbitrarily
    start_vertex = list(successor_list.keys())[0]

    # Inner function to find the Eulerian cycle
    def find_euler_cycle(vertex):
        while successor_copy[vertex]:
            # Choose the next vertex
            next_vertex = successor_copy[vertex].pop(0)

            # Remove the edge between the current vertex and the next vertex
            successor_copy[next_vertex].remove(vertex)

            # Visit the next vertex
            find_euler_cycle(next_vertex)

        # Add the current vertex to the Eulerian cycle
        euler_cycle.append(vertex)

    # Find the Eulerian cycle
    find_euler_cycle(start_vertex)

    # Reverse the Eulerian cycle to get the correct order
    euler_cycle.reverse()

    # Print the Eulerian cycle
    print("Cykl Eulera:", euler_cycle)
    return euler_cycle

g_v_1 = 5
a_l_1 = [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4)]
g_v_3 = 5
a_l_3 = [(0, 1), (0, 2), (2, 3), (2, 4), (3, 4)]
g_v_2 = 5
a_l_2 = [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (4, 1)]

matrix = utils.build_adjacency_matrix(g_v_1, a_l_1)
print(fury_ms(matrix))