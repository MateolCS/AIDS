import sys
from tree import Tree
from node import Node

from timeit import default_timer as timer

sys.setrecursionlimit(200000)
class RandomTree(Tree):
    def __init__(self, array) -> None:
        self.root = self.build_tree(array)

    def build_tree(self, array):
        root = Node(array[0])
        for i in range(1, len(array)):
            self.insert_value(root, array[i])

        return root


    def find_subtree(self, value):
        current_node = self.root


        while current_node is not None and current_node.value != value:
            if value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left

        print(f"Height: {self.get_height(current_node)}")
        print(self.get_preorder(current_node))

    def get_height(self, root):
        if root is None:
            return 0
        
        left = self.get_height(root.left)
        right = self.get_height(root.right)

        return max(left, right) + 1
    

    def get_min(self, node):
        if node is None:
            return None, []

        minimum = float('inf')
        path = []

        def dfs(node, current_path):
            nonlocal minimum, path

            if node is None:
                return

            current_path.append(node.value)

            if node.value < minimum:
                minimum = node.value
                path = list(current_path)

            dfs(node.left, current_path)
            dfs(node.right, current_path)

            current_path.pop()

        dfs(node, [])
        return minimum
    
    def get_max(self, node):
        start = timer()
        if node is None:
            return None, []

        maximum = float('-inf')
        path = []

        def dfs(node, current_path):
            nonlocal maximum, path

            if node is None:
                return

            current_path.append(node.value)

            if node.value > maximum:
                maximum = node.value
                path = list(current_path)

            dfs(node.left, current_path)
            dfs(node.right, current_path)

            current_path.pop()

        dfs(node, [])
        return maximum
    
    def count_level(self,value, level=0):
        current_node = self.root

        while current_node is not None and current_node.value != value:
            if value > current_node.value:
                current_node = current_node.right
                level = level + 1
            elif value < current_node.value:
                current_node = current_node.left
                level = level + 1

        return level
    
    def get_all_level_nodes(self, value):
        current_node = self.root
        level = self.count(value)
        all_nodes = self.nodes_at_level(current_node, level)
        self.delete(self.root, value)
        return f"Level: {level} nodes: {all_nodes}"
    
    def count(self, value, level=0, current_node=None):
        if current_node is None:
            current_node = self.root
        
        if current_node is None:
            return -1  # Value not found in the tree
        
        if current_node.value == value:
            return level  # Value found, return the current level
        
        # Recursively search left and right subtrees
        left_level = self.count(value, level + 1, current_node.left)
        right_level = self.count(value, level + 1, current_node.right)
        
        # Return the maximum of left and right levels
        return max(left_level, right_level)
    
    def build_bst(self, arranew_node):
        if len(arranew_node) == 0:
            return None
 
        sorted_arranew_node = sorted(arranew_node)
        mid = len(sorted_arranew_node)//2

        root = Node(sorted_arranew_node[mid])
        root.left = self.build_bst(sorted_arranew_node[:mid])
        root.right = self.build_bst(sorted_arranew_node[mid+1:])

        return root
    
    def rebalance(self):
        self.root = self.build_bst(self.get_inorder(self.root))
    