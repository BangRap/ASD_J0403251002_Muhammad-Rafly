#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

# ========================================================== 
# Studi Kasus: Generator PIN 
# ========================================================== 
 
def buat_pin(panjang, hasil=""): 
 
    if len(hasil) == panjang: #Ini akan dieksekusi kalau panjang hasil sama nilainya dengan "panjang"
        print("PIN:", hasil) 
        return 
 
    for angka in ["0", "1", "2"]: # Loop pilihan digit yang boleh dipakai
        buat_pin(panjang, hasil + angka) 
        # Memanggil fungsi lagi dengan menambahkan digit (0/1/2) ke string hasil saat ini
 
buat_pin(3) 

#ALUR PROGRAM
#Secara intinya
# base case -> panjang string sudah = panjang pin
# rekursi -> menambahkan digit 0,1,2
# banyak kombinasinya 3 pangkat panjang maka 3 pangkat 3 = 27 PIN

