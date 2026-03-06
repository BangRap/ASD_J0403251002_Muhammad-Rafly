#==============================================
#Nama   : Muhammad Rafly
#NIM    : J0403251002
#Kelas  : A
#==============================================

def bubblesort_skorakademik(data):
    '''
    Ini adalah fungsi bubble sort untuk mengurutkan skor akademik secara descending
    '''
    exchanges = True
    list_skor = len(data)-1
    while list_skor > 0 and exchanges:
        exchanges = False
        for i in range(list_skor):
            if data[i]<data[i+1]:
                exchanges = True
                temp = data[i]
                data[i] = data[i+1]
                data[i+1] = temp
        list_skor = list_skor-1

data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]


#====================PERTANYAAN=====================

#1. Jika Pak Budi akan meloloskan lima kandidat dengan nilai tertinggi, tuliskanlah skor lima kandidat tersebut dari yang paling tinggi hingga terendah.
bubblesort_skorakademik(data)
print(data) #Output [98, 89, 76, 68, 57, 43, 33, 22, 12, 9]

#Jadi, skor lima kandidat tersebut dari yang tertinggi adalah 98,89,76,68,57

#2. Kandidat berapa saja yang lolos?

#Untuk kandidat yang lolos adalah berjumlah 5 orang
#1.kandidat urutan ke-7 dari list dengan nilai 98
#2.kandidat urutan ke-4 dari list dengan nilai 89
#3.kandidat urutan ke-2 dari list dengan nilai 76
#4.kandidat urutan ke-9 dari list dengan nilai 68
#5.kandidat urutan ke-6 dari list dengan nilai 57
