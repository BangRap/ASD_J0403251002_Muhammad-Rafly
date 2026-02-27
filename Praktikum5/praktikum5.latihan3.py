#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

# ========================================================== 
# Latihan 3: Mencari Nilai Maksimum 
# ========================================================== 
 
def cari_maks(data, index=0): 
 
    # Base case 
    if index == len(data) - 1: #Ini akan dieksekusi ketika panjang datanya bernilai 1 dan akan mengembalikan nilai elemen
        return data[index] 
 
    # Recursive case 
    maks_sisa = cari_maks(data, index + 1) #Cari nilai maksimum dari sisa data (mulai index + 1)
 
    if data[index] > maks_sisa: # Disini proses perbandingan. Bandingkan elemen sekarang dengan maksimum sisa
        return data[index] #Jika lebih besar, kembalikan elemen sekarang
    else: 
        return maks_sisa # Jika tidak, kembalikan maksimum sisa
 
 
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka)) #output: Nilai maksimum: 9

#ALUR PROGRAM
#1.cari_maks(index=0) → nilai = 3, harus mencari maksimum dari [7,2,9,5] dulu dan simpan angka 3
#2.cari_maks(index=1) → nilai = 7, harus mencari maksimum dari [2,9,5] dulu dan simpan angka 7
#3.cari_maks(index=2) → nilai = 2, harus mencari maksimum dari [9,5] dulu dan simpan angka 2
#4 cari_maks(index=3) → nilai = 9, harus mencari maksimum dari [5] dulu dan simpan angka 9
#5.cari_maks(index=4) → nilai = 5, base case ini sudah selesai jadi langsung kembalikan 5

#Lanjut fase unwinding
#Kembali ke index=3 (nilai 9), Bandingkan 9 dengan 5 maka maksimum = 9
#Kembali ke index=2 (nilai 2), Bandingkan 2 dengan 9 maka maksimum = 9
#Kembali ke index=1 (nilai 7), Bandingkan 7 dengan 9 maka maksimum = 9
#Kembali ke index=0 (nilai 3), Bandingkan 3 dengan 9 maka Maksimum = 9