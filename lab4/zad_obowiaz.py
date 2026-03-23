class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"{self.key}:{self.value}"


class HashTable:
    def __init__(self, size, c1=1, c2=0):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.tab = [None for i in range(size)]
        self.deleted = 'Deleted'

    def hash_ASCII(self, key):
        if isinstance(key, str):
            total = 0
            for char in key:
                total += ord(char)
            return total % self.size
        return key % self.size

    def addres(self, hash_elem, i):
        return (hash_elem + self.c1 * i + self.c2 * i * i) % self.size

    def search(self, key):
        hash_elem = self.hash_ASCII(key)

        for i in range(self.size):
            index = self.addres(hash_elem, i)

            if self.tab[index] is None:
                return None
            
            if self.tab[index] ==  self.deleted:
                continue

            if self.tab[index].key == key:
                return self.tab[index].value

        return None

    def insert(self, key, value):
        hash_elem = self.hash_ASCII(key)

        for i in range(self.size):
            index = self.addres(hash_elem, i)

            if self.tab[index] is None or self.tab[index] == self.deleted:
                self.tab[index] = Element(key, value)
                return True

            if self.tab[index].key == key:
                self.tab[index].value = value
                return True

        return None

    def remove(self, key):
        hash_elem = self.hash_ASCII(key)

        for i in range(self.size):
            index = self.addres(hash_elem, i)

            if self.tab[index] is None:
                return None
            
            if self.tab[index] == self.deleted:
                continue

            if self.tab[index].key == key:
                self.tab[index] = self.deleted
                return True

        return None

    def __str__(self):
        result = "{"

        for i in range(self.size):
            if self.tab[i] is None:
                result += "None"
            elif self.tab[i] == self.deleted:
                result += 'Deleted'
        
            else:
                result += f"{self.tab[i].key}:{self.tab[i].value}"

            if i != self.size - 1:
                result += ", "

        result += "}"
        return result
    
def func_test1(size, c1, c2):
    h = HashTable(size, c1, c2)

    keys = [1, 2, 3, 4, 5, 18, 31, 8, 9, 10, 11, 12, 13, 14, 15]
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

    for i in range(len(keys)):
        if h.insert(keys[i], values[i]) is None:
            print("Brak miejsca")

    print(h)

    print(h.search(5))
    print(h.search(14))

    if h.insert(5, 'Z') is None:
        print("Brak miejsca")

    print(h.search(5))

    if h.remove(5) is None:
        print("Brak danej")

    print(h)

    print(h.search(31))

    if h.insert("test", "W") is None:
        print("Brak miejsca")
    
    print(h)

def func_test2(size, c1, c2):
    h = HashTable(size, c1, c2)

    keys = [13 * i for i in range(1, 16)]
    values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

    for i in range(len(keys)):
        if h.insert(keys[i], values[i]) is None:
            print("Brak miejsca")

    print(h)


def main():
    print("Test funkca 1 - liniowe")
    func_test1(13, 1, 0)
    print("\n----------------------------------------------------------------------------------------")

    print("\nTest funkcja 2 - liniowe")
    func_test2(13, 1, 0)
    print("\n----------------------------------------------------------------------------------------")

    print("\nTest funkcja 2 - kwadratowe")
    func_test2(13, 0, 1)
    print("\n----------------------------------------------------------------------------------------")

    print("\nTest 1 funkcja - kwadratowe")
    func_test1(13, 0, 1)


main()