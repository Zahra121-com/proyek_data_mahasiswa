from .processing import Mahasiswa

HEADER = "nim|nama|jurusan|semester|ipk|email\n"

def buat_file(path):
    try:
        with open(path, "x", encoding="utf-8") as f:
            f.write(HEADER)
        print("File data dibuat.")
    except FileExistsError:
        pass 

def tambah_file(path, mhs):
    with open(path, "a", encoding="utf-8") as f:
        f.write(mhs.ke_baris())

def baca_file(path):
    daftar = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for nomor, baris in enumerate(f, start=1):
                if nomor == 1 or not baris.strip():
                    continue  
                try:
                    p = baris.strip().split("|")
                    if len(p) != 6:
                        raise ValueError("jumlah kolom salah")
                    daftar.append(Mahasiswa(p[0], p[1], p[2], p[3], p[4], email=p[5]))
                except ValueError:
                    print(f"Baris {nomor} rusak, dilewati: {baris.strip()}")
    except FileNotFoundError:
        print(f"File {path} belum ada. Tambah data dulu.")
    return daftar

def tulis_laporan(path, teks):
    with open(path, "w", encoding="utf-8") as f:
        f.write(teks)
