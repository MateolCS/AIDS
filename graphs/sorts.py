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
            for i in graph[v]:  
                dfs(i)
            temp_mark[v] = False
            stack.append(v)


    if start_vertex is None:
        in_degrees = [0] * in_v
        for successors in graph.values():
            for j in successors:
                in_degrees[j] += 1

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

