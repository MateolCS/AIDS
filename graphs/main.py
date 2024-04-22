import utils
import getter
import sorts
dim, vertices, arcs = getter.read_data(r'graphs\input.txt')
matrix = utils.build_adjacency_matrix(dim[0], arcs)

d = utils.build_consequent_list(dim[0], arcs)

print(f"dict {d}")
#print(sorts.kahn_ms(dim[0], matrix))
print(sorts.kahn_ln(d))