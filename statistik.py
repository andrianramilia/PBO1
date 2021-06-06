import sqlite3
from pendaftaran import Pendaftaran
from tabulate import tabulate

connection = sqlite3.connect("bola.in.db")

def tampilkan_data(connection):
    with connection:
         return connection.execute("SELECT * FROM statistik").fetchall()

def tambah_data(connection,gol_terbanyak,umpan_terbanyak,kartu_merah,kartu_kuning,tim,pemain,nama_kejuaraan):
    with connection:
         connection.execute("INSERT INTO statistik(gol_terbanyak,umpan_terbanyak,kartu_merah,kartu_kuning,tim,pemain,nama_kejuaraan) VALUES (?, ?, ?, ?, ?, ?, ?);",(gol_terbanyak,umpan_terbanyak,kartu_merah,kartu_kuning,tim,pemain,nama_kejuaraan))

def edit_data(connection,gol_terbanyak,umpan_terbanyak,kartu_merah,kartu_kuning,tim,pemain,nama_kejuaraan,id):
    with connection:
        connection.execute("UPDATE statistik SET gol_terbanyak=?,umpan_terbanyak=?,kartu_merah=?,kartu_kuning=?,tim=?,pemain=?,nama_kejuaraan=? WHERE id=?;",(gol_terbanyak,umpan_terbanyak,kartu_merah,kartu_kuning,tim,pemain,nama_kejuaraan,id))

def hapus_data(connection,gol_terbanyak,umpan_terbanyak,kartu_merah,kartu_kuning,tim,pemain,nama_kejuaraan,id):
    with connection:
        connection.execute("DELETE FROM klasemen WHERE id=?;",(id))

class Statistik(Pendaftaran):
    def __init__(self,gol_terbanyak,umpan_terbanyak,kartu_merah,kartu_kuning,tim,pemain,nama_kejuaraan):
        self._gol_terbanyak = gol_terbanyak
        self._umpan_terbanyak = umpan_terbanyak
        self._kartu_merah = kartu_merah
        self._kartu_kuning = kartu_kuning
        self._tim = tim
        self._pemain = pemain
        self._nama_kejuaraan = nama_kejuaraan
    
    @property
    def getGol_Terbanyak(self):
        pass

    @getGol_Terbanyak.getter
    def getGol_Terbanyak(self):
        return self._gol_terbanyak

    @property
    def getUmpan_Terbanyak(self):
        pass

    @getUmpan_Terbanyak.getter
    def getUmpan_Terbanyak(self):
        return self._umpan_terbanyak
    
    @property
    def getKartu_Merah(self):
        pass

    @getKartu_Merah.getter
    def getKartu_Merah(self):
        return self._kartu_merah

    @property
    def getKartu_Kuning(self):
        pass

    @getKartu_Kuning.getter
    def getKartu_Kuning(self):
        return self._kartu_kuning

    @property
    def getTim(self):
        pass

    @getTim.getter
    def getTim(self):
        return self._tim

    @property
    def getPemain(self):
        pass

    @getPemain.getter
    def getPemain(self):
        return self._pemain

    @property
    def getNama_Kejuaraan(self):
        pass

    @getNama_Kejuaraan.getter
    def getNama_Kejuaraan(self):
        return self._nama_kejuaraan


    @staticmethod
    def tambah_statistik(connection):
        statistik = Statistik(input("Masukkan Gol Terbanyak: "), input("Masukkan Umpan Terbanyak: "),input("Masukkan Kartu Merah: "), input("Masukkan Kartu Kuning: "), input("Masukkan Nama Tim: "), input("Masukkan Nama Pemain : "),input("Masukkan Nama Kejuaraan: "))
        tambah_data(connection, statistik.getGol_Terbanyak,statistik.getUmpan_Terbanyak,statistik.getKartu_Merah,statistik.getKartu_Kuning,statistik.getTim,statistik.getPemain,statistik.getNama_Kejuaraan)

    @staticmethod
    def tampilkan_statistik(connection):
        statistik = tampilkan_data(connection)
        header = ["ID", "Gol Terbanyak", "Umpan Terbanyak", "Kartu Merah", "Kartu Kuning", "Nama Tim", "Pemain", "Nama Kejuaraan"]

        result = []

        for data in statistik:
            result.append(data)
        return print (tabulate(result, headers = header))

    @staticmethod
    def edit_statistik(connection):
        id = input("Masukkan ID yang Ingin Diperbarui ")
        statistik = Statistik(input("Masukkan Gol Terbanyak: "), input("Masukkan Umpan Terbanyak: "),input("Masukkan Kartu Merah: "), input("Masukkan Kartu Kuning: "), input("Masukkan Nama Tim: "), input("Masukkan Nama Pemain : "),input("Masukkan Nama Kejuaraan: "))
        edit_data(connection, statistik.getGol_Terbanyak,statistik.getUmpan_Terbanyak,statistik.getKartu_Merah,statistik.getKartu_Kuning,statistik.getTim,statistik.getPemain,statistik.getNama_Kejuaraan, id)
    
    @staticmethod
    def hapus_statistik(connection):
        id = input("Masukkan ID yang Ingin Dihapus ")
        hapus_data(connection, Statistik.getGol_Terbanyak,Statistik.getUmpan_Terbanyak,Statistik.getKartu_Merah,Statistik.getKartu_Kuning,Statistik.getTim,Statistik.getPemain,Statistik.getNama_Kejuaraan, id)