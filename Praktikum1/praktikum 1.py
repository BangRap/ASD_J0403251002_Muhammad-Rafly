with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("==== Hasil Read ====")
print("Tipe Data :", type(isi_file))


# ================================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 1: Membuka file per baris
# ================================================================

print("====Membuka File Per Baris====")
jumlah_baris= 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print("Baris ke-", jumlah_baris)
        print("isinya :", baris)


# ================================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 2: Memparsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom-kolom data 
# ================================================================

print("====Membuka File Per Baris====")
jumlah_baris= 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip() #Menghilang karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menajdi data satuan dan simpan ke variabel
        print("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai)


# ================================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 3: Membaca Data dan Menyimpannya ke struktur data list
# ================================================================

data_list = [] #inisiasi list untuk menampung data

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #Menghilang karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menajdi data satuan dan simpan ke variabel
        data_list.append([nim,nama,int(nilai)]) #Menyimpan data ke list
    
    print("====Menampilkan List====")
    print(data_list)
    print("Contoh record ke 1", data_list[0])
    print("Contoh record ke 2", data_list[1])
    print("Jumlah Record", len(data_list))

# ================================================================
# Praktikum 1: Konsep ADT dan File Handling
# Latihan Dasar 4: Membaca Data dan Menyimpanna ke struktur data list
# ================================================================

data_dict = {} #Inisialisasi Dictinary

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip() #Menghilang karakter baris baru
        nim, nama, nilai = baris.split(",") #pecah menajdi data satuan dan simpan ke variabel
        #simpan data dalam dictionary (key, value)
        data_dict[nim] = {
            "nama" : nama,
            "nilai" : int(nilai)
        }
    print ("===== Menampilkan Data Dictionary ====")
    print(data_dict)