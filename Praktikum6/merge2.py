#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

def mergeSort(data):
    '''
    Ini adalah fungsi merge sort dalam mengurutkan secara descending
    '''
    print("Splitting ",data)
    if len(data)>1:
        mid = len(data)//2
        lefthalf = data[:mid]
        righthalf = data[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] >= righthalf[j]: #Diubah tanda <= menjadi >= artinya Supaya descending, ubah menjadi memilih nilai yang lebih besar dulu
                data[k]=lefthalf[i]
                i=i+1
            else:
                data[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            data[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            data[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",data)

data = [54,26,93,17,77,31,44,55,20]
mergeSort(data)
print(data)