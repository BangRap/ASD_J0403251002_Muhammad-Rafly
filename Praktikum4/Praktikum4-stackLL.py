#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A1
#==============================================

#==============================================
#Implementasi Dasar : Stack
#==============================================

class Node:
    #konstruktor adalah fungsi yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=name)



#Stack ada operasi push(memasukkan head baru) dari pop (menghapus head)

class stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atasa (awalnya kosong)

    
    
    def push(self,data): #memasukkan data baru pada stack
        #1 Membuat noded baru
        nodeBaru = Node(data) #instantiasi / memanggil konstruktor pada class Node

        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top

        #3 geser top pindah ke node baru
        self.top = nodeBaru

        # B -> A -> None
    
    def is_empty(self):
        return self.top is None #stack kosong jika top = None
    
    def pop(self): #Mengambil / menghapus node paling atas (top/head)
        
        if self.is_empty():
            print("Stack Kosong, tidak bisa pop")
            return None
        
        data_terhapus = self.top.data #soroti bagian top dengan simpan di variabe top
        self.top = self.top.next
        return data_terhapus

    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data
    

    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print("Top " , end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

#Instantiasi Class Stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print("Peek (Lihat Top): " , s.peek())
s.pop()
s.tampilkan()
print("Peek (Lihat Top): " , s.peek())
