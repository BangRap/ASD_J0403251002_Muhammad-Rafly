# ========================================================== 
# TUGAS HANDS-ON MODUL 1 
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt) 
# 
# Nama  : Muhammad Rafly
# NIM   : J0403251002
# Kelas : A1
# ========================================================== 
# ------------------------------- 
# stok_barang.txt 
# ------------------------------- 
NAMA_FILE = "stok_barang.txt" 

# ------------------------------- 
# Fungsi: Membaca data dari file 
# ------------------------------- 

def baca_stok(nama_file): 
    """ 
    Membaca data stok dari file teks. 
    Format per baris: KodeBarang,NamaBarang,Stok 
    Output: - stok_dict (dictionary) 
    key   = kode_barang 
    value = {"nama": nama_barang, "stok": stok_int} 
    """ 
    stok_dict = {} #Inisiasi data dictionary dalam file

    with open(nama_file, "r", encoding="utf-8") as file: 
        for isi in file:
            isi = isi.strip() #Mengambil data per baris
            kodebarang, namabarang, stok = isi.split(",") #ambil data per item data
            stok_dict[kodebarang] = {"kodebarang" : kodebarang, "namabarang" : namabarang, "stok" : int(stok)} #Memasukkan Data
    return stok_dict

    
    

# ------------------------------- 
# Fungsi: Menyimpan data ke file 
# ------------------------------- 

def simpan_stok(nama_file, stok_dict): 
    """ 
    Menyimpan seluruh data stok ke file teks. 
    Format per baris: KodeBarang,NamaBarang,Stok 
    """
    with open(nama_file,"w", encoding="utf-8") as file:
        for Kodebarang in sorted(stok_dict.keys()): #Loop kode barang satu per satu
            namabarang = stok_dict[Kodebarang]["namabarang"] #Ambil "Nama Barang" dari dalam dictionary
            stok = stok_dict[Kodebarang]["stok"] #Ambil angka Stok dari dalam dictionary
            file.write(f'{Kodebarang},{namabarang},{stok}\n') #Menyimpan data kedalam dictionary
    
    input("\nTekan Enter untuk kembali ke menu...")


# ------------------------------- 
# Fungsi: Menampilkan semua data 
# -------------------------------

def tampilkan_semua(stok_dict):
    """
    Menampilkan semua barang di stok_dict.
    """

    print("\n======== DAFTAR BARANG ========")
    print(f"{"Kode Barang" : <11} | {"Nama Barang" : <15} | {"Stok" : >5}") #Membuat batas per variabel
    print("-" *35) #Membuat Garis
   
    for Kodebarang in sorted(stok_dict.keys()): #Loop semua kode barang
        namabarang = stok_dict[Kodebarang]["namabarang"] #Ambil data Nama Barang
        stok = stok_dict[Kodebarang]["stok"] #Ambil data Stok
        print(f"{Kodebarang: <11} | {namabarang:<15} | {int(stok):>5}") #Buat Tabel
    
    input("\nTekan Enter untuk kembali ke menu...")
    
   

# ------------------------------- 
# Fungsi: Cari barang berdasarkan kode 
# ------------------------------- 

def cari_barang(stok_dict): 
    """ 
    Mencari barang berdasarkan kode barang. 
    """ 
    kode = input("Masukkan kode barang: ").strip().upper()


    if kode in stok_dict: #Buat mengecek kode barang di dalam dictionary
        namabarang = stok_dict[kode]["namabarang"]
        stok = stok_dict[kode]["stok"]

        print("===== Data Mahasiswa Ditemukan =====")
        print(f"Kode Barang     : {kode}")
        print(f"Nama Barang     : {namabarang}")
        print(f"Stok            : {stok}")
        
        input("\nTekan Enter untuk kembali ke menu...")
    
    else: #Kalau kode gak ada akan mengeksekusi baris ini
        print("Data tidak ditemukan. Pastikan Kode Barang yang dimasukkan sudah benar")
        input("\nTekan Enter untuk kembali ke menu...")



# ------------------------------- 
# Fungsi: Tambah barang baru 
# ------------------------------- 

