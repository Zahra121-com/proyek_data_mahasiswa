from .validasi import cek_kosong, cek_semester, cek_ipk

class Mahasiswa:
    def __init__(self, nim, nama, jurusan, semester, ipk, **kwargs):
        self.nim = cek_kosong(nim, "NIM")
        self.nama = cek_kosong(nama, "Nama")
        self.jurusan = cek_kosong(jurusan, "Jurusan")
        self.semester = cek_semester(semester)
        self.ipk = cek_ipk(ipk)
        self.email = kwargs.get("email", "-")

    def ke_baris(self):
        return (f"{self.nim}|{self.nama}|{self.jurusan}|"
                f"{self.semester}|{self.ipk}|{self.email}\n")

    def __str__(self):
        return (f"{self.nim:<10} {self.nama:<18} {self.jurusan:<16} "
                f"Smt {self.semester:<2} IPK {self.ipk:.2f}")

def hitung_rata(*angka):
    return sum(angka) / len(angka) if angka else 0

class DaftarMahasiswa:
    def __init__(self, daftar):
        assert isinstance(daftar, list), "daftar harus list"
        self.daftar = daftar

    def tambah(self, mhs):
        if any(m.nim == mhs.nim for m in self.daftar):
            raise ValueError(f"NIM {mhs.nim} sudah terdaftar")
        self.daftar.append(mhs)

    def cari_nama(self, kata):
        return list(filter(lambda m: kata.lower() in m.nama.lower(), self.daftar))

    def filter_ipk(self, minimal=0.0, maksimal=4.0):
        return list(filter(lambda m: minimal <= m.ipk <= maksimal, self.daftar))

    def terbaik(self, n=3):
        return sorted(self.daftar, key=lambda m: m.ipk, reverse=True)[:n]

    def rata_ipk(self):
        return hitung_rata(*[m.ipk for m in self.daftar])

    def per_jurusan(self):
        hasil = {}
        for m in self.daftar:
            hasil[m.jurusan] = hasil.get(m.jurusan, 0) + 1
        return hasil

    def teks_laporan(self):
        if not self.daftar:
            return "LAPORAN MAHASISWA\nBelum ada data.\n"
        baris = ["LAPORAN DATA MAHASISWA",
                 f"Jumlah mahasiswa : {len(self.daftar)}",
                 f"Rata-rata IPK    : {self.rata_ipk():.2f}",
                 "Jumlah per jurusan:"]
        for jurusan, jumlah in self.per_jurusan().items():
            baris.append(f"  {jurusan}: {jumlah}")
        baris.append("3 IPK tertinggi:")
        for m in self.terbaik(n=3): 
            baris.append(f"  {m}")
        return "\n".join(baris) + "\n"
