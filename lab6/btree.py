class BTreeNode:
    def __init__(self):
        self.keys = []
        self.children = []

    
    
class BTree:
    def __init__(self, max_children):
        self.root = BTreeNode()
        self.max_children = max_children
        self.max_keys = max_children - 1
    
    def _insert_key_node(self, node, key):
        node.keys.append(key)
        node.keys.sort()

    def split_node(self, node):
        mid_idx = len(node.keys) // 2

        mid_key  = node.keys[mid_idx]
        new_node = BTreeNode()
        new_node.keys = node.keys[mid_idx + 1:]
        node.keys = node.keys[:mid_idx]

        if len(node.children) > 0:
                new_node.children = node.children[mid_idx + 1:]
                node.children = node.children[:mid_idx + 1]
        
        return mid_key, new_node
    
    def add_to_node(self, node, key, new_child=None):
        i = 0
        while i < len(node.keys) and node.keys[i] < key:
            i += 1
        
        node.keys.insert(i, key)

        if new_child is not None:
            node.children.insert(i + 1, new_child)

         
        if len(node.keys) > self.max_keys:
            return self.split_node(node)
        return None
    
    def insert1(self, node, key):
        if len(node.children) == 0:
            return self.add_to_node(node, key)
        
        else:
            i=0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            
            result = self.insert1(node.children[i], key)

            if result is not None:
                mid_key, new_child = result
                return self.add_to_node(node, mid_key, new_child)

    def insert2(self, key):
        result = self.insert1(self.root, key)

        if result is not None:
            mid_key, new_child = result
            old_root = self.root
            new_root = BTreeNode()
            new_root.keys = [mid_key]
            new_root.children = [old_root, new_child]
            self.root = new_root
    
    def print_tree(self):
        print("==============")
        self._print_tree(self.root, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node is not None:
            for i in range(len(node.keys) + 1):
                if i < len(node.children):
                    self._print_tree(node.children[i], lvl + 1)

                if i < len(node.keys):
                    print(lvl * "  ", node.keys[i])


if __name__ == "__main__":
    tree1 = BTree(4)
    values1 = [5, 17, 2, 14, 7, 4, 12, 1, 16, 8, 11, 9, 6, 13, 0, 3, 18, 15, 10, 19]

    for value in values1:
        tree1.insert2(value)

    print("Drzewo 1:")
    tree1.print_tree()

    
    tree2 = BTree(4)

    for value in range(20):
        tree2.insert2(value)

    print("Drzewo 2:")
    tree2.print_tree()

    
    for value in range(20, 200):
        tree2.insert2(value)

    print("Drzewo 2 po dodaniu 20..199:")
    tree2.print_tree()

    
    tree3 = BTree(6)

    for value in range(200):
        tree3.insert2(value)

    print("Drzewo 3:")
    tree3.print_tree()