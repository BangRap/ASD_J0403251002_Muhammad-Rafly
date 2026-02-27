#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

# ========================================================== 
# Latihan 2: Tracing Rekursi 
# ==========================================================

def countdown(n): 
 
    if n == 0: #Jika n ini memiliki nilai 0 maka program akan langsung selesai
        print("Selesai") 
        return 
 
    print("Masuk:", n) #ini akan dieksekusi ketika nilai n bukan sama dengan 0 
 
    countdown(n - 1) #Fungsi akan memanggil lagi sendiri dan mengurangi nilai n sebesar 1 dan akan berulang sampai fungsi if terpenuhi yaitu n == 0
 
    print("Keluar:", n) #Fungsi ini memasuki fase unwinding, akan dieksekusi setelah rekursif selesai

countdown(3) #-> memanggil fungsi countdown dengan nilai n == 3

#Output
#Masuk: 3
#Masuk: 2
#Masuk: 1
#Selesai
#Keluar: 1
#Keluar: 2
#Keluar: 3


#ALUR PROGRAM
# Pemanggilan turun (menuju base case):
# Masuk: 3 -> akan mencetak ini dan harus menjalankan countdown (2) jadi disimpan dulu 3 n nya
# Masuk: 2 -> akan mencetak ini dan harus menjalankan countdown (1) jadi disimpan dulu 2 n nya
# Masuk: 1 -> akan mencetak ini dan harus menjalankan countdown (0) jadi disimpan dulu 1 n nya
# Selesai

# Pengembalian naik (keluar dari rekursi):
# Keluar: 1 -> Kembali ke countdown 1
# Keluar: 2 -> kembali ke countdown 2
# Keluar: 3 -> kembali ke countdown 3