def tarjan_ms(in_v, in_matrix, start_vertex=None):
    visited = [False] * in_v
    temp_mark = [False] * in_v
    stack = []
    
    def dfs(v):
        if temp_mark[v]:
            print("Graf zawiera cykl. Sortowanie niemożliwe.")
            raise Exception("Graf zawiera cykl")
        if not visited[v]:
            visited[v] = True
            temp_mark[v] = True
            for i in range(in_v):
                if in_matrix[v][i] == 1:
                    dfs(i)
            temp_mark[v] = False
            stack.append(v)

    # Jeśli użytkownik nie poda wierzchołka startowego, znajdź wierzchołek o zerowym stopniu wejściowym
    if start_vertex is None:
        in_degrees = [0] * in_v
        for i in range(in_v):
            for j in range(in_v):
                in_degrees[j] += in_matrix[i][j]
        # Wyszukaj wierzchołek z zerowym stopniem wejściowym
        start_vertex = next((index for index, degree in enumerate(in_degrees) if degree == 0), None)
        # Jeśli nie ma wierzchołka z zerowym stopniem wejściowym, może to oznaczać, że w grafie jest cykl
        if start_vertex is None:
            print("Graf może zawierać cykl lub nie posiada wierzchołka z zerowym stopniem wejściowym.")
            return []
    
    # Rozpocznij DFS z wybranego wierzchołka
    dfs(start_vertex)
    
    # Kontynuuj DFS dla pozostałych nieodwiedzonych wierzchołków
    for v in range(in_v):
        if not visited[v]:
            dfs(v)

    stack.reverse()  # Odwracamy stos, aby uzyskać prawidłową kolejność topologiczną
    return stack


def tarjan_ln(graph, start_vertex=None):
    in_v = len(graph)  # Liczba wierzchołków
    visited = [False] * in_v
    temp_mark = [False] * in_v
    stack = []

    def dfs(v):
        if temp_mark[v]:
            print("Graf zawiera cykl. Sortowanie niemożliwe.")
            raise Exception("Graf zawiera cykl")
        if not visited[v]:
            visited[v] = True
            temp_mark[v] = True
            for i in graph[v]:  # Przechodzimy przez wszystkich następników wierzchołka v
                dfs(i)
            temp_mark[v] = False
            stack.append(v)

    # Jeśli użytkownik nie poda wierzchołka startowego, znajdź wierzchołek o zerowym stopniu wejściowym
    if start_vertex is None:
        in_degrees = [0] * in_v
        for successors in graph.values():
            for j in successors:
                in_degrees[j] += 1
        # Wyszukaj wierzchołek z zerowym stopniem wejściowym
        start_vertex = next((index for index, degree in enumerate(in_degrees) if degree == 0), None)
        # Jeśli nie ma wierzchołka z zerowym stopniem wejściowym, może to oznaczać, że w grafie jest cykl
        if start_vertex is None:
            print("Graf może zawierać cykl lub nie posiada wierzchołka z zerowym stopniem wejściowym.")
            return []

    # Rozpocznij DFS z wybranego wierzchołka
    dfs(start_vertex)

    # Kontynuuj DFS dla pozostałych nieodwiedzonych wierzchołków
    for v in range(in_v):
        if not visited[v]:
            dfs(v)

    stack.reverse()  # Odwracamy stos, aby uzyskać prawidłową kolejność topologiczną
    return stack



def kahn_ms(in_v, in_matrix):
    # Vector to store indegree of each vertex
    indegree = [0] * in_v
    
    # Count indegrees for each vertex
    for i in range(in_v):
        for j in range(in_v):
            if in_matrix[i][j] == 1:
                indegree[j] += 1
 
    # Queue to store vertices with indegree 0
    q = []
    for i in range(in_v):
        if indegree[i] == 0:
            q.append(i)
    
    result = []
    while q:
        node = q.pop(0)
        result.append(node)
        # Decrease indegree of adjacent vertices as the current node is in topological order
        for j in range(in_v):
            if in_matrix[node][j] == 1:
                indegree[j] -= 1
                # If indegree becomes 0, push it to the queue
                if indegree[j] == 0:
                    q.append(j)
 
    # Check for cycle
    if len(result) != in_v:
        print("Graph contains cycle!")
        return []
    
    return result


def kahn_ln(in_dict):
    # Dictionary to store indegree of each vertex
    indegree = {v: 0 for v in in_dict}
    
    # Count indegrees for each vertex
    for vertex in in_dict:
        for neighbor in in_dict[vertex]:
            indegree[neighbor] += 1
 
    # Queue to store vertices with indegree 0
    q = [v for v in in_dict if indegree[v] == 0]
    
    result = []
    while q:
        node = q.pop(0)
        result.append(node)
        # Decrease indegree of adjacent vertices as the current node is in topological order
        for neighbor in in_dict[node]:
            indegree[neighbor] -= 1
            # If indegree becomes 0, push it to the queue
            if indegree[neighbor] == 0:
                q.append(neighbor)
 
    # Check for cycle
    if len(result) != len(in_dict):
        print("Graph contains cycle!")
        return []
    
    return result

