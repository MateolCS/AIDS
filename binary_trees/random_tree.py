
from tree import Tree
from node import Node
class RandomTree(Tree):
    def __init__(self, array) -> None:
        self.root = self.build_tree(array)

    def build_tree(self, array):
        if not array:
            return None

        root = Node(array[0])
        queue = [root]

        i = 1
        while i < len(array):
            current_node = queue.pop(0)

            # Add left child if available
            if i < len(array) and array[i] is not None:
                current_node.left = Node(array[i])
                queue.append(current_node.left)
            i += 1

            # Add right child if available
            if i < len(array) and array[i] is not None:
                current_node.right = Node(array[i])
                queue.append(current_node.right)
            i += 1

        return root
