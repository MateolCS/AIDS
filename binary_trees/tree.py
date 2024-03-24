from node import Node

class Tree:
    def __init__(self, array) -> None:
        self.root = self.buildTree(array)

    def buildTree(self, array):
        if len(array) == 0:
            return None

        sorted_array = sorted(array)
        print(sorted_array)
        mid = len(sorted_array)//2

        root = Node(sorted_array[mid])
        print(root.value)
        root.left = self.buildTree(sorted_array[:mid])
        root.right = self.buildTree(sorted_array[mid+1:])

        return root
    

