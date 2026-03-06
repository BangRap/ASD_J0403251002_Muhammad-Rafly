#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

def insertionSort(data):
    '''
    Ini adalah fungsi insertion sort dalam mengurutkan secara descending
    '''
    for index in range(1,len(data)):
        currentvalue = data[index]
        position = index
        while position>0 and data[position-1]<currentvalue: #Disini diubah tanda > menjadi < terhadap current value untuk membalikkan nilai yang membuat mengurutkan data dari terbesar ke terkecil
            data[position]=data[position-1]
            position = position-1
            data[position]=currentvalue

data = [54,26,93,17,77,31,44,55,20]
insertionSort(data)
print(data)