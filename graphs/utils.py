def build_adjacency_matrix(in_v, arcs):
    adjacency_matrix = [[0] * in_v for _ in range(in_v)]

    for start, end in arcs:
        adjacency_matrix[start][end] = 1
        adjacency_matrix[end][start] = -1

    return adjacency_matrix

def build_consequent_list(arcs):
    consequent_list = {}

    for start, end in arcs:
        if start in consequent_list.keys():
            consequent_list[start].append(end)
        else:
            consequent_list[start] = [end]
    
    return consequent_list

