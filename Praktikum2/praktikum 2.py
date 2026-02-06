# ================================================================
# Praktikum 2: Membuat Fungsi Load Data dari File
# Latihan Dasar 1:Membuat Fungsi Load Data dari file
# ================================================================

#variabel menyimpan data file

nama_file = "data_mahasiswa.txt"

def baca_data(nama_file):
    data_dict = {} #inisialisasi data dictionary
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() #ambil data per baris dan hilangkan new line
            nim, nama, nilai = baris.split(",") #ambil data per item data
            data_dict[nim] ={"nama": nama, "nilai": int(nilai)} #masukkan dalam
    return data_dict

buka_data = baca_data(nama_file)
print("jumlah data terbaca", len(buka_data))

# ================================================================
# Praktikum 2: Konsep ADTdan File Handling (STUDI KASUS)
# Latihan Dasar 2: Membuat Fungsi Menampilkan Data 
# ================================================================

def tampilkan_data(data_dict):
    #Membuat header tabel
    print("\n======== DAFTAR MAHASISWA ========")
    print(f"{"NIM" : <10} | {"Nama" : <12} | {"Nilai" : >5}")
    print("-" *35) #Membuat Garis
    '''
    untuk tampilan yang rapi, atur lebar kolomnya
    {nim<10} artinya nim rata kiri dengan lebar 10
    {nama:<12} artinya nama rata kiri dengan lebar 12
    {int(nilai):>5} artinya nilai rata kanan dengan lebar 5
    '''
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]
        print(f"{nim: <10} | {nama:<12} | {int(nilai):>5}")

tampilkan_data(buka_data) #Memanggil fungsi untuk menampilkan data

# ================================================================
# Praktikum 2: Konsep ADTdan File Handling (STUDI KASUS)
# Latihan Dasar 3: Membuat Fungsi Menampilkan Data 
# ================================================================

#membuat fungsi pencarian data
def cari_data(data_dict):
    #pencarian data berdasarkan nim sebagai key dictionary
    #membuat input nim mahsiswa yang akan dicari
    nim_cari = input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()

    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("===== Data Mahasiswa Ditemukan =====")
        print(f"NIM       : {nim_cari}")
        print(f"Nama      : {nama}")
        print(f"Nilai     : {nilai}")
    else:
        print("Data tiak ditemukan. Pastikan NIM yang dimasukkan benar")

#memanggil fungsi cari ddata
cari_data(buka_data)

# ================================================================
# Praktikum 2: Konsep ADTdan File Handling (STUDI KASUS)
# Latihan Dasar 4: Membuat Fungsi Menampilkan Data 
# ================================================================

#membuat fungsi update data

def ubah_data(data_dict):

    #awali dulu dengan mencari nim / data mahasiswa yang ingin di update
    nim = input("Masukkan NIM mahasiswa yang ingin diubah datanya : ").strip()

    if nim not in data_dict:
        print("NIM tidak ditemukan. Update ddibatalkan")
        return
    
    try:
        nilai_baru = int(input("Masukkan nilai baru 0-100 : "))
    
    except ValueError:
        print("Nilai harus berupa angka. Update Dibatalkan")
    
    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update Dibatalkan")
    

    nilai_lama = data_dict[nim]["nilai"]
    data_dict[nim]["nilai"] = nilai_baru

    print(f"Update Berhasil. Nilai {nim} berubah dari {nilai_lama} menjadi {nilai_baru}")

#memanggil fungsi ubah data
ubah_data(buka_data)

# ================================================================
# Praktikum 2: Konsep ADTdan File Handling (STUDI KASUS)
# Latihan Dasar 5: Membuat Fungsi Menampilkan Data 
# ================================================================

#Membuat fungsi menyimpan data ke file

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]
            file.write(f"{nim}, {nama}, {nilai}\n")

#memanggil fungsi simpan data
simpan_data(nama_file, buka_data)
print("\nData Berhasil Disimpan ke file: ", nama_file)

# ================================================================
# Praktikum 2: Konsep ADTdan File Handling (STUDI KASUS)
# Latihan Dasar 6: Membuat Menu Interaktif 
# ================================================================

def main():
    #load data otomatis saat program dimulai
    buka_data = baca_data(nama_file) #fs.1 

    while True:
        print("\n=====MENU DATA MAHASISWA===")
        print("1.Tampilkan Data Mahasiswa")
        print("2. Cari Data Berdasarkan NIM")
        print("3. Ubah Nilai Mahasiswa")
        print("4. simpan Data ke File")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data) #Memanggil fs.2 menampilkan data mahasiswa
        
        elif pilihan == "2":
            cari_data(buka_data) #Memanggil fs.3 mencari data mahasiswa
        
        elif pilihan == "3":
            ubah_data(buka_data) #Memanggil fs.4 Mengubah data mahasiswa
        elif pilihan == "4":
            simpan_data(nama_file, buka_data) #Memanggil fs.5 menyimpan data mahasiswa ke file
            print("Data Berhasil Disimpan")
        elif pilihan == "0":
            print("Program Selesai.")
            break

        else:
            print("Pilihan Tidak Valid, Silahkan Coba Lagi")