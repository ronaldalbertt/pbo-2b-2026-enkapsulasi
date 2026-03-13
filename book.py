import datetime
class Book:
    def __init__(self, id_buku, judul, penulis, tahun):
        self.__id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.status = "tersedia"
        self.__update_terakhir = datetime.datetime.now()

    def update_judul(self, judul_baru):
        self.judul = judul_baru
        self.__update_terakhir = datetime.datetime.now()

    def get_update_terakhir(self):
        return self.__update_terakhir