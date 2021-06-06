import sqlite3
from pendaftaran import Pendaftaran
from tabulate import tabulate

connection = sqlite3.connect("bola.in.db")

def tampilkan_data(connection):
    with connection:
         return connection.execute("SELECT * FROM klasemen").fetchall()

def tambah_data(connection,tim,nama_kejuaraan,jumlah_main,jumlah_menang,jumlah_kalah,poin,jumlah_pertandingan):
    with connection:
         connection.execute("INSERT INTO klasemen(tim,nama_kejuaraan,jumlah_main,jumlah_menang,jumlah_kalah,poin,jumlah_pertandingan) VALUES (?, ?, ?, ?, ?, ?, ?);",(tim,nama_kejuaraan,jumlah_main,jumlah_menang,jumlah_kalah,poin,jumlah_pertandingan))

def edit_data(connection,tim,nama_kejuaraan,jumlah_main,jumlah_menang,jumlah_kalah,poin,jumlah_pertandingan,id):
    with connection:
        connection.execute("UPDATE klasemen SET tim =?,nama_kejuaraan=?,jumlah_main=?,jumlah_menang=?,jumlah_kalah=?,poin=?,jumlah_pertandingan=? WHERE id=?;",(tim,nama_kejuaraan,jumlah_main,jumlah_menang,jumlah_kalah,poin,jumlah_pertandingan,id))
def hapus_data(connection,tim,nama_kejuaraan,jumlah_main,jumlah_menang,jumlah_kalah,poin,jumlah_pertandingan,id):
    with connection:
        connection.execute("DELETE FROM klasemen WHERE id=?;",(id))

class Klasemen(Pendaftaran):
    def __init__(self,tim,nama_kejuaraan,jumlah_main,jumlah_menang,jumlah_kalah,poin,jumlah_pertandingan):
        self._tim = tim
        self._nama_kejuaraan = nama_kejuaraan
        self._jumlah_main = jumlah_main
        self._jumlah_menang = jumlah_menang
        self._jumlah_kalah = jumlah_kalah
        self._poin = poin
        self._jumlah_pertandingan = jumlah_pertandingan
    
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
    
    @property
    def getJumlah_Main(self):
        pass

    @getJumlah_Main.getter
    def getJumlah_Main(self):
        return self._jumlah_main

    @property
    def getJumlah_Menang(self):
        pass

    @getJumlah_Menang.getter
    def getJumlah_Menang(self):
        return self._jumlah_menang

    @property
    def getJumlah_Kalah(self):
        pass

    @getJumlah_Kalah.getter
    def getJumlah_Kalah(self):
        return self._jumlah_kalah

    @property
    def getPoin(self):
        pass

    @getPoin.getter
    def getPoin(self):
        return self._poin

    @property
    def getJumlah_Pertandingan(self):
        pass

    @getJumlah_Pertandingan.getter
    def getJumlah_Pertandingan(self):
        return self._jumlah_pertandingan


    @staticmethod
    def tambah_klasemen(connection):
        klasemen = Klasemen(input("Masukkan Nama Tim: "), input("Masukkan Nama Kejuaraan: "),input("Masukkan Jumlah Main: "), input("Masukkan Jumlah Menang: "), input("Masukkan Jumlah Kalah: "), input("Masukkan Poin : "),input("Masukkan Jumlah_Pertandingan: "))
        tambah_data(connection, klasemen.getTim,klasemen.getNama_Kejuaraan,klasemen.getJumlah_Main,klasemen.getJumlah_Menang,klasemen.getJumlah_Kalah,klasemen.getPoin,klasemen.getJumlah_Pertandingan)

    @staticmethod
    def tampilkan_klasemen(connection):
        klasemen = tampilkan_data(connection)
        header = ["ID", "Nama Tim", "Nama Kejuaraan", "Jumlah Main", "Jumlah Menang", "Jumlah Kalah", "Poin", "Jumlah Pertandingan"]

        result = []

        for data in klasemen:
            result.append(data)
        return print (tabulate(result, headers = header))

    @staticmethod
    def edit_klasemen(connection):
        id = input("Masukkan ID yang Ingin Diperbarui ")
        klasemen = Klasemen(input("Masukkan Nama Tim: "), input("Masukkan Nama Kejuaraan: "),input("Masukkan Jumlah Main: "), input("Masukkan Jumlah Menang: "), input("Masukkan Jumlah Kalah: "), input("Masukkan Poin : "),input("Masukkan Jumlah_Pertandingan: "))
        edit_data(connection, klasemen.getTim,klasemen.getNama_Kejuaraan,klasemen.getJumlah_Main,klasemen.getJumlah_Menang,klasemen.getJumlah_Kalah,klasemen.getPoin,klasemen.getJumlah_Pertandingan,id)
    @staticmethod
    def hapus_klasemen(connection):
        id = input("Masukkan ID yang Ingin Dihapus ")
        hapus_data(connection, Klasemen.getTim,Klasemen.getNama_Kejuaraan,Klasemen.getJumlah_Main,Klasemen.getJumlah_Menang,Klasemen.getJumlah_Kalah,Klasemen.getPoin,Klasemen.getJumlah_Pertandingan,id)