def tambah_barang(stok_dict):

    """ 
    Menambah barang baru ke stok_dict. 
    """ 

    kode = input("Masukkan kode barang baru: ").strip().upper()
    
    if kode in stok_dict: #Buat mengecek kode agar tidak duplikat
        print(f"\n,GAGAL, Kode '{kode}' sudah digunakan.")
        print("Silakan gunakan kode lain atau update stok barang tersebut.")
        return 
    nama = input("Masukkan nama barang: ").strip()

    if nama in stok_dict: #Buat mengecek nama agar tidak duplikat
        print(f"\nGAGAL, Barang '{nama}' sudah ada dalam stok.")
        print("Silakan gunakan barang lain atau update stok barang tersebut.")
        return

    jumlah_barang = int(input("Masukkan jumlah barang baru"))

    
    
    stok_dict[kode] = {
        "kodebarang" : kode,
        "namabarang" : nama,
        "stok" : jumlah_barang
    }
    print(f"\nBERHASIL, Barang '{nama}' (Kode: {kode}) dengan stok {jumlah_barang} telah ditambahkan.")



# ------------------------------- 
# Fungsi: Update stok barang 
# ------------------------------- 

def update_stok(stok_dict): 
    """ 
    Mengubah stok barang (tambah atau kurangi). 
    Stok tidak boleh menjadi negatif. 
    """ 
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()
    
    if kode not in stok_dict:
        print("Kode Barang tidak ditemukan. Update dibatalkan")
        return
    
    
 
    print("Pilih jenis update:") 
    print("1. Tambah stok") 
    print("2. Kurangi stok") 
 
    pilihan = input("Masukkan pilihan (1/2): ").strip()
    
    if pilihan == "1":
        try:
            tambahan_stok = int(input("Masukkan jumlah stok barang yang ingin ditambah"))

            stok_lama = stok_dict[kode]["stok"]
            stok_baru = stok_lama + tambahan_stok
            stok_dict[kode]["stok"] = stok_baru
            print(f"Update Berhasil. Stok Barang {kode} berubah dari {stok_lama} menjadi {stok_baru}")
            if tambahan_stok <= 0:
                print("Maaf harus menulis angka lebih dari 0")
                return
        except ValueError:
            print("Stok harus berupa angka. Update Dibatalkan")
    
    elif pilihan == "2":
        try:
            pengurang_stok = int(input("Masukkan jumlah stok barang yang ingin ditambah: "))

            stok_lama = stok_dict[kode]["stok"]
            stok_baru = stok_lama - pengurang_stok
            stok_dict[kode]["stok"] = stok_baru
            print(f"Update Berhasil. Stok Barang {kode} berubah dari {stok_lama} menjadi {stok_baru}")
            if pengurang_stok <= 0 or stok_lama < pengurang_stok:
                print("Maaf harus menulis angka lebih dari 0")
                return
        except ValueError:
            print("Stok harus berupa angka. Update Dibatalkan")
    

 
 
 
# ------------------------------- 
# Program Utama 
# ------------------------------- 

def main(): 

    # Membaca data dari file saat program mulai 
    stok_barang = baca_stok(NAMA_FILE) 
 
    while True: 
        print("\n=== MENU STOK KANTIN ===") 
        print("1. Tampilkan semua barang") 
        print("2. Cari barang berdasarkan kode") 
        print("3. Tambah barang baru") 
        print("4. Update stok barang") 
        print("5. Simpan ke file") 
        print("0. Keluar") 
 
        pilihan = input("Pilih menu: ").strip() 
 
        if pilihan == "1": 
            tampilkan_semua(stok_barang) 
 
        elif pilihan == "2": 
            cari_barang(stok_barang) 
 
        elif pilihan == "3": 
            tambah_barang(stok_barang) 
 
        elif pilihan == "4": 
            update_stok(stok_barang) 
 
        elif pilihan == "5": 
            simpan_stok(NAMA_FILE, stok_barang) 
            print("Data berhasil disimpan.") 
        elif pilihan == "0": 
            print("Program selesai.") 
            break 
        else: 
            print("Pilihan tidak valid. Silakan coba lagi.") 

# Menjalankan program utama 
if __name__ == "__main__": 
    main()
