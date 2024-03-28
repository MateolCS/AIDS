from node import Node
from timeit import default_timer as timer
import math
class Tree:
    def __init__(self, arranew_node) -> None:
        self.root = self.build_tree(arranew_node)

    def build_tree(self, arranew_node):
        if len(arranew_node) == 0:
            return None
 
        sorted_arranew_node = sorted(arranew_node)
        mid = len(sorted_arranew_node)//2

        root = Node(sorted_arranew_node[mid])
        root.left = self.build_tree(sorted_arranew_node[:mid])
        root.right = self.build_tree(sorted_arranew_node[mid+1:])

        return root
    
    def get_min(self):
        start = timer()
        current_node = self.root
        path = []

        while current_node.left != None:
            path.append(current_node.value)
            current_node = current_node.left
        end = timer()
        return f'Minimum: {current_node.value}, path: {path} time: {end-start}'

    def get_max(self):
        start = timer()
        current_node= self.root
        path= []
        while current_node.right != None:
            path.append(current_node.value)
            current_node = current_node.right
        end = timer()
        return f'Maxinmum: {current_node.value}, path: {path} time: {end-start}'

    def get_inorder(self, node):
        result = []
        stack = []
        current_node = node
    
        while current_node is not None or len(stack) > 0:
            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            result.append(current_node.value)
            current_node = current_node.right
        
        return result
    
    def get_decreasing(self, node):
        result = []
        stack = []
        current_node = node
    
        while current_node is not None or len(stack) > 0:
            while current_node is not None:
                stack.append(current_node)
                current_node = current_node.right
            current_node = stack.pop()
            result.append(current_node.value)
            current_node = current_node.left
        
        return result
    
    def get_postorder(self, node):
        result = []

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.value)

        traverse(node)
        return result
    
    def get_preorder(self, node):
        result = []
        stack = []
        current_node = node
    
        while current_node is not None or len(stack) > 0:
            while current_node is not None:
                result.append(current_node.value)
                stack.append(current_node)
                current_node = current_node.right
            current_node = stack.pop()
            current_node = current_node.left
        
        return result

    def insert_value(self, root ,value):
        if root == None:
            return Node(value)
        
        if value > root.value:
            root.right = self.insert_value(root.right, value)
        
        if value < root.value:
            root.left = self.insert_value(root.left, value)

        return root

    def delete(self, node, value):
        if not node:
            return node
        
        if value > node.value:
            node.right = self.delete(node.right, value)
        elif value < node.value:
            node.left = self.delete(node.left, value)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            
            current_node = node.right
            while current_node.left:
                current_node = current_node.left

            node.value = current_node.value
            node.right = self.delete(node.right, node.value)
        
        return node
        

    def rotate_left(self, node):
        new_node = node.right
        temp = new_node.left
        new_node.left = node
        node.right = temp
        node.height = 1 + max(self.get_height(node.left),
                           self.get_height(node.right))
        new_node.height = 1 + max(self.get_height(new_node.left),
                           self.get_height(new_node.right))
        return new_node

    
    def rotate_right(self, node):
        new_node = node.left
        temp = new_node.right
        new_node.right = node
        node.left = temp
        node.height = 1 + max(self.get_height(node.left),
                           self.get_height(node.right))
        new_node.height = 1 + max(self.get_height(new_node.left),
                           self.get_height(new_node.right))
        return new_node

    def balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)


    def rebalance(self):
        start = timer()
        self.root = self.build_tree(self.get_inorder(self.root))
        end = timer()

        return end - start
        

    def count_level(self,value, level=0):
        current_node = self.root

        while current_node.value != value:
            if value > current_node.value:
                current_node = current_node.right
                level = level + 1
            elif value < current_node.value:
                current_node = current_node.left
                level = level + 1

        return level
    

    def get_all_level_nodes(self, value):
        current_node = self.root
        level = self.count_level(value)
        all_nodes = self.nodes_at_level(current_node, level)
        self.delete(self.root, value)
        return f"Level: {level} nodes: {all_nodes}"


    def nodes_at_level(self, root, target_level):
        if root is None:
            return []

        queue = [(root, 0)]  # Initialize a queue for level-order traversal
        result = []

        while queue:
            node, level = queue.pop(0)  # Dequeue the front node and its level

            if level == target_level:
                result.append(node.value)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result
    
    def find_subtree(self, value):
        current_node = self.root


        while current_node.value != value:
            if value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left
        
        print(f"Heigth: {self.get_height(current_node)}")
        print(self.get_preorder(current_node))



    def delete_postorder(self, node, value):
        if not node:
            return None

        node.left = self.delete_postorder(node.left, value)
        node.right = self.delete_postorder(node.right, value)  
                
        if node.value == value:
            node.left = None
            node.right = None
            return None

        return node
    
    def find_and_delete(self, value):
        self.find_subtree(value)
        self.delete_postorder(self.root, value)
        

    def get_height(self, root):
        if root is None:
            return 0
        
        left = self.get_height(root.left)
        right = self.get_height(root.right)

        return max(left, right) +1
    
    def all_right(self, prime):
        counter = 0
        placeholder = prime.right
        while placeholder:
            if placeholder.left:
                placeholder2 = placeholder
                placeholder = placeholder.left
                placeholder2.left = placeholder.right
                placeholder.right = placeholder2
                prime.right = placeholder
            else:
                counter += 1
                prime = placeholder
                placeholder = placeholder.right
        return counter


    def handle_turn(self, prime, m):
        placeholder = prime.right
        for i in range(m):
            placeholder2 = placeholder
            placeholder = placeholder.right
            prime.right = placeholder
            placeholder2.right = placeholder.left
            placeholder.left = placeholder2
            prime = placeholder
            placeholder = placeholder.right
    
    def correct_balance(self, start):
        prime = Node(0)
        prime.right = start
        count = self.all_right(prime)
        h = int(math.log2(count + 1))
        m = pow(2, h) - 1
        self.handle_turn(prime, count - m)
        for m in [m // 2 ** i for i in range(1, h + 1)]:
            self.handle_turn(prime, m)
        return prime.right

    
    def print_tree(self):
        self.get_tree(self.root, 0)

    def get_tree(self, node, level):
        if node is None:
            return
        self.get_tree(node.right, level + 1)
        print("    " * level + str(node.value))
        self.get_tree(node.left, level + 1)
