#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

# ========================================================== 
# Contoh Rekursi 1: Faktorial 
# ========================================================== 

def faktorial(n): 
# Base case: berhenti ketika n = 0 
    if n == 0: 
        return 1 #Jika if terpenuhi maka aakn mengembalikan nilai 1 
# Recursive case: masalah diperkecil menjadi faktorial(n-1) 
    return n * faktorial(n - 1)  #Fungsi memanggil dirinya sendiri dengan nilai lebih kecil


print(faktorial(5))  # Output: 120 

