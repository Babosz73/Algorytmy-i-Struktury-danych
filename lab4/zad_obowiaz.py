class Element:
    def __init__(self, key, value):
        self.value = value
        self.key = key
    def __str__(self):
        return f"{self.key}:{self.value}"
        
class HashTable:
    def __init__(self, size, c1 = 1, c2 = 0):
        self.size = size
        self.c1 = c1
        self.c2 = c2
        self.tab = [None for i in range(size)]
    
    def hash_ASCII(self, key):
        if isinstance(key, str):
            total = 0
            for char in key:
                total += ord(char)
            return total % self.size
        else:
            return key % self.size
        
    def addres(self, hash_elem, i):
        return (hash_elem + self.c1*i + self.c2*i*i) % self.size
    
    def search(self, key):
        hash_elem = self.hash_ASCII(key)

        for i in range (self.size):
            index = self.addres(hash_elem, i)
        
            if self.tab[index] is None:
                return None
        
            if self.tab[index].key == key:
                return self.tab[index].value
    
        return None

    def insert(self, key, value):
        hash_elem = self.hash_ASCII(key)

        for i in range (self.size):
            index = self.addres(hash_elem, i)

            if self.tab[index] is None:
                self.tab[index] = Element(key, value)
                return
            
            if self.tab[index].key == key:
                self.tab[index].value = value
                return
        print("brak miejsca")


    def remove(self, key):
        hash_elem = self.hash_ASCII(key)

        for i in range(self.size):
            index = self.addres(hash_elem, i)

            if self.tab[index] is None:
                return False
            
            if self.tab[index].key == key:
                self.tab[index] = None
                return True
        return False
    
    def __str__(self):
        result = "{"

        for i in range(self.size):
            if self.tab[i] is None:
                result += "None"
            else:
                result += f"{self.tab[i].key}:{self.tab[i].value}"
            
            if i != self.size - 1:
                result += ", "
        result += "}"

        return result



        
    







        
    
