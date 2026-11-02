class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

    def tampilkan_info(self):
        return f"NIM: {self.nim}, Nama: {self.nama}"
if __name__ == "__main__":
    mhs = Mahasiswa("352071", "Rara")

    print(mhs.nim)
    print(mhs.nama)
    print(mhs.tampilkan_info())