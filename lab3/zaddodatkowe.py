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
            self.tab[i] = self.tab[i + 1]

        self.tab[self.count - 1] = None
        self.count -= 1
        return value


class UnrolledLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def print_list(self):
        current = self.head
        result = []

        while current is not None:
            node_str = "["
            for i in range(current.count):
                node_str += str(current.tab[i]) + " "
            node_str = node_str.strip() + "]"
            result.append(node_str)
            current = current.next

        print("  ".join(result))

    def get(self, index):
        if index < 0 or index >= self.size:
            return None

        current = self.head

        while current is not None:
            if index < current.count:
                return current.tab[index]
            index -= current.count
            current = current.next

        return None

    def insert(self, index, elem):
        if index < 0:
            return False

        if index > self.size:
            index = self.size

        if self.head is None:
            self.head = Node()
            self.head.insert(0, elem)
            self.size += 1
            return True

        current = self.head
        prev = None

        while current is not None:
            if index <= current.count:
                if current.count < size:
                    current.insert(index, elem)
                    self.size += 1
                    return True

                new_node = Node()
                half = size // 2

                for i in range(half, size):
                    new_node.tab[i - half] = current.tab[i]
                    new_node.count += 1
                    current.tab[i] = None

                current.count = half
                new_node.next = current.next
                current.next = new_node

                if index <= current.count:
                    current.insert(index, elem)
                else:
                    new_node.insert(index - current.count, elem)

                self.size += 1
                return True

            index -= current.count
            prev = current
            current = current.next

        if prev.count < size:
            prev.insert(prev.count, elem)
        else:
            new_node = Node()
            new_node.insert(0, elem)
            prev.next = new_node

        self.size += 1
        return True

    def delete(self, index):
        if index < 0 or index >= self.size or self.head is None:
            return None
        
        current = self.head
        prev = None

        while current is not None:
            if index < current.count:
                value = current.delete(index)
                self.size -= 1
                
                if current.count == 0:
                    if prev is None:
                        self.head = current.next
                    else:
                        prev.next = current.next
                    return value
                
                half = size // 2
                target = half + 1

                if current.count < half and current.next is not None:
                    next_node = current.next

                    if current.count + next_node.count <= size:
                        for i in range(next_node.count):
                            current.tab[current.count] = next_node.tab[i]
                            current.count += 1

                        current.next = next_node.next
                    else:
                        while current.count < target and next_node.count > 0:
                            current.tab[current.count] = next_node.tab[0]
                            current.count += 1
                            next_node.delete(0)
                        if next_node.count < half:
                            for i in range(next_node.count):
                                current.tab[current.count] = next_node.tab[i]
                                current.count += 1
                            current.next = next_node.next
                return value
            index -= current.count
            prev = current
            current = current.next
        return None

def main():
    lista = UnrolledLinkedList()

    print("--------------- TWORZENIE LISTY -------------------")
    for i in range(1, 10):
        lista.insert(lista.size, i)
    print("Lista po dodaniu od 1 do9:")
    lista.print_list()

    print("\n--------------- GET -------------------")
    print("Element o indeksie 4:", lista.get(4))

    print("\n--------------- INSERT -------------------")
    print("Wstawiam 10 na indeks 1")
    lista.insert(1, 10)
    lista.print_list()

    print("\nWstawiam 11 na indeks 8")
    lista.insert(8, 11)
    lista.print_list()

    print("\n--------------- DELETE -------------------")
    print("Usuwam element z indeksu 1")
    lista.delete(1)
    lista.print_list()

    print("\nUsuwam element z indeksu 2")
    lista.delete(2)
    lista.print_list()

if __name__ == "__main__":
    main()