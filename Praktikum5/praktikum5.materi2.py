#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

# ========================================================== 
# Contoh Rekursi 2: Tracing Masuk/Keluar 
# ========================================================== 
def hitung(n): 
# Base case 
    if n == 0: 
        print("Selesai") #Jika n == 0 maka print selesai
        return #Memberhentikan rekursif
    print("Masuk:", n) # Dicetak saat fungsi pertama kali dipanggil      
    hitung(n - 1) # Pemanggilan rekursif dengan n dikurangi 1
    print("Keluar:", n) #Dicetak setelah fungsi rekursif selesai

hitung(3) 
