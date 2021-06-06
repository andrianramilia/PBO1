
import sqlite3
from tabulate import tabulate

connection = sqlite3.connect("bola.in.db")

def tampilkan_data(connection):
    with connection:
         return connection.execute("SELECT * FROM login").fetchall()

def tambah_data(connection, nama, email, password):
    with connection:
         connection.execute("INSERT INTO login (nama, email, password) VALUES (?, ?, ?);",(nama,email,password))

def edit_data(connection,nama, email, password,id):
    with connection:
        connection.execute("UPDATE login SET nama=?, email=?, password=? WHERE id=?;",(nama,email,password,id))
def hapus_data(connection,nama,email, password,id):
    with connection:
        connection.execute("DELETE FROM login WHERE id=?;",(id))

class Login():
    def __init__(self,nama,email,password):
        self._nama = nama
        self._email = email
        self._password = password
    
    @property
    def getNama(self):
        pass

    @getNama.getter
    def getNama(self):
        return self._nama

    @property
    def getEmail(self):
        pass

    @getEmail.getter
    def getEmail(self):
        return self._email
    
    @property
    def getPassword(self):
        pass

    @getPassword.getter
    def getPassword(self):
        return self._password

    @staticmethod
    def tambah_login(connection):
        login = Login(input("Masukkan Nama Anda: "), input("Masukkan Email Anda: "), input("Masukkan Password Anda: "))
        tambah_data(connection, login.getNama, login.getEmail, login.getPassword)

    @staticmethod
    def tampilkan_login(connection):
        login = tampilkan_data(connection)
        header = ["ID", "Nama", "Email", "Password"]

        result = []

        for data in login:
            result.append(data)
        return print (tabulate(result, headers = header))

    @staticmethod
    def edit_login(connection):
        id = input("Masukkan ID yang Ingin Diperbarui ")
        login = Login(input("Masukkan Nama Anda: "), input("Masukkan Username Anda: "), input("Masukkan Password Anda: "))
        edit_data(connection, login.getNama, login.getEmail, login.getPassword, id)
        
    @staticmethod
    def hapus_login(connection):
        id = input("Masukkan ID yang Ingin Dihapus ")
        hapus_data(connection, Login.getNama, Login.getEmail, Login.getPassword, id)



    

 


