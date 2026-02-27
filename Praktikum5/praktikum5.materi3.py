#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

# ========================================================== 
# Contoh Rekursi 3: Menjumlahkan Elemen List 
# ========================================================== 

def jumlah_list(data, index=0): # Kita definisikan fungsi jumlah_list()
    # Base case: jika index sudah mencapai panjang list 
    if index == len(data): # Jika index sama dengan panjang data
        return 0 # Kembalikan 0
    # Recursive case: elemen sekarang + jumlah elemen setelahnya 
    return data[index] + jumlah_list(data, index + 1) # Akan mengembalikan data yang ada di index 0, kemudian yang di index 1, hingga index = 4
print(jumlah_list([2, 4, 6, 8])) # Ngeprint fungsi jumlah_list dan output 20