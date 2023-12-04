# Menambahkan Inputan Data
def tambah(nama, nilai):
    data[nama] = nilai

# Menampilkan Data inputan
def tampilkan():
    for nama, nilai in data.items():
        print(f"| Nama: {nama} \t| Nilai: {nilai}\t|")

# Menghapus Data Inputan
def hapus(nama):
    del data[nama]

# Mengubah Data Inputan
def ubah(nama, nilai):
    data[nama] = nilai

data = {}

print("Data mahasiswa :")
tambah("uyun", 85)
tambah("arul", 90)
tambah("nurul", 78)
print('=================================')
tampilkan()
print('=================================')

hapus("nurul")
print("Output setelah dihapus :")
print('=================================')
tampilkan()
print('=================================')

ubah("uyun", 92)
print("Output setelah diubah :")
print('=================================')
tampilkan()
print('=================================')