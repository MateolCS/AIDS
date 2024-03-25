from node import Node

class Tree:
    def __init__(self, array) -> None:
        self.root = self.buildTree(array)

    def buildTree(self, array):
        if len(array) == 0:
            return None
 
        sorted_array = sorted(array)
        mid = len(sorted_array)//2

        root = Node(sorted_array[mid])
        root.left = self.buildTree(sorted_array[:mid])
        root.right = self.buildTree(sorted_array[mid+1:])

        return root
    
    def get_min(self):
        current_node = self.root
        path = []
        path.append(current_node.value)

        while current_node.left != None:
            path.append(current_node.value)
            current_node = current_node.left

        return f'Minimum: {current_node.value}, path: {path}'

    def get_max(self):
        current_node = self.root
        path= []
        path.append(current_node.value)
        while current_node.right != None:
            path.append(current_node.value)
            current_node = current_node.right

        return f'Maxinmum: {current_node.value}, path: {path}'


    def traverse_preorder(self, node):
        if node == None:
            return
        
        print(node.value)
        self.traverse_preorder(node.left)
        self.traverse_preorder(node.right)

        

    def traverse_inorder(self, node):
        if node == None:
            return
        
        self.traverse_inorder(node.left)
        print(node.value)
        self.traverse_inorder(node.right)

    def traverse_postorder(self, node):
        if node == None:
            return
        
        self.traverse_postorder(node.left)
        self.traverse_postorder(node.right)
        print(node.value)

    def insert_value(self, root ,value):
        if root == None:
            return Node(value)
        
        if value > root.value:
            root.right = self.insert_value(root, value)
        
        if value < root.value:
            root.left = self.insert_value(root, value)

        return root

    def delete(self, node, value):
        if node is None:
            return node
        
        if value < node.value:
            node.left = self.delete(node, value)
        elif value > node.value:
            node.right = self.delete(node, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

        node.value = self.inorder_successor(node.right)
        node.right = self.delete(node.right, node.value)
        
        return node

    def inorder_successor(self, node):
        current_node = node.value

        while current_node.left is not None:
            current_node = node.left

        return current_node
        

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass

    def balance(self):
        pass

    
    def print_tree(self):
        self.get_tree(self.root, 0)

    def get_tree(self, node, level):
        if node is None:
            return
        self.get_tree(node.right, level + 1)
        print("    " * level + str(node.value))
        self.get_tree(node.left, level + 1)
