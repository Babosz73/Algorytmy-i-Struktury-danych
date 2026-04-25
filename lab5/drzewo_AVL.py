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
    
    def insert(self, key, value):
        self.root = self.insert2(self.root, key, value)
    
    def insert2(self, node, key, value):
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.left = self.insert2(node.left, key, value)
        elif key > node.key:
            node.right = self.insert2(node.right, key, value)
        else:
            node.value = value
            return node
        return self.rebalance(node)
    
    def delete(self, key):
        self.root = self.delete2(self.root, key)
        
    def delete2(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self.delete2(node.left, key)
        elif key > node.key:
            node.right = self.delete2(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                minimal_prawe = self.find_min_right_delete(node.right)
                node.key = minimal_prawe.key
                node.value = minimal_prawe.value
                node.right = self.delete2(node.right, minimal_prawe.key)
        return self.rebalance(node)
    


    def find_min_right_delete(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current    
        
            
    def print_as_list(self):
        result = []

        def traverse(node):
            if node is None:
                return
            
            traverse(node.left)
            result.append(f"{node.key}:{node.value}")
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
            

def main():
    tree = AVL()

    elementy = [
        (50,'A'), (15,'B'), (62,'C'), (5,'D'), (2,'E'), (1,'F'), (11,'G'), (100,'H'), (7,'I'), (6,'J'), (55,'K'), 
        (52,'L'),(51,'M'), (57,'N'), (8,'O'), (9,'P'), (10,'R'), (99,'S'), (12,'T')]

    for kl, va in elementy:
        tree.insert(kl, va)

    tree.print_tree()
    tree.print_as_list()

    print(tree.search(10))

    tree.delete(50)
    tree.delete(52)
    tree.delete(11)
    tree.delete(57)
    tree.delete(1)
    tree.delete(12)

    tree.insert(3, 'AA')
    tree.insert(4, 'BB')

    tree.delete(7)
    tree.delete(8)

    tree.print_tree()
    tree.print_as_list()

if __name__ == "__main__":
    main()

# W poleceniu pojawia się sformułowanie „wyświetl drzewo BST”, jednak z kontekstu zadania zrozumialem, że należy zaimplementować i testować drzewo AVL. 
# Dlatego wszystkie operacje takie jak insert, delete,  czy wyświetlanie zostały wykonane  na drzewie AVL, przynajmniej tak mi sie wydaje ze to jest barzdziej logiczne.