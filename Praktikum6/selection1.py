#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

def selectionSort(data):
    '''
    Ini adalah fungsi selection sort dalam mengurutkan secara ascending
    '''
    for fillslot in range(len(data)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            if data[location]>data[positionOfMax]:
                positionOfMax = location
# Swap
        temp = data[fillslot]
        data[fillslot] = data[positionOfMax]
        data[positionOfMax] = temp


data = [54,26,93,17,77,31,44,55,20]
selectionSort(data)
print(data)