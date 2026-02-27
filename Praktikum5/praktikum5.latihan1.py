#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

# ========================================================== 
# Latihan 1: Rekursi Pangkat 
# ==========================================================

def pangkat(a, n): 
#Base case 
    if n == 0: 
        return 1
    #Untuk base case ini:
    #Jika pangkat n = 0 maka hasilnya akan selalu 1
    #Sesuai dengan teori matematika, maka bilangan yang pangkatnya 0 maka akan menghasilkan 1
    
    
    #Recursive case 
    return a * pangkat(a, n - 1) 
        #Fungsi ini memanggil dirinya sendiri
        # a^n = a * a^(n-1)
        # Nilai n ini akan dikurangi 1 setiap pemanggilan

print(pangkat(2, 4))  # Output: 16 

#ALUR PROGRAM
#pangkat (2,4)
# = 2 * pangkat(2,3)
# = 2 * (2 * pangkat(2,2))
# = 2 * (2 * (2 * pangkat(2,1)))
# = 2 * (2 * (2 * (2 * pangkat(2,0))))
# = 2 * (2 * (2 * (2 * 1)))

#Lanjut fase undwinding
# 2 * 1 = 2 -> pangkat (2,1)
# 2 * 2 = 4 -> pangkat (2,2)
# 2 * 4 = 8 -> pangkat (2,3)
# 2 * 8 = 16 -> pangkat (2,4)

#Maka dapat dihasilkanlah output 16 ini