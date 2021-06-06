import sqlite3
from tabulate import tabulate

connection = sqlite3.connect("bola.in.db")

def tampilkan_data(connection):
    with connection:
         return connection.execute("SELECT * FROM pendaftaran").fetchall()

def tambah_data(connection, tim, nama_kejuaraan,pemain):
    with connection:
         connection.execute("INSERT INTO pendaftaran (tim, nama_kejuaraan, pemain) VALUES (?, ?, ?);",(tim,nama_kejuaraan,pemain))

def edit_data(connection, tim, nama_kejuaraan,pemain,id):
    with connection:
        connection.execute("UPDATE pendaftaran SET tim=?, nama_kejuaraan=?, pemain=? WHERE id=?;",(tim,nama_kejuaraan,pemain,id))
def hapus_data(connection, tim, nama_kejuaraan,pemain,id):
    with connection:
        connection.execute("DELETE FROM pendaftaran WHERE id=?;",(id))

class Pendaftaran():
    def __init__(self,tim,nama_kejuaraan,pemain):
        self._tim = tim
        self._nama_kejuaraan = nama_kejuaraan
        self._pemain = pemain
    
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
    def Nama_Kejuaraan(self):
        return self._nama_kejuaraan
    
    @property
    def getPemain(self):
        pass

    @getPemain.getter
    def getPemain(self):
        return self._pemain

    @staticmethod
    def tambah_pendaftaran(connection):
        pendaftaran = Pendaftaran(input("Masukkan Nama Tim: "), input("Masukkan Nama Kejuaraan: "), input("Masukkan Nama Pemain: "))
        tambah_data(connection, pendaftaran.getTim, pendaftaran.getNama_Kejuaraan, pendaftaran.getPemain)

    @staticmethod
    def tampilkan_pendaftaran(connection):
        pendaftaran = tampilkan_data(connection)
        header = ["ID", "Tim", "Nama_Kejuaraan", "Pemain"]

        result = []

        for data in pendaftaran:
            result.append(data)
        return print (tabulate(result, headers = header))

    @staticmethod
    def edit_pendaftaran(connection):
        id = input("Masukkan ID yang Ingin Diperbarui ")
        pendaftaran = Pendaftaran(input("Masukkan Nama Tim: "), input("Masukkan Nama Kejuaraan: "), input("Masukkan Nama Pemain: "))
        edit_data(connection, pendaftaran.getTim, pendaftaran.getNama_Kejuaraan, pendaftaran.getPemain, id)
        
    @staticmethod
    def hapus_pendaftaran(connection):
        id = input("Masukkan ID yang Ingin Dihapus ")
        hapus_data(connection, Pendaftaran.getTim, Pendaftaran.getNama_Kejuaraan, Pendaftaran.getPemain, id)
