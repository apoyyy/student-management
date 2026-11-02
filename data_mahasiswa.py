class DataMahasiswa:
    def __init__(self):
        self.data = {}

    def tambah(self, mahasiswa):
        if mahasiswa.nim in self.data:
            return False

        self.data[mahasiswa.nim] = mahasiswa
        return True

    def cari(self, nim):
        return self.data.get(nim)

    def hapus(self, nim):
        if nim in self.data:
            del self.data[nim]
            return True

        return False