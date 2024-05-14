def robert_flores_ms(adj_matrix):
    num_vertices = len(adj_matrix)
    dp = [[0] * (1 << num_vertices) for _ in range(num_vertices)]

    # Initialize the base case
    for i in range(num_vertices):
        dp[i][1 << i] = 1

    # Iterate over all subsets of vertices
    for mask in range(1, 1 << num_vertices):
        for i in range(num_vertices):
            if mask & (1 << i):
                for j in range(num_vertices):
                    if mask & (1 << j) and adj_matrix[j][i] and i != j:
                        dp[i][mask] += dp[j][mask ^ (1 << i)]

    # Find the last vertex in the cycle
    last_vertex = -1
    for i in range(num_vertices):
        if dp[i][(1 << num_vertices) - 1] > 0:
            last_vertex = i
            break

    # Reconstruct the cycle
    if last_vertex == -1:
        print("Cykl nie istnieje")
        return

    cycle = [last_vertex]
    mask = (1 << num_vertices) - 1
    while mask != 0:
        for i in range(num_vertices):
            if adj_matrix[i][last_vertex] and (mask & (1 << i)) and dp[i][mask ^ (1 << last_vertex)] > 0:
                cycle.append(i)
                mask ^= (1 << last_vertex)
                last_vertex = i
                break

    print("Cykl Hamiltona:", cycle)


def robert_flores_ln(successor_list):
    num_vertices = len(successor_list)
    dp = [[0] * (1 << num_vertices) for _ in range(num_vertices)]

    # Initialize the base case
    for i in range(num_vertices):
        dp[i][1 << i] = 1

    # Iterate over all subsets of vertices
    for mask in range(1, 1 << num_vertices):
        for i in range(num_vertices):
            if mask & (1 << i):
                for j in successor_list[i]:
                    if mask & (1 << j) and i != j:
                        dp[i][mask] += dp[j][mask ^ (1 << i)]

    # Find the last vertex in the cycle
    last_vertex = -1
    for i in range(num_vertices):
        if dp[i][(1 << num_vertices) - 1] > 0:
            last_vertex = i
            break

    # Reconstruct the cycle
    if last_vertex == -1:
        print("Cykl nie istnieje")
        return

    cycle = [last_vertex]
    mask = (1 << num_vertices) - 1
    while mask != 0:
        for i in successor_list[last_vertex]:
            if mask & (1 << i) and dp[i][mask ^ (1 << last_vertex)] > 0:
                cycle.append(i)
                mask ^= (1 << last_vertex)
                last_vertex = i
                break

    print("Cykl Hamiltona:", cycle)

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