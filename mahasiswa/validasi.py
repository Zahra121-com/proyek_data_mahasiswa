def cek_kosong(nilai, nama):
    nilai = nilai.strip()
    if nilai == "":
        raise ValueError(f"{nama} wajib diisi")
    return nilai

def cek_semester(teks):
    try:
        semester = int(teks)
    except ValueError:
        raise ValueError("semester harus berupa angka bulat")
    if semester < 1 or semester > 14:
        raise ValueError("semester harus 1 sampai 14")
    return semester

def cek_ipk(teks):
    try:
        ipk = float(teks)
    except ValueError:
        raise ValueError("IPK harus berupa angka")
    if ipk < 0 or ipk > 4:
        raise ValueError("IPK harus 0.0 sampai 4.0")
    return ipk

if __name__ == "__main__":
    assert cek_ipk("3.5") == 3.5
    assert cek_semester("3") == 3
    print("validasi.py OK")
