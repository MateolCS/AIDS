def build_adjacency_matrix(in_v, arcs):
    adjacency_matrix = [[0] * in_v for _ in range(in_v)]

    for start, end in arcs:
        adjacency_matrix[start][end] = 1
        adjacency_matrix[end][start] = -1

    return adjacency_matrix

def build_consequent_list(in_v, arcs):
    consequent_list = {}

    for i in range(in_v):
        consequent_list[i] = []

    #print(f"Przed appendem {consequent_list}")
    for start, end in arcs:
        consequent_list[start].append(end)

    #print(f"Przed appendem {consequent_list}")
    
    return consequent_list

def find_cycle_matrix(in_matrix):
    def dfs(vertex, parent):
        visited.add(vertex)
        for neighbor, connected in enumerate(in_matrix[vertex]):
            if connected:
                if neighbor not in visited:
                    parent[neighbor] = vertex
                    if dfs(neighbor, parent):
                        return True
                elif neighbor != parent[vertex]:
                    cycle.append(neighbor)
                    while vertex != neighbor:
                        vertex = parent[vertex]
                        cycle.append(vertex)
                    return True
        return False
    
    n = len(in_matrix)
    visited = set()
    parent = [-1] * n
    cycle = []

    for v in range(n):
        if v not in visited and dfs(v, parent):
            return cycle[::-1]
    return None

def find_cycle_dict(in_dict):
    def dfs(vertex, parent):
        visited.add(vertex)
        for neighbor in in_dict.get(vertex, []):
            if neighbor not in visited:
                parent[neighbor] = vertex
                if dfs(neighbor, parent):
                    return True
            elif neighbor != parent[vertex]:
                cycle.append(neighbor)
                while vertex != neighbor:
                    vertex = parent[vertex]
                    cycle.append(vertex)
                return True
        return False

    visited = set()
    parent = {}
    cycle = []

    for v in in_dict:
        if v not in visited and dfs(v, parent):
            return cycle[::-1]
    return None