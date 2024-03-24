from node import Node

class Tree:
    def __init__(self, array) -> None:
        self.root = self.build_tree(array)

    def build_tree(self, array):
        if len(array) == 0:
            return None

        sorted_array = sorted(array)

        mid = len(sorted_array)//2

        root = Node(sorted_array[mid])
        root.left = self.build_tree(sorted_array[:mid])
        root.right = self.build_tree(sorted_array[mid+1:])

        return root
    
    def print_tree(self):
        self.get_tree(self.root, 0)

    def get_tree(self, node, level):
        if node is None:
            return
        self.get_tree(node.right, level + 1)
        print("    " * level + str(node.value))
        self.get_tree(node.left, level + 1)

    
    def find_min(self):
        curr_node = self.root
        path = []
        while(curr_node.left != None):
            path.append(curr_node.value)
            curr_node = curr_node.left

        return f'Minimu: {curr_node.value}, path: {path}'
    
    def find_max(self):
        curr_node = self.root
        path = []

        while(curr_node.right != None):
            path.append(curr_node.value)
            curr_node = curr_node.right

        #return  f'Maximum: {curr_node.value}, path: {path}'
        return curr_node
    
    def get_height(self, root, value, level=0):
        if root is None:
            return 0
        if root.value == value:
            return level
        left_level = self.get_height_of_value(root.left, value, level + 1)
        if left_level != 0:
            return left_level
        return self.get_height_of_value(root.right, value, level + 1)
        
tree = Tree([1, 2, 4, 8, 16, 32, 64, 128, 256, 512])
tree.print_tree()
max_val = tree.find_max()
print(tree.get_height(tree.root, 32))