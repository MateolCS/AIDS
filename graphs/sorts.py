def tarjan_ln(in_matrix):
    visited = {key: False for key in in_matrix}
    stack = []

    def dfs(v):
        visited[v] = True
        for neighbor in in_matrix.get(v, []):
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(v)


    if start_vertex is None:
        in_degrees = [0] * in_v
        for i in range(in_v):
            for j in range(in_v):
                in_degrees[j] += in_matrix[i][j]

        start_vertex = next((index for index, degree in enumerate(in_degrees) if degree == 0), None)
        
        if start_vertex is None:
            print("Graf może zawierać cykl lub nie posiada wierzchołka z zerowym stopniem wejściowym.")
            return []
    
    
    dfs(start_vertex)
    
    
    for v in range(in_v):
        if not visited[v]:
            dfs(v)

    stack.reverse()  
    return stack


def tarjan_ln(graph, start_vertex=None):
    in_v = len(graph)  
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
    
    indegree = [0] * in_v
    
   
    for i in range(in_v):
        for j in range(in_v):
            if in_matrix[i][j] == 1:
                indegree[j] += 1
 

    q = []
    for i in range(in_v):
        if indegree[i] == 0:
            q.append(i)
    
    result = []
    while q:
        node = q.pop(0)
        result.append(node)

        for j in range(in_v):
            if in_matrix[node][j] == 1:
                indegree[j] -= 1

                if indegree[j] == 0:
                    q.append(j)
 

    if len(result) != in_v:
        return "Znaleziono cykl, sortowanie niemozliwe"
    
    return result


def kahn_ln(in_dict):

    indegree = {v: 0 for v in in_dict}
    

    for vertex in in_dict:
        for neighbor in in_dict[vertex]:
            indegree[neighbor] += 1
 

    q = [v for v in in_dict if indegree[v] == 0]
    
    result = []
    while q:
        node = q.pop(0)
        result.append(node)

        for neighbor in in_dict[node]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                q.append(neighbor)
 

    if len(result) != len(in_dict):
        return "Graf zawiera cykl, sortowanie niemoozliwe"
    
    return result

