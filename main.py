# Import fungsi dari modul terpisah
from inventaris import catat_pergerakan_stok, cetak_laporan_stok

# Variabel Global untuk menyimpan data inventaris
inventaris_stok = {
    "Kopi Instan": 50,
    "Air Mineral": 100,
    "Sabun Mandi": 30
}

def tampilkan_menu():
    """
    Menampilkan opsi menu untuk pengguna.
    """
    print("\n" + "*"*40)
    print("  SISTEM PENGELOLA INVENTARIS TOKO MAJU")
    print("*"*40)
    print("1. Catat Barang Masuk (Pembelian)")
    print("2. Catat Barang Keluar (Penjualan)")
    print("3. Tampilkan Laporan Stok")
    print("4. Keluar Program")
    print("-" * 40)
    
    pilihan = input("Masukkan pilihan Anda (1-4): ")
    return pilihan

def proses_pencatatan(tipe_pergerakan):
    """
    Fungsi untuk menerima input barang dan jumlah, kemudian memanggil fungsi utilitas.
    (Fungsi ke-3 di file main.py)
    """
    print(f"\n--- Pencatatan Barang {'MASUK' if tipe_pergerakan == 'masuk' else 'KELUAR'} ---")
    nama = input("Masukkan nama barang: ")
    try:
        jumlah = int(input("Masukkan jumlah unit: "))
        if jumlah <= 0:
            print("❌ Jumlah harus bilangan bulat positif.")
            return
        
        global inventaris_stok # Mengakses variabel global
        # Memanggil fungsi dari modul terpisah
        inventaris_stok = catat_pergerakan_stok(inventaris_stok, nama, jumlah, tipe_pergerakan)
        
    except ValueError:
        print("❌ Input jumlah tidak valid. Masukkan angka.")
    

def jalankan_program():
    """
    Fungsi utama untuk menjalankan loop program.
    (Fungsi ke-4 di program ini, dan ke-2 di file main.py)
    """
    while True:
        pilihan = tampilkan_menu()
        
        if pilihan == '1':
            proses_pencatatan('masuk') # Barang Masuk
        
        elif pilihan == '2':
            proses_pencatatan('keluar') # Barang Keluar
            
        elif pilihan == '3':
            # Memanggil fungsi dari modul terpisah
            cetak_laporan_stok(inventaris_stok)
            
        elif pilihan == '4':
            print("\nTerima kasih. Sistem Inventaris dimatikan. Sampai jumpa!")
            break
            
        else:
            print("\n❌ Pilihan tidak valid. Silakan coba lagi.")


# Memulai program
if __name__ == "_main_":
    jalankan_program()