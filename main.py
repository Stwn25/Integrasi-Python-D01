import psycopg2
import pandas as pd
import os
def clear(): 
    os.system('cls')
import time
import datetime
from tabulate import tabulate
from colorama import init, Fore
datetime = datetime.datetime.now()

conn = psycopg2.connect(database='Basda', user='postgres', password='iwanganteng', host='localhost', port=5432)
cur = conn.cursor()

#~~~Page awal

def halaman_awal():
    clear()
    print("+========================================================+")
    print("|                    SELAMAT DATANG DI                   |")
    print("|                      GH ADVENTURE                      |")
    print("+========================================================+")
    print("|   [1]   Sign In Customer                               |")
    print("|   [2]   Login Customer                                 |")
    print("|   [3]   Login Admin                                    |")
    print("|   [4]   Exit                                           |")
    print("+========================================================+")
    pilih_kode = input(" Pilih kode (1/2/3/4): ")
    if pilih_kode == '1':
        clear()
        regis_cust()
    elif pilih_kode == '2':
        clear()
        login_cust()
    elif pilih_kode == '3':
        clear()
        login_admin()
    elif pilih_kode == '4':
        exit
    else:
        print("\nMasukkan input yang sesuai!\n")
        halaman_awal()



#~Page login customer

user_login = []

def login_cust():
    clear()
    print("+========================================================+")
    print("|                   LOGIN as CUSTOMER                    |")
    print("+========================================================+")
    access_masuk = input("Masukkan username : ")
    if access_masuk == '':
        print("Input username!")
        time.sleep(2)
        return login_cust()
    else:
        user_login.append(access_masuk) #digunakan untuk mengidentifikasi user login

    pw_login = input("Masukkan password : ")
    if pw_login == '':
        print("Input password!")
        time.sleep(3)
        return login_cust()

    query_login_cust = f"SELECT * from customer WHERE usernamecust = '{access_masuk}' AND pwcust = '{pw_login}'"
    cur.execute(query_login_cust)
    rows = cur.fetchone() 
    
    if rows is None:
        print("Username atau password salah\n")
        input("Tekan enter untuk mencoba lagi...")
        return login_cust()
    else:
        clear()
        print(Fore.GREEN + "Login berhasil!" + Fore.RESET)
        time.sleep(3)
        return db_customer()


#~login admin
admin_login = []

def login_admin():
    clear()
    print("+========================================================+")
    print("|                     LOGIN as ADMIN                     |")
    print("+========================================================+")
    access_masuk = input("Masukkan no. telepon : ")
    if access_masuk == '':
        print("Input no. telepon!")
        time.sleep(2)
        return login_admin()
    else:
        admin_login.append(access_masuk) #digunakan untuk mengidentifikasi user login

    pw_login = input("Masukkan password : ")
    if pw_login == '':
        print("Input password!")
        time.sleep(3)
        return login_admin()

    query_login_cust = f"SELECT * from admin WHERE telpadmin = '{access_masuk}' AND pwadmin = '{pw_login}'"
    cur.execute(query_login_cust)
    rows = cur.fetchone() 
    
    if rows is None:
        print("no. telepon atau password salah\n")
        input("Tekan enter untuk mencoba lagi...")
        return login_admin()
    else:
        clear()
        print(Fore.GREEN + "Login berhasil!" + Fore.RESET)
        time.sleep(3)
        return db_admin()

#~~~ dashboard customer
def db_customer():
    clear()
    
#~~~ dashboard admin
def db_admin():
    clear()
    print("+========================================================+")
    print("|                      SELAMAT DATANG                    |")
    print("+========================================================+")
    print("|   [1]   Kelola Peralatan                               |")
    print("|   [2]   Booking Customer                               |")
    print("|   [3]   Riwayat Transaksi                              |")
    print("|   [4]   Exit                                           |")
    print("+========================================================+")

    pilih_kode = input(" Pilih kode (1/2/3/4): ")
    
























def kelola_peralatan():
    print("1. Tambah Peralatan\n2. Lihat Peralatan")
    pilih = input("Pilih Opsi: ")
    if pilih == "1":
        create_peralatan()
    elif pilih == "2":
        print("\n")
        read_peralatan()
        print("\n")


def read_peralatan():
    lihat_data = "Select * from peralatan"
    cur.execute(lihat_data)
    data = cur.fetchall()
    headers = ["Kode Peralatan", "Nama Peralatan", "Stok", "Harga Sewa", "Keterangan", "Kode Jenis"]
    print(tabulate(data, headers=headers, tablefmt="grid"))
    cur.close() 
    conn.close()

def create_peralatan():
    data_peralatan = "Select * from peralatan"
    data_jenis_peralatan = "Select * from jenisperalatan"
    cur.execute(data_peralatan)
    data_alat = cur.fetchall()
    print("\nDaftar peralatan yang tersedia: ")
    for row in data_alat:
        print(row)
    cur.execute(data_jenis_peralatan)
    data_jenis = cur.fetchall()
    print("\nKode jenis peralatan: ")
    for row in data_jenis:
        print(row)

    tanya = int(input("\nIngin memasukkan berapa data?: "))
    for i in range(tanya):
        no_peralatan = input("Kode peralatan (ex. BG01): ")
        nama_peralatan = input("Input nama barang: ")
        stok_peralatan = int(input("Stok yang disewakan: "))
        harga_sewa = int(input("Harga sewa (ex. 2000): "))
        keterangan = input("Keterangan barang: ")
        jenis_peralatan = input("Kode jenis (sesuai kode jenis diatas): ")
        query = f"INSERT INTO peralatan (noperalatan, namaperalatan, stokperalatan, hargasewa, keterangan, jenisperalatan_idjenis) VALUES ('{no_peralatan}', '{nama_peralatan}', '{stok_peralatan}', '{harga_sewa}','{keterangan}', '{jenis_peralatan}')"
        # query = f"INSERT INTO peralatan (noperalatan, namaperalatan, stokperalatan, 
        # hargasewa, keterangan, jenisperalatan_idjenis) VALUES (%s, %s, %s, %s, %s, %s)"

        cur.execute(query, (no_peralatan, nama_peralatan, stok_peralatan, harga_sewa, 
                            keterangan, jenis_peralatan))

    conn.commit()
    cur.close()
    conn.close()



halaman_awal()