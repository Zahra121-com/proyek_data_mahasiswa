import unittest
from mahasiswa import fileio, testing
from mahasiswa.processing import Mahasiswa, DaftarMahasiswa

FILE_DATA = "data_mahasiswa.txt"
FILE_LAPORAN = "laporan_mahasiswa.txt"

def tampilkan_menu():
    print("\n" + "=" * 45)
    print("        SISTEM DATA MAHASISWA")
    print("=" * 45)
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Semua Data")
    print("3. Cari Mahasiswa (Nama)")
    print("4. Filter Berdasarkan IPK")
    print("5. Buat Laporan")
    print("6. Jalankan Pengujian")
    print("0. Keluar")
    print("-" * 45)
    return input("Pilih menu (0-6): ")

def menu_tambah(data):
    print("\n--- TAMBAH DATA MAHASISWA ---")
    try:
        mhs = Mahasiswa(nim=input("Nama            : "),
                        nama=input("NPM            : "),
                        jurusan=input("Jurusan         : "),
                        semester=input("Semester (1-8) : "),
                        ipk=input("IPK (0.0-4.0)   : "),
                        email=input("Email (opsional): ") or "-")
        data.tambah(mhs)
    except ValueError as e:
        print("Input ditolak:", e)
        return
    fileio.tambah_file(FILE_DATA, mhs)
    print(f"\n✓ Data {mhs.nama} berhasil disimpan!")

def tampilkan(daftar):
    if not daftar:
        print("Tidak ada data.")
    for m in daftar:
        print(m)

def menu_filter(data):
    try:
        minimal = float(input("IPK minimal: "))
    except ValueError :
        print("Harus angka.")
        return
    tampilkan(data.filter_ipk(minimal=minimal))

def menu_laporan(data):
    teks = data.teks_laporan()
    fileio.tulis_laporan(FILE_LAPORAN, teks)
    print(teks)

def jalankan_tes():
    suite = unittest.defaultTestLoader.loadTestsFromModule(testing)
    unittest.TextTestRunner(verbosity=2).run(suite)

def main():
    fileio.buat_file(FILE_DATA)
    data = DaftarMahasiswa(fileio.baca_file(FILE_DATA))
    while True:
        pilih = tampilkan_menu()
        if pilih == "1":
            menu_tambah(data)
        elif pilih == "2":
            tampilkan(data.daftar)
        elif pilih == "3":
            tampilkan(data.cari_nama(input("Nama dicari: ")))
        elif pilih == "4":
            menu_filter(data)
        elif pilih == "5":
            menu_laporan(data)
        elif pilih == "6":
            jalankan_tes()
        elif pilih == "0":
            break
            
        else:
            print("Pilihan tidak valid, pilih 0-6.")

if __name__ == "__main__":
    main()