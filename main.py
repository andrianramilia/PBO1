import login
import pendaftaran
import pertandingan
import klasemen
import statistik
import sqlite3
connection = sqlite3.connect("bola.in.db")

def Menu():
    print('-------SELAMAT DATANG DI APLIKASI DATA BOLA.IN-------')
    print('[1] kelas klasmen')
    print('[2] kelas login')
    print('[3] kelas pendaftaran')
    print('[4] kelas pertandingan')
    print('[5] kelas statistik')
    print('[6] exit')
    
    kelas = int(input('Silahkan Pilih kelas '))
    if kelas < 1:
        print("Pilihan Anda Tidak Tersedia, silahkan masukkan kelas kembali")
        Menu()
    elif kelas > 6:
        print("Pilihan Anda Tidak Tersedia, silahkan masukkan kelas kembali")
        Menu()
    while (kelas == 6):
        print("Terima Kasih")
        exit()

    print('[1] melihat data')
    print('[2] menambah data')
    print('[3] mengubah data')
    print('[4] menghapus data')
    print('[5] kembali')

    menu = int(input('Silahkan pilih kegiatan '))
    while (menu < 1):
        print("Input Anda Salah")
        menu = int(input('Silahkan pilih kegiatan '))
    while (menu > 5):
        print("Input Anda Salah")
        menu = int(input('Silahkan pilih kegiatan '))

    
    if kelas == 1 and menu == 1:
        klasemen.Klasemen.tampilkan_klasemen(connection)
    elif kelas == 1 and menu == 2:
        klasemen.Klasemen.tambah_klasemen(connection)
    elif kelas == 1 and menu == 3:
        klasemen.Klasemen.edit_klasemen(connection)
    elif kelas == 1 and menu == 4:
        klasemen.Klasemen.hapus_klasemen(connection)
    
    elif kelas == 2 and menu == 1:
        login.Login.tampilkan_login(connection)
    elif kelas == 2 and menu == 2:
        login.Login.tambah_login(connection)
    elif kelas == 2 and menu == 3:
        login.Login.edit_login(connection)
    elif kelas == 2 and menu == 4:
        login.Login.hapus_login(connection)

    elif kelas == 3 and menu == 1:
        pendaftaran.Pendaftaran.tampilkan_pendaftaran(connection)
    elif kelas == 3 and menu == 2:
        pendaftaran.Pendaftaran.tambah_pendaftaran(connection)
    elif kelas == 3 and menu == 3:
        pendaftaran.Pendaftaran.edit_pendaftaran(connection)
    elif kelas == 3 and menu == 4:
        pendaftaran.Pendaftaran.hapus_pendaftaran(connection)

    elif kelas == 4 and menu == 1:
        pertandingan.Pertandingan.tampilkan_pertandingan(connection)
    elif kelas == 4 and menu == 2:
        pertandingan.Pertandingan.tambah_pertandingan(connection)
    elif kelas == 4 and menu == 3:
        pertandingan.Pertandingan.edit_pertandingan(connection)
    elif kelas == 4 and menu == 4:
        pertandingan.Pertandingan.hapus_pertandingan(connection)

    elif kelas == 5 and menu == 1:
        statistik.Statistik.tampilkan_statistik(connection)
    elif kelas == 5 and menu == 2:
        statistik.Statistik.tambah_statistik(connection)
    elif kelas == 5 and menu == 3:
        statistik.Statistik.edit_statistik(connection)
    elif kelas == 5 and menu == 4:
        statistik.Statistik.hapus_statistik(connection)
    elif menu == 5:
        Menu()
    else:
        print('program tidak tersedia, silahkan masukkan menu kembali')
    

if __name__ == "__main__":
    while(True):
        Menu()