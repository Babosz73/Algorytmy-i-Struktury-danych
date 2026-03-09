from unittest import result


class Elem:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
    
    def destroy(self):
        self.head = None
    
    def add(self, data):
        new_elem = Elem(data)
        if self.head is None: 
            self.head = new_elem
        else:
            new_elem.next = self.head
            self.head = new_elem
    
    def append(self,data):
        last_elem = Elem(data)

        if self.head is None:
            self.head = last_elem
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            
            current.next = last_elem

    def remove(self):
        if self.head is None:
            return None
        
        removed = self.head
        self.head = self.head.next
        return removed.data
            

    def remove_end(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            removed = self.head
            self.head = None
            return removed.data
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            removed = current.next
            current.next = None
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

   
    print("Długość listy:", uczelnie.length())

    
    # print("Usunięty pierwszy element:", uczelnie.remove())

    
    # print("Pierwszy element po usunięciu:", uczelnie.get())

   
    # print("Usunięty ostatni element:", uczelnie.remove_end())

    
    # print("Lista po usunięciu pierwszego i ostatniego elementu:")
    # print(uczelnie.print_list())

   
    # uczelnie.destroy()
    # print("Czy lista jest pusta po destroy?:", uczelnie.is_empty())

   
    # print("Usuwanie pierwszego elementu z pustej listy:", uczelnie.remove())

    
    # print("Usuwanie ostatniego elementu z pustej listy:", uczelnie.remove_end())

    
    # uczelnie.append(('AGH', 'Kraków', 1919))

    
    # print("Usunięty ostatni element:", uczelnie.remove_end())

    
    # print("Czy lista jest pusta na końcu?:", uczelnie.is_empty())