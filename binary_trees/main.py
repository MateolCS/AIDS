from tree import Tree

import numpy as np

n = int(input("Podaj długosc tablicy: \n"))
input_list = np.random.randint(1, 100, size=n)
print(f"Wygenerowana lista: {input_list}")

tree = Tree(input_list)