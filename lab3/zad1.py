class Queue:
    def __init__(self):
        self.tab = [None for i in range(5)]
        self.size = 5
        self.read = 0
        self.write = 0
        
    def is_empty(self):
        return self.read == self.write
    def peek(self):
        if self.is_empty():
            return None
        return self.tab[self.read]
    def dequeue(self):
        if self.is_empty():
            return None
        value = self.tab[self.read]
        self.tab[self.read] = None
        self.read = (self.read + 1) % self.size
        return value
    def enqueue(self, element):
        self.tab[self.write] = element
        self.write = (self.write + 1) % self.size

        if self.write == self.read:
            old_tab = self.tab
            old_size = self.size

            self.tab = [None for i in range(old_size * 2)]
            for i in range(self.write):
                self.tab[i] = old_tab[i]
            
            for i in range(self.read, old_size):
                self.tab[i + old_size] = old_tab[i]
            
            self.read = self.read + old_size
            self.size = 2 * old_size
    
    def __str__(self):
        if self.is_empty():
            return "[]"

        i = self.read
        result = []

        while i != self.write:
            result.append(self.tab[i])
            i = (i + 1) % self.size

        return str(result)        

def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print(q.dequeue())
    print(q.peek())
    print(q)

    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    print(q.tab)

    while not q.is_empty():
        print(q.dequeue())
    
    print(q)
    
if __name__ == "__main__":
    main()