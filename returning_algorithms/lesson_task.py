def is_eulerian(vertices, arcs):

    adj_matrix = [[0]*vertices for _ in range(vertices)]

    for u, v in arcs:
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1


    degrees = [sum(row) for row in adj_matrix]
    odd_degree_count = sum(1 for degree in degrees if degree % 2 == 1)
    

    def is_connected():
        visited = [False] * vertices
        stack = []
        

        for i in range(vertices):
            if sum(adj_matrix[i]) > 0:
                stack.append(i)
                break
        
        if not stack:
            return False  
        
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                for neighbor in range(vertices):
                    if adj_matrix[node][neighbor] > 0 and not visited[neighbor]:
                        stack.append(neighbor)
        

        return all(visited[i] or sum(adj_matrix[i]) == 0 for i in range(vertices))

    connected = is_connected()
    has_eulerian_cycle = odd_degree_count == 0 and connected
    has_eulerian_path = odd_degree_count == 2 and connected

    # Wypisz wynik
    if has_eulerian_cycle and has_eulerian_path:
        return "Graf zawiera cykl i ścieżkę Eulera"
    elif has_eulerian_cycle:
        return "Graf zawiera cykl Eulera"
    elif has_eulerian_path:
        return "Graf zawiera ścieżkę Eulera"
    else:
        return "Graf nie zawiera ścieżki ani cyklu Eulera"


g_v_1 = 5
a_l_1 = [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4)]
print("A")
print(is_eulerian(g_v_1, a_l_1))

g_v_2 = 5
a_l_2 = [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4), (4, 1)]
print("B")
print(is_eulerian(g_v_2, a_l_2))

g_v_3 = 5
a_l_3 = [(0, 1), (0, 2), (2, 3), (2, 4), (3, 4)]
print("C")
print(is_eulerian(g_v_3, a_l_3))

g_v_4 = 5
a_l_4 = [(0, 2), (1, 2), (2, 3), (2, 4)]
print("D")
print(is_eulerian(g_v_4, a_l_4))

g_v_5 = 5
a_l_5 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 3), (2, 4), (3, 4)]
print("E")
print(is_eulerian(g_v_5, a_l_5))

g_v_6 = 6
a_l_6 = [(0, 1), (0, 2), (1, 2), (3, 4), (3, 5), (4, 5)]
print("F")
print(is_eulerian(g_v_6, a_l_6))

g_v_7 = 6
a_l_7 = [(0, 1), (0, 2), (1, 2), (2, 3), (2, 4), (3, 4)]
print("G")
print(is_eulerian(g_v_7, a_l_7))