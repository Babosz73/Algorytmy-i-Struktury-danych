size = 6
class Node:
    def __init__(self):
        self.tab = [None] * size
        self.count = 0
        self.next = None
    
    def insert(self, index, elem):
        if self.count == size or index < 0 or index > self.count:
            return False
        
        for i in range(self.count, index, -1):
            self.tab[i] = self.tab[i - 1]
        self.tab[index] = elem
        self.count += 1
        return True

    def delete(self, index):
        if self.count == 0 or index < 0 or index >= self.count:
            return None
        
        value = self.tab[index]
        for i in range(index, self.count - 1):
            self.tab[i] = self.tab[i +1]
        self.tab[self.count - 1] = None
        self.count -= 1
        return value