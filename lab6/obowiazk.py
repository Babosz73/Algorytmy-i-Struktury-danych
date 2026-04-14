class Elem:
    def __init__(self, dane, priorytet):
        self.__dane = dane
        self.__priorytet = priorytet

    def __lt__(self, other):
        return self.__priorytet < other.__priorytet

    def __gt__(self, other):
        return self.__priorytet > other.__priorytet

    def __repr__(self):
        return f"{self.__priorytet} : {self.__dane}"

class Prioritory_Queue:
    def __init__(self):
        self.__tab = []
        self.__heap_size = 0
    
    def left(self, idx):
        return 2 * idx + 1

    def right(self, idx):
        return 2 * idx + 2
    
    def parent(self, idx):
        return (idx - 1) // 2

    def is_empty(self):
        return self.__heap_size == 0
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.__tab[0]
        
    def heap_down(self, idx):
        largest = idx
        left_idx = self.left(idx)
        right_idx = self.right(idx)

        if left_idx < self.__heap_size and self.__tab[left_idx] > self.__tab[largest]:
            largest = left_idx

        if right_idx < self.__heap_size and self.__tab[right_idx] > self.__tab[largest]:
            largest = right_idx

        if largest != idx:
            self.__tab[idx], self.__tab[largest] = self.__tab[largest], self.__tab[idx]
            self.heap_down(largest)

    
    def dequeue(self):
        if self.is_empty():
            return None
        
        else:
            naj_elem = self.__tab[0]
            self.__tab[0] = self.__tab[self.__heap_size - 1]
            self.__heap_size -= 1
            self.heap_down(0)

            return naj_elem
        
    def heap_up(self, idx):
        if idx <= 0:
            return
        parent_idx = self.parent(idx)

        if idx > 0 and self.__tab[idx] > self.__tab[parent_idx]:
            self.__tab[idx], self.__tab[parent_idx] = self.__tab[parent_idx], self.__tab[idx]
            self.heap_up(parent_idx)
    
    def enqueue(self, elem):
        if self.__heap_size == len(self.__tab):
            self.__tab.append(elem)
        else:
            self.__tab[self.__heap_size] = elem

        self.__heap_size += 1
        self.heap_up(self.__heap_size - 1)
    
    def print_tab(self):
        print('{', end=' ')
        print(*self.__tab[:self.__heap_size], sep=', ', end=' ')
        print('}')


    def print_tree(self, idx, lvl):
        if idx < self.__heap_size:
            self.print_tree(self.right(idx), lvl + 1)
            print(2 * lvl * '  ', self.__tab[idx] if self.__tab[idx] else None)
            self.print_tree(self.left(idx), lvl + 1)
            
def main():
    kol_prior = Prioritory_Queue()

    priorytety = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    litery = "GRYMOTYLA"

    for i in range(len(priorytety)):
        elem = Elem(litery[i], priorytety[i])
        kol_prior.enqueue(elem)

    kol_prior.print_tree(0, 0)
    kol_prior.print_tab()

    pierwszy_usuniety = kol_prior.dequeue()

    print(kol_prior.peek())

    kol_prior.print_tab()

    print(pierwszy_usuniety)

    while not kol_prior.is_empty():
        print(kol_prior.dequeue())

    kol_prior.print_tab()

if __name__ == "__main__":
    main()
    
    