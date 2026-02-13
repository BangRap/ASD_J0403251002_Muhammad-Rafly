

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

    def	delete_node(self,	key):
        """
        Berfungsi untuk menghapus node
        """
        temp = self.head

        if	temp	and	temp.data	==	key:	
            self.head	=	temp.next	
            temp	=	None	
            return
    
    
        prev = None
        while temp and temp.data !=	key:	
            prev = temp	
            temp = temp.next	
    
    
        if temp is	None:	
            return	

        prev.next = temp.next	
        temp	=	None

#Memulai Program
ll = LinkedList()
ll.insert_at_end(4)
ll.insert_at_end(20)
ll.insert_at_end(25)
ll.insert_at_end(35)
ll.insert_at_end(45)
ll.display()
ll.delete_node(20)
ll.display()

