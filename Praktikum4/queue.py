#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A1
#==============================================

#==============================================
#Implementasi Dasar : Queue
#==============================================

class Node:
    #Konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Nodde dipanggil / diinstansiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke Note berikutnya (awal=nama)

class queue:
    #buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang
    
    def is_empty(self):
        return self.front is None #stack kosong jika top = None
    
    
    
    #membuat fungsi untuk menambahkan data barru padad bagian belakang
    def enqueue(self,data):
        nodeBaru = Node(data)
        
        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        
        self.rear.next = nodeBaru #Letakkan data baru pada setelahnya rear
        self.rear = nodeBaru #Jadikan data baru sebagai rear
    
    def dequeue(self):
        #menghapus data dari depan / front
        data_terhapus = self.front.data #Lihat data paling depan
        
        #geserr front ke node berikutnya
        self.front = self.front.next

        #jika setelah geser front menjadi none, maka queue kosong
        #rear juga harus jadi None
        if self.front is None:
            self.rear = None

    def tampilkan(self):
        current = self.front
        print("front ->", end='')
        while current is not None:
            print(current.data, end= "-> ")
            current = current.next
        print(" Rear")

#Inisialisasi class queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()

