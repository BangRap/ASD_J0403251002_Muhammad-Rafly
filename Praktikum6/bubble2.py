#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================


def shortBubbleSort_descending(alist):
    '''
    Ini adalah fungsi bubble sort dalam mengurutkan secara descending
    '''
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i]<alist[i+1]: #Disini diubah tanda > menjadi < untuk membalikkan nilai yang membuat mengurutkan data dari terbesar ke terkecil
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
        passnum = passnum-1

alist=[20,30,40,90,50,60,70,80,100,110]
shortBubbleSort_descending(alist)
print(alist)