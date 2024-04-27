def tarjan_ln(in_matrix):
    visited = {key: False for key in in_matrix}
    stack = []

    def dfs(v):
        visited[v] = True
        for neighbor in in_matrix.get(v, []):
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(v)

    for vertex in in_matrix:
        if not visited[vertex]:
            dfs(vertex)

    return stack[::-1] 


def tarjan_ms(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    stack = []

    def dfs(v):
        visited[v] = True
        for i in range(n):
            if adj_matrix[v][i] and not visited[i]:
                dfs(i)
        stack.append(v)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return stack[::-1]



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
