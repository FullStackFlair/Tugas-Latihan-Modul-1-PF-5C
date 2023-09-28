# Sistem Penilaian Akhir Mahasiswa
# Tambahkan fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(uts, uas):
    return (uts + uas) / 2

# Tambahkan fungsi untuk menghitung nilai akhir semua mahasiswa
def hitung_nilai_akhir_keseluruhan(data_mahasiswa):
    nilai_akhir_mahasiswa = {}
    for nama, nilai in data_mahasiswa.items():
        uts, uas = nilai["uts"], nilai["uas"]
        nilai_akhir = hitung_nilai_akhir(uts, uas)
        nilai_akhir_mahasiswa[nama] = nilai_akhir
    return nilai_akhir_mahasiswa

def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa :")
    for nama, nilai_akhir, in data_nilai_akhir.items():
        print("Nama : {}\t\tNilai Akhir : {:.2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        #Data Mahasiswa (nama sebagai key dan nilai UTS serta UAS sebagai value dalam bentuk dictionary)
        "Bahrul Ulum    "   : {"uts" : 80, "uas" : 90},
        "Danu Fadillah  " : {"uts" : 70, "uas" : 85},
        "Candra Setio   "  : {"uts" : 90, "uas" : 75}
    }

    data_nilai_akhir = hitung_nilai_akhir_keseluruhan(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()