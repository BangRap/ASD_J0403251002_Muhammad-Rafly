#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

# ========================================================== 
# Latihan 4: Kombinasi Huruf 
# ========================================================== 
 
def kombinasi(n, hasil=""): 
 
    if len(hasil) == n: #ini akan dieksekusi kalau panjang string hasil ini memiliki nilai yang sama dengan n
        print(hasil) #Mencetak kombinasi
        return 
 
    kombinasi(n, hasil + "A") #Disini menambahkan huruf A ke hasil lalu lanjut rekursif
    kombinasi(n, hasil + "B") #Dissini menambahkan huruf B ke hasil lalu lanjut rekursif
 
 
kombinasi(2) 

#Output
#AA
#AB
#BA
#BB

#ALUR PROGRAM
# hasil="" -> panjang masih < 2, tambah "A"
# hasil="A" -> panjang masih < 2, tambah "A" lagi
# hasil="AA" -> panjang sudah = 2 → print "AA"

# Kembali ke "A", coba "B"
# hasil="AB" -> panjang sudah = 2 → print "AB"

#Lalu dilanjutkan dengan cabang B sama seperti A 


#Fase Unwinding
# Setelah "AA" dicetak -> balik ke hasil="A"
# Setelah "AB" dicetak -> balik ke hasil=""
# Setelah "BA" dicetak -> balik ke hasil="B"
# Setelah "BB" dicetak -> balik ke hasil=""
