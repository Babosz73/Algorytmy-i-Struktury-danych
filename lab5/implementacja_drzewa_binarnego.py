class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
class BST:
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
        if self.root is None:
            self.root = Node(key, value)
            return 
        current = self.root
        while current is not None:
            if key == current.key:
                current.value = value
                return
            elif key < current.key:
                if current.left is None:
                    current.left = Node(key, value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(key, value)
                    return
                current = current.right

    def delete(self, key):
        parent = None
        current = self.root

        while current is not None and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
            
        if current is None:
            return

        if current.left is None and current.right is None:
            if parent is None:
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None

        elif current.left is None or current.right is None:
            if current.left is not None:
                child = current.left
            else:
                child = current.right
            if parent is None:
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child
        else:
            successor_parent = current
            successor = current.right

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            current.key = successor.key
            current.value = successor.value

            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
            
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

def main():
    tree = BST()
    data = [(50, 'A'),(15, 'B'),(62, 'C'),(5, 'D'),(20, 'E'),(58, 'F'),(91, 'G'),(3, 'H'),(8, 'I'),(37, 'J'),(60, 'K'),(24, 'L')]
    for key, value in data:
        tree.insert(key, value)
    tree.print_tree()
    tree.print_as_list()
    wartosc =tree.search(24)
    print(f"Wartość dla klucza 24: {wartosc}")
    tree.insert(20, "AA")
    tree.insert(6, "M")
    tree.delete(62)
    tree.insert(59, "N")
    tree.insert(100, "P")
    tree.delete(8)
    tree.delete(15)
    tree.insert(55, 'R')
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print("Wysokość drzewa:", tree.height())
    tree.print_as_list()
    tree.print_tree()

if __name__ == "__main__":
    main()