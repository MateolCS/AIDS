import utils
import getter
import sorts
dim, vertices, arcs = getter.read_data('./input.txt')
matrix = utils.build_adjacency_matrix(dim[0], arcs)

d = utils.build_consequent_list(dim[0], arcs)

#print(f"dict {d}")
#print(f"matrix {matrix}")
#print(sorts.kahn_ms(dim[0], matrix))
#print(sorts.kahn_ln(d))
print(sorts.tarjan_ms(dim[0], matrix))
print(sorts.tarjan_ln(d))