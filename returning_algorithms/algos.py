import utils

def robert_flores_ms(adj_matrix):
    return hamiltonian_cycle(adj_matrix)

def find_euler_tour(graph, start):
    tour = []
    stack = [start]

    while stack:
        u = stack[-1]
        print(stack[-1])
        if any(graph[u]):
            for v in range(len(graph)):
                if graph[u][v] > 0:
                    stack.append(v)
                    graph[u][v] -= 1
                    graph[v][u] -= 1
                    break
        else:
            tour.append(stack.pop() + 1)

    return tour[::-1]

def euler_cycle(graph):
    odd_count = sum([sum(row) % 2 for row in graph]) // 2
    if odd_count != 0 and odd_count != 2:
        print("Graf wejściowy nie zawiera cyklu Eulera.")
        return

    start = 0
    for i in range(len(graph)):
        if sum(graph[i]) % 2 != 0:
            start = i
            break

    tour = find_euler_tour(graph, start)
    print("Cykl Eulera znaleziony:", tour)


def is_valid_hamilton(vertex, graph, path, pos):
    if graph[path[pos - 1]][vertex] == 0:
        return False

    if vertex in path:
        return False

    return True

def hamilton_util(graph, path, pos):
    if pos == len(graph):
        if graph[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    for v in range(len(graph)):
        if is_valid_hamilton(v, graph, path, pos):
            path[pos] = v

            if hamilton_util(graph, path, pos + 1):
                return True

            path[pos] = -1

    return False

def hamiltonian_cycle(graph):
    path = [-1] * len(graph)
    path[0] = 0

    if not hamilton_util(graph, path, 1):
        print("Graf wejściowy nie zawiera cyklu Hamiltona.")
        return


def hamiltonian(v, graph, visited, path, start):
    path.append(v)  # Append the current vertex to the path at the beginning of the function call
    visited[v] = True
    visited_count = sum(visited.values())

    if visited_count == len(graph) and start in graph[v]:
        return True  # Check if all vertices are visited and the start can be reached from the current vertex

    for i in graph[v]:
        if not visited[i]:
            if hamiltonian(i, graph, visited, path, start):
                return True  # Recursively explore the next vertex

    path.pop()  # If no path is found, remove the vertex from the path
    visited[v] = False
    return False

def Hcycle(graph, n, start):
    visited = {v: False for v in range(n)}  # Initialize the visited dictionary from 0 to n-1
    path = []

    if hamiltonian(start, graph, visited, path, start):
        path.append(start)  # To complete the cycle, append the start vertex at the end if a cycle is found
        return True, path
    else:
        return False, []

def robert_flores_ln(graph, n):
    found, hamiltonian_cycle = Hcycle(graph, n, 0)  # Start from vertex 0
    if found:
        return f"Found Hamiltonian cycle: {hamiltonian_cycle}"
    else:
        return "No Hamiltonian cycle found."


def fury_ms(adj_matrix):
    num_vertices = len(adj_matrix)

    # Check if the graph is Eulerian and ensure the graph is connected
    for i in range(num_vertices):
        if sum(adj_matrix[i]) % 2 != 0:
            return []

    # Copy the adjacency matrix to avoid modifying the original
    adj_copy = [row[:] for row in adj_matrix]

    # Initialize an empty list to store the Eulerian cycle
    euler_cycle = []

    # Choose the starting vertex arbitrarily (not isolated)
    start_vertex = next((i for i, row in enumerate(adj_matrix) if any(v > 0 for v in row)), 0)

    # Inner function to find the Eulerian cycle
    def find_euler_cycle(vertex):
        stack = [vertex]
        while stack:
            curr = stack[-1]
            row = adj_copy[curr]
            try:
                next_vertex = next(i for i, v in enumerate(row) if v > 0)
                adj_copy[curr][next_vertex] -= 1
                adj_copy[next_vertex][curr] -= 1
                stack.append(next_vertex)
            except StopIteration:
                euler_cycle.append(stack.pop())

    # Find the Eulerian cycle
    find_euler_cycle(start_vertex)

    # Print the Eulerian cycle
    print("Cykl Eulera:", euler_cycle)
    return euler_cycle


def fury_ln(successor_list):
    # Check if the graph is Eulerian

    # Copy the successor list to avoid modifying the original
    successor_copy = {vertex: list(successors) for vertex, successors in successor_list.items()}

    # Initialize an empty list to store the Eulerian cycle
    euler_cycle = []

    # Choose the starting vertex that is not isolated
    start_vertex = next((v for v, successors in successor_list.items() if successors), None)
    if start_vertex is None:
        print("No valid starting vertex found.")
        return []

    # Function to find the Eulerian cycle using a stack
    def find_euler_cycle(vertex):
        stack = [vertex]
        while stack:
            current = stack[-1]
            if successor_copy[current]:
                next_vertex = successor_copy[current].pop(0)
                successor_copy[next_vertex].remove(current)
                stack.append(next_vertex)
            else:
                euler_cycle.append(stack.pop())

    # Check connectivity using a modified approach
    def is_connected(component_vertex):
        explored = set()
        stack = [component_vertex]
        while stack:
            node = stack.pop()
            if node not in explored:
                explored.add(node)
                stack.extend(successor_copy[node])
        return set(successor_list.keys()) == explored

    # Ensure the graph is connected
    if not is_connected(start_vertex):
        print("Graf nie jest spójny")
        return []

    # Find the Eulerian cycle
    find_euler_cycle(start_vertex)

    # The cycle might be in reverse order
    euler_cycle.reverse()

    # Print the Eulerian cycle
    print("Cykl Eulera:", euler_cycle)
    return euler_cycle