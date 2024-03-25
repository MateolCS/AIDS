from tree import Tree

tree = Tree([1, 2, 4, 8, 16, 32, 64, 128, 256, 512])
tree.print_tree()
tree.delete(tree.root, 64)
tree.traverse_inorder()
print(tree.find_max())