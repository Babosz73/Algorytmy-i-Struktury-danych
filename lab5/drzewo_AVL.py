class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
class AVL:
    def __init__(self):
        self.root = None
    
    def search(self, key):
        current = self.root
        while current is not None:
            if key == current.key:
                return current.value
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None
    
    #napisz def insert
        
    #napisz def delete
        
            
    def print_as_list(self):
        result = []

        def traverse(node):
            if node is None:
                return
            
            traverse(node.left)
            result.append(f"{node.key} {node.value}")
            traverse(node.right)

        traverse(self.root)
        print(", ".join(result))
    
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node is not None:
            self.__print_tree(node.right, lvl + 5)

            print()
            print(lvl * " ", node.key, node.value)

            self.__print_tree(node.left, lvl + 5)
    
    def height(self):
        def h(node):
            if node is None:
                return 0

            left_height = h(node.left)
            right_height = h(node.right)
            return max(left_height, right_height) + 1
        return h(self.root)
    
    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right)
                                  
                                  )
    def get_height(self,node):
        if node is None:
            return 0
        return node.height
    
    def calculate_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def rotate_right(self, node):
        new_root = node.left
        temp = new_root.right

        new_root.right = node
        node.left = temp

        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def rotate_left(self, node):
        new_root = node.right
        temp = new_root.left

        new_root.left = node
        node.right = temp

        self.update_height(node)
        self.update_height(new_root)
        return new_root
    
    def rebalance(self, node):
        self.update_height(node)
        balance = self.calculate_balance(node)
        if balance == 2:
            if self.calculate_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
            else:
                return self.rotate_right(node)
        elif balance == -2:
            if self.calculate_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)
            else:
                return self.rotate_left(node)
        return node
            

