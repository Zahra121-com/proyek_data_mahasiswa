import os
import tempfile
import unittest
from . import fileio
from .processing import Mahasiswa, DaftarMahasiswa, hitung_rata
from .validasi import cek_ipk, cek_semester

class TestMahasiswa(unittest.TestCase):
    def setUp(self):
        self.daftar = DaftarMahasiswa([
            Mahasiswa("001", "Zahra", "Ilmu komputer", "3", "3.75"),
            Mahasiswa("002", "Bela", "Manajemen Informatika", "5", "3.20"),
            Mahasiswa("003", "Chintya", "Sistem Informasi", "7", "2.80")])

    def test_ipk_di_luar_rentang(self):
        with self.assertRaises(ValueError):
            cek_ipk("4.5")

    def test_semester_bukan_angka(self):
        with self.assertRaises(ValueError):
            cek_semester("abc")

    def test_field_kosong(self):
        with self.assertRaises(ValueError):
            Mahasiswa("", "Chintya", "Sistem informasi", "3", "3.5")

    def test_nim_duplikat(self):
        with self.assertRaises(ValueError):
            self.daftar.tambah(Mahasiswa("001", "Bela", "Manajemen Informatika", "1", "3.0"))

    def test_hitung_rata_args(self):
        self.assertEqual(hitung_rata(2, 4, 6), 4)

    def test_filter_ipk(self):
        self.assertEqual(len(self.daftar.filter_ipk(minimal=3.0)), 2)

    def test_terbaik(self):
        self.assertEqual(self.daftar.terbaik(n=1)[0].nama, "Zahra")

    def test_cari_nama(self):
        self.assertEqual(self.daftar.cari_nama("chin")[0].nim, "003")

    def test_file_baris_rusak_dilewati(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "data.txt")
            fileio.buat_file(path)
            fileio.tambah_file(path, Mahasiswa("001", "Zahra", "Ilmu Komputer", "3", "3.75"))
            with open(path, "a", encoding="utf-8") as f:
                f.write("rusak|data\n")
            self.assertEqual(len(fileio.baca_file(path)), 1)

if __name__ == "__main__":
    unittest.main()
