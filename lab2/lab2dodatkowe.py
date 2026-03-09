class Elem:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def destroy(self):
        current = self.head
        while current is not None:
            next_elem = current.next
            current.prev = None
            current.next = None
            current = next_elem
        self.head = None
        self.tail = None
    
    def add(self, data):
        new_elem = Elem(data)
        if self.head is None: 
            self.head = new_elem
            self.tail = new_elem
        else:
            new_elem.next = self.head
            new_elem.prev = None
            self.head.prev = new_elem
            self.head = new_elem
    
    def append(self,data):
        last_elem = Elem(data)

        if self.head is None:
            self.head = last_elem
            self.tail = last_elem
        else:
            last_elem.prev = self.tail
            last_elem.next = None
            self.tail.next = last_elem
            self.tail = last_elem

    def remove(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            removed = self.head
            self.head = None
            self.tail = None
            return removed.data
        else:
            removed = self.head
            self.head = self.head.next
            self.head.prev = None
            return removed.data

    def remove_end(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            removed = self.head
            self.head = None
            self.tail = None
            return removed.data
        else:
            removed = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return removed.data
    
    def is_empty(self):
        return self.head is None
    
    def length(self):
        if self.head is None:
            return 0
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def get(self):
        if self.head is None:
            return None
        return self.head.data
    
    def print_list(self):
        current = self.head
        result = ""

        while current:
            result += f"-> {current.data}\n"
            current = current.next

        return result

    def print_list_reverse(self):
        current = self.tail
        result = ""

        while current:
            result += f"-> {current.data}\n"
            current = current.prev
        return result
    
    

if __name__ == "__main__":

    dane = [
        ('AGH', 'Kraków', 1919),
        ('UJ', 'Kraków', 1364),
        ('PW', 'Warszawa', 1915),
        ('UW', 'Warszawa', 1915),
        ('UP', 'Poznań', 1919),
        ('PG', 'Gdańsk', 1945)
    ]

    uczelnie = List()

    
    uczelnie.append(dane[0])
    uczelnie.append(dane[1])
    uczelnie.append(dane[2])

    
    uczelnie.add(dane[3])
    uczelnie.add(dane[4])
    uczelnie.add(dane[5])

    
    print("Lista uczelni:")
    print(uczelnie.print_list())
    print("Lista uczelni od tyłu")
    print(uczelnie.print_list_reverse())

   
    print("Długość listy", uczelnie.length())

    
    print("Usunięty pierwszy element", uczelnie.remove())

    
    print("Pierwszy element po usunięciu", uczelnie.get())

   
    print("Usunięty ostatni element", uczelnie.remove_end())

    
    print("Lista po usunięciu pierwszego i ostatniego elementu")
    print(uczelnie.print_list())
    print("Lista po usunięciu pierwszego i ostatniego elementu od tyłu")
    print(uczelnie.print_list_reverse())

   
    uczelnie.destroy()
    print("Czy lista jest pusta po destroy dla isempty", uczelnie.is_empty())

   
    print("Usuwanie pierwszego elementu z pustej listy", uczelnie.remove())

    
    print("Usuwanie ostatniego elementu z pustej listy", uczelnie.remove_end())

    
    uczelnie.append(('AGH', 'Kraków', 1919))

    
    print("Usunięty ostatni element po dodaniu aghkrakow1919", uczelnie.remove_end())

    
    print("Wypisywanie wyniku isepmty", uczelnie.is_empty())