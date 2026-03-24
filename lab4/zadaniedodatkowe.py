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
        
        