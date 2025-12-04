# matematika.py
# Modul ini berisi fungsi-fungsi utilitas untuk operasi matematika sederhana
# dalam konteks pengelolaan stok (penambahan dan pengurangan).

def catat_pergerakan_stok(stok_saat_ini, nama_barang, jumlah, tipe):
    """
    Memperbarui kamus stok berdasarkan pergerakan (masuk atau keluar).

    Args:
        stok_saat_ini (dict): Kamus (nama_barang: jumlah) stok saat ini.
        nama_barang (str): Nama barang yang pergerakannya dicatat.
        jumlah (int): Jumlah unit yang bergerak.
        tipe (str): Tipe pergerakan ('masuk' atau 'keluar').

    Returns:
        dict: Kamus stok yang telah diperbarui.
    """
    nama_barang = nama_barang.title()  # Kapitalisasi awal untuk konsistensi
    
    if tipe == 'masuk':
        # Operasi matematika: Penambahan
        stok_saat_ini[nama_barang] = stok_saat_ini.get(nama_barang, 0) + jumlah
        print(f"\n✅ {jumlah} unit {nama_barang} berhasil ditambahkan ke stok.")
    
    elif tipe == 'keluar':
        # Operasi matematika: Pengurangan (dengan pengecekan batas)
        stok_awal = stok_saat_ini.get(nama_barang, 0)
        
        if stok_awal >= jumlah:
            stok_saat_ini[nama_barang] -= jumlah
            print(f"\n✅ {jumlah} unit {nama_barang} berhasil dikeluarkan dari stok (Penjualan).")
        else:
            print(f"\n❌ Gagal: Stok {nama_barang} hanya tersedia {stok_awal} unit. Tidak bisa mengeluarkan {jumlah} unit.")
            
    else:
        print("\n⚠️ Tipe pergerakan tidak valid. Gunakan 'masuk' atau 'keluar'.")
        
    return stok_saat_ini

def cetak_laporan_stok(stok_saat_ini):
    """
    Mencetak laporan ringkasan stok saat ini dan menghitung total unit.
    
    Args:
        stok_saat_ini (dict): Kamus (nama_barang: jumlah) stok saat ini.
    """
    print("\n" + "="*40)
    print("      * LAPORAN STOK INVENTARIS *")
    print("="*40)
    
    if not stok_saat_ini:
        print("Inventaris kosong.")
        return

    print(f"{'Nama Barang':<20} | {'Jumlah Stok':>15}")
    print("-" * 40)
    
    total_unit = 0
    for barang, jumlah in sorted(stok_saat_ini.items()):
        print(f"{barang:<20} | {jumlah:>15}")
        total_unit += jumlah # Operasi matematika: Penambahan Total
    
    print("-" * 40)
    print(f"{'TOTAL UNIT':<20} | {total_unit:>15}")
    print("="*40)