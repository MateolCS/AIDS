def get_data():
    
    V, E = list(map(int, input().split(" ")))

    vertices =[]
    arcs = []

    while len(vertices) < V:
        v1, v2 = list(map(int, input().split(" ")))

        if v1 not in vertices:
            vertices.append(v1)

        if v2 not in vertices:
            vertices.append(v2)

        arcs.append((v1, v2))

    return (V, E), vertices, arcs

def read_data(path):
    f = open(path, 'r')
    lines = f.readlines()
    input_list = []
    
    for line in lines:
        line = line.strip()
        line = list(map(int, line.split(" ")))
        input_list.append(line)
    

    V, E = input_list[0]

    vertices = []
    arcs = []

    for v1, v2 in input_list[1:]:
        
        if v1 not in vertices:
            vertices.append(v1)

        if v2 not in vertices:
            vertices.append(v2)

        arcs.append((v1, v2))
    
    return (V, E),  vertices, arcs
