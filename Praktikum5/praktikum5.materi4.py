#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

# ========================================================== 
# Contoh Backtracking 1: Kombinasi Biner (n) 
# ========================================================== 

def biner(n, hasil=""): 
    # Base case: jika panjang string sudah n, cetak hasil 
    if len(hasil) == n: # Jika panjang hasil sudah sama dengan n
        print(hasil) #Mencetak kombinasi biner
        return
# Choose + Explore: tambah '0' 
    biner(n, hasil + "0") 
    # Dilakukan rekursif dengan menambahkan digit 1 dan membuat cabang kemungkinan lain
 
    # Choose + Explore: tambah '1' 
    biner(n, hasil + "1")
     # Dilakukan rekursif dengan menambahkan digit 1 dan membuat cabang kemungkinan lain   
 
biner(3) 