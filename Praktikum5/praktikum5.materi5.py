#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

# ========================================================== 
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning) 
# ========================================================== 
 
def biner_batas(n, batas, hasil="", jumlah_1=0): 
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti 
    if jumlah_1 > batas: #Jika jumlah 1 sudah melebihi batas,
        return 
 
    # Base case 
    if len(hasil) == n:  #Jika panjang hasil sudah n 
        print(hasil) 
        return 
 
    # Pilih '0' 
    biner_batas(n, batas, hasil + "0", jumlah_1) #Pilih '0' maka jumlah_1 tetap dengan menambah digit 0 ke hasil

    # Pilih '1' 
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1) #Pilih '1' maka jumlah_1 bertambah 1 dengan menambah digit 1 dan menghitung jumlah 1

biner_batas(4, 2) 