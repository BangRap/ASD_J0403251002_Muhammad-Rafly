class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Pointer tail

    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:  # Jika list kosong
            self.head = new_node
            self.tail = new_node
            self.tail.next = self.head  # Circular ke dirinya sendiri
        else:
            self.tail.next = new_node   # Sambungkan tail ke node baru
            self.tail = new_node        # Update tail
            self.tail.next = self.head  # Circular kembali ke head

    def display(self):
        if not self.head:
            print("List is empty")
            return

        print("Circular Linked List Traversal:")
        temp = self.head

        print(temp.data, end=" -> ")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("... (back to head)")
    
    def search(self, key): 
        temp = self.head
        if self.head is None:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari")
        while temp: 
                if temp.data == key: 
                    print(f"Elemen {key}, ditemukan dalam Circular Linked List.")
                    return True 
                temp = temp.next
                if temp.data != key:
                    print(f"Elemen {key}, tidak ditemukan dalam Circular Linked List.")
                    return True
                
        return False

print("===========================================================")
# Contoh Tampilan 1
cll = CircularSinglyLinkedList()
cll.insert_at_end(3)
cll.insert_at_end(7)
cll.insert_at_end(12)
cll.insert_at_end(19)
cll.insert_at_end(25)
cll.display()
cll.search(12)

print("===========================================================")
# Contoh Tampilan 2
cll = CircularSinglyLinkedList()
cll.insert_at_end(5)
cll.insert_at_end(10)
cll.insert_at_end(15)
cll.insert_at_end(20)
cll.insert_at_end(30)
cll.display()
cll.search(25)

print("===========================================================")
# Contoh Tampilan 3
cll = CircularSinglyLinkedList()
cll.display()
cll.search(10)

print("===========================================================")
print("===TAMPILAN JIKA INGIN MENGINPUT MANUAL===")
#Tampilan untuk inputan
cll = CircularSinglyLinkedList()

data_input = input("Masukkan elemen (pisahkan dengan koma): ")
elements = data_input.split(",")

for item in elements:
    if item.strip() != "":
        cll.insert_at_end(int(item.strip()))

key = int(input("Masukkan elemen yang ingin dicari: "))
cll.search(key)

