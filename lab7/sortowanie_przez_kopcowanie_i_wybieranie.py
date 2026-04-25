import random
import time

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
    def __init__(self, tab = None):
        if tab is None:
            self.__tab = []
            self.__heap_size = 0
        else:
            self.__tab = tab
            self.__heap_size = len(tab)
        
            for i in range(self.parent(self.__heap_size - 1), -1, -1):
                self.heap_down(i)
    
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
            self.__tab[0], self.__tab[self.__heap_size - 1] = self.__tab[self.__heap_size - 1], self.__tab[0]
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

def sort_swap(tab):
    for i in range(len(tab)):
        min_idx = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min_idx]:
                min_idx = j
        tab[i], tab[min_idx] = tab[min_idx], tab[i]

def sort_shift(tab):
    for i in range(len(tab)):
        min_idx = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[min_idx]:
                min_idx = j
        elem = tab.pop(min_idx)
        tab.insert(i, elem)
              

def main():
    test = int(input("Podaj numer testu (1 lub 2): "))

    if test == 1:
        print("===== TEST 1 =====")

        dane = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'),
                (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]

        tab = [Elem(value, key) for key, value in dane]

        kopiec = Prioritory_Queue(tab)

        print("Kopiec jako tablica:")
        kopiec.print_tab()

        print("\nKopiec jako drzewo:")
        kopiec.print_tree(0, 0)

        while not kopiec.is_empty():
            kopiec.dequeue()

        print("\nPosortowana tablica:")
        print(tab)

        print("\nStabilność:")
        print("NIESTABILNE")

        print("\n===== SORT SWAP =====")

        tab_swap = [Elem(value, key) for key, value in dane]
        sort_swap(tab_swap)

        print("Posortowana tablica:")
        print(tab_swap)

        print("\nStabilnosc:")
        print("NIESTABILNE")

        print("\n===== SORT SHIFT =====")

        tab_shift = [Elem(value, key) for key, value in dane]
        sort_shift(tab_shift)

        print("Posortowana tablica:")
        print(tab_shift)

        print("\nStabilnosc:")
        print("STABILNE")

    elif test == 2:
        print("===== TEST 2 =====")

        tab = [int(random.random() * 100) for _ in range(10000)]

        tab_heap = tab.copy()
        tab_swap = tab.copy()
        tab_shift = tab.copy()

        t_start = time.perf_counter()
        kopiec = Prioritory_Queue(tab_heap)
        while not kopiec.is_empty():
            kopiec.dequeue()
        t_stop = time.perf_counter()
        print("Heapsort czas:", "{:.7f}".format(t_stop - t_start))

        t_start = time.perf_counter()
        sort_swap(tab_swap)
        t_stop = time.perf_counter()
        print("Selection sort (swap) czas:", "{:.7f}".format(t_stop - t_start))

        t_start = time.perf_counter()
        sort_shift(tab_shift)
        t_stop = time.perf_counter()
        print("Selection sort (shift) czas:", "{:.7f}".format(t_stop - t_start))


if __name__ == "__main__":
    main()