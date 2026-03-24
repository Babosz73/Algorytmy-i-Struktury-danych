import random
def randomLevel(p, maxLevel):   
    lvl = 1
    while random.random() < p and lvl < maxLevel:
        lvl = lvl + 1
    return lvl

class Element:
    def __init__(self, key, data, level):
        self.key = key
        self.data = data
        self.level = level
        self.tab = [None] * level


class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.head = Element(None, None, max_level)

    def search(self,key):
        current = self.head

        for lvl in range(self.max_level - 1, -1, -1):
            while current.tab[lvl] is not None and current.tab[lvl].key < key:
                current = current.tab[lvl]
        
        current = current.tab[0]
        if current is not None and current.key == key:
            return current.data

        return None
    
    def insert(self, key, data):
        update = [None] * self.max_level
        current = self.head

        for lvl in range(self.max_level - 1, -1, -1):
            while current.tab[lvl] is not None and current.tab[lvl].key < key:
                current = current.tab[lvl]
            update[lvl] = current

        current = current.tab[0]

        if current is not None and current.key == key:
            current.data = data
            return

        new_level = randomLevel(0.5, self.max_level)
        new_element = Element(key, data, new_level)

        for lvl in range(new_level):
            new_element.tab[lvl] = update[lvl].tab[lvl]
            update[lvl].tab[lvl] = new_element
        
    def remove(self, key):
        update = [None] * self.max_level
        current = self.head

        for lvl in range(self.max_level - 1, -1, -1):
            while current.tab[lvl] is not None and current.tab[lvl].key < key:
                current = current.tab[lvl]
            update[lvl] = current

        current = current.tab[0]

        if current is None or current.key != key:
            return

        for lvl in range(len(current.tab)):
            if update[lvl].tab[lvl] == current:
                update[lvl].tab[lvl] = current.tab[lvl]
    def __str__(self):
        result = []
        node = self.head.tab[0]

        while node is not None:
            result.append(f"({node.key}:{node.data})")
            node = node.tab[0]

        return " ".join(result)
    def displayList_(self):
        node = self.head.tab[0]  # pierwszy element na poziomie 0
        keys = [ ]                        # lista kluczy na tym poziomie
        while node is not None:
            keys.append(node.key)
            node = node.tab[0]

        for lvl in range(self.max_level - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node is not None:
                while node.key > keys[idx]:
                    print(end=5*" ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.data:2s}", end="")
                node = node.tab[lvl]
            print()
        
import random

def randomLevel(p, maxLevel):   
    lvl = 1
    while random.random() < p and lvl < maxLevel:
        lvl = lvl + 1
    return lvl


class Element:
    def __init__(self, key, data, level):
        self.key = key
        self.data = data
        self.level = level
        self.tab = [None] * level


class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.head = Element(None, None, max_level)

    def search(self, key):
        current = self.head

        for lvl in range(self.max_level - 1, -1, -1):
            while current.tab[lvl] is not None and current.tab[lvl].key < key:
                current = current.tab[lvl]

        current = current.tab[0]
        if current is not None and current.key == key:
            return current.data

        return None

    def insert(self, key, data):
        update = [None] * self.max_level
        current = self.head

        for lvl in range(self.max_level - 1, -1, -1):
            while current.tab[lvl] is not None and current.tab[lvl].key < key:
                current = current.tab[lvl]
            update[lvl] = current

        current = current.tab[0]

        if current is not None and current.key == key:
            current.data = data
            return

        new_level = randomLevel(0.5, self.max_level)
        new_element = Element(key, data, new_level)

        for lvl in range(new_level):
            new_element.tab[lvl] = update[lvl].tab[lvl]
            update[lvl].tab[lvl] = new_element

    def remove(self, key):
        update = [None] * self.max_level
        current = self.head

        for lvl in range(self.max_level - 1, -1, -1):
            while current.tab[lvl] is not None and current.tab[lvl].key < key:
                current = current.tab[lvl]
            update[lvl] = current

        current = current.tab[0]

        if current is None or current.key != key:
            return

        for lvl in range(len(current.tab)):
            if update[lvl].tab[lvl] == current:
                update[lvl].tab[lvl] = current.tab[lvl]

    def __str__(self):
        result = []
        node = self.head.tab[0]

        while node is not None:
            result.append(f"({node.key}:{node.data})")
            node = node.tab[0]

        return " ".join(result)

    def displayList_(self):
        node = self.head.tab[0]
        keys = []
        while node is not None:
            keys.append(node.key)
            node = node.tab[0]

        for lvl in range(self.max_level - 1, -1, -1):
            print(f"{lvl}  ", end=" ")
            node = self.head.tab[lvl]
            idx = 0
            while node is not None:
                while idx < len(keys) and node.key > keys[idx]:
                    print(end=5 * " ")
                    idx += 1
                idx += 1
                print(f"{node.key:2d}:{node.data:2s}", end="")
                node = node.tab[lvl]
            print()


def main():
    random.seed(42)

    print("PIERWSZY TEST 1 do 15")
    skip_list = SkipList(5)

    for i in range(1, 16):
        skip_list.insert(i, chr(64 + i))

    print(skip_list)
    print(skip_list.search(2))

    skip_list.insert(2, 'Z')
    print(skip_list.search(2))

    skip_list.remove(5)
    skip_list.remove(6)
    skip_list.remove(7)

    print(skip_list)

    skip_list.insert(6, 'W')
    print(skip_list)

    print("\nWszystkie poziomy:")
    skip_list.displayList_()

    print("\nDRUGI TEST 15 do1 ")
    skip_list_2 = SkipList(5)

    for i in range(15, 0, -1):
        skip_list_2.insert(i, chr(64 + i))

    print(skip_list_2)
    print(skip_list_2.search(2))

    skip_list_2.insert(2, 'Z')
    print(skip_list_2.search(2))

    skip_list_2.remove(5)
    skip_list_2.remove(6)
    skip_list_2.remove(7)

    print(skip_list_2)

    skip_list_2.insert(6, 'W')
    print(skip_list_2)

    print("\nWszystkie poziomy:")
    skip_list_2.displayList_()


if __name__ == "__main__":
    main()