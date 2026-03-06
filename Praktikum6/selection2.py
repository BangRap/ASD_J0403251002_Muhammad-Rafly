#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

def selectionSort_descending(data):
    '''
    Ini adalah fungsi selection sort dalam mengurutkan secara descending
    '''
    for fillslot in range(len(data)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if data[location]<data[positionOfMax]: #Disini diubah tanda > menjadi < terhadap data[positionofmax] untuk membalikkan nilai yang membuat mengurutkan data dari terbesar ke terkecil
                positionOfMax = location
# Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp


data = [54,26,93,17,77,31,44,55,20]
selectionSort_descending(data)
print(data)