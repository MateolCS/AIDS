import utils
import getter

dim, vertices, arcs = getter.read_data(r'graphs\input.txt')
print(utils.build_consequent_list(arcs))
print(dim[0])
matrix = utils.build_adjacency_matrix(dim[0], arcs)

for row in matrix:
    print(row)