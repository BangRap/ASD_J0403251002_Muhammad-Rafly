class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        """
        Untuk menginisasi
        """
        self.head = None
        self.tail = None  # Pointer tail

    def insert_at_end(self, data):
        """
        Untuk menyimpan list
        """
        new_node = Node(data)

        if not self.head:  # Jika linked list kosong
            self.head = new_node
            self.tail = new_node  # Tail menunjuk ke node pertama
        else:
            self.tail.next = new_node  # Sambungkan tail ke node baru
            self.tail = new_node       # Update tail ke node baru

    def display(self):
        """
        Ini untuk memoformat list lalu mengeprintnya
        """
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    
    def combine(self, other):
        temp = self.head
        
        while temp:
            if temp.next is None:
                temp.next = other.head
                break
            temp = temp.next

#Membuat List ke-1
ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(13)
ll.insert_at_end(2)
ll.display()

#Membuat List ke-2
lllist2 = LinkedList()
lllist2.insert_at_end(7)
lllist2.insert_at_end(9)
lllist2.insert_at_end(11)
lllist2.display()

#Menyatukan 2 list
ll.combine(lllist2)
ll.display()
