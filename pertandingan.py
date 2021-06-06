import sqlite3
from pendaftaran import Pendaftaran
from tabulate import tabulate

connection = sqlite3.connect("bola.in.db")

def tampilkan_data(connection):
    with connection:
         return connection.execute("SELECT * FROM pertandingan").fetchall()

def tambah_data(connection,tanggal_pertandingan,skor,tim,nama_kejuaraan):
    with connection:
         connection.execute("INSERT INTO pertandingan(tanggal_pertandingan,skor,tim,nama_kejuaraan) VALUES (?, ?, ?, ?);",(tanggal_pertandingan,skor,tim,nama_kejuaraan))

def edit_data(connection, tanggal_pertandingan,skor,tim,nama_kejuaraan,id):
    with connection:
        connection.execute("UPDATE pertandingan SET tanggal_pertandingan=?, skor=?, tim=?, nama_kejuaraan=? WHERE id=?;",(tanggal_pertandingan,skor,tim,nama_kejuaraan,id))
def hapus_data(connection, tanggal_pertandingan,skor,tim,nama_kejuaraan,id):
    with connection:
        connection.execute("DELETE FROM pertandingan WHERE id=?;",(id))

class Pertandingan(Pendaftaran):
    def __init__(self,tanggal_pertandingan,skor,tim,nama_kejuaraan):
        self._tanggal_pertandingan = tanggal_pertandingan
        self._skor = skor
        self._tim = tim
        self._nama_kejuaraan = nama_kejuaraan
    
    @property
    def getTanggal_Pertandingan(self):
        pass

    @getTanggal_Pertandingan.getter
    def getTanggal_Pertandingan(self):
        return self._tanggal_pertandingan

    @property
    def getSkor(self):
        pass

    @getSkor.getter
    def getSkor(self):
        return self._skor
    
    @property
    def getTim(self):
        pass

    @getTim.getter
    def getTim(self):
        return self._tim

    @property
    def getNama_Kejuaraan(self):
        pass

    @getNama_Kejuaraan.getter
    def getNama_Kejuaraan(self):
        return self._nama_kejuaraan

    @staticmethod
    def tambah_pertandingan(connection):
        pertandingan = Pertandingan(input("Masukkan Tanggal Pertandingan: "), input("Masukkan Skor: "), input("Masukkan Tim: "),input("Masukkan Nama Kejuaraan: "))
        tambah_data(connection, pertandingan.getTanggal_Pertandingan, pertandingan.getSkor, pertandingan.getTim, pertandingan.getNama_Kejuaraan)

    @staticmethod
    def tampilkan_pertandingan(connection):
        pertandingan = tampilkan_data(connection)
        header = ["ID", "Tanggal_Pertandingan", "Skor", "Tim", "Nama_Kejuaraan"]

        result = []

        for data in pertandingan:
            result.append(data)
        return print (tabulate(result, headers = header))

    @staticmethod
    def edit_pertandingan(connection):
        id = input("Masukkan ID yang Ingin Diperbarui ")
        pertandingan =Pertandingan(input("Masukkan Tanggal Pertandingan: "), input("Masukkan Skor: "), input("Masukkan Tim: "),input("Masukkan Nama Kejuaraan: "))
        edit_data(connection, pertandingan.getTanggal_Pertandingan, pertandingan.getSkor, pertandingan.getTim, pertandingan.getNama_Kejuaraan, id)
        
    @staticmethod
    def hapus_pertandingan(connection):
        id = input("Masukkan ID yang Ingin Dihapus ")
        hapus_data(connection, Pertandingan.getTanggal_Pertandingan, Pertandingan.getSkor, Pertandingan.getTim, Pertandingan.getNama_Kejuaraan, id)
