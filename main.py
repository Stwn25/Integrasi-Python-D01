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

conn = psycopg2.connect(database='plis', user='postgres', password='iwanganteng', host='localhost', port=5432)
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

#~Page registrasi customer

def regis_cust():
    print("+========================================================+")
    print("|                     Registrasi                         |")
    print("+========================================================+")
    mandatory = Fore.RED + "*" + Fore.RESET
    nama_regis = input(f"Masukkan nama{mandatory}        : ")
    if nama_regis == '':
        time.sleep(2)
        clear()
        print("Input data registasi!\n")
        regis_cust()

    username_regis = input(f"Masukkan username{mandatory}    : ")
    if username_regis == '':
        time.sleep(2)
        clear()
        print("Input data registasi!\n")
        regis_cust()

    email_regis = input(f"Masukkan email{mandatory}       : ")
    if email_regis == '':
        time.sleep(2)
        clear()
        print("Input data registasi!\n")
        regis_cust()

    telp_regis = input(f"Masukkan no. telpon{mandatory}  : ")
    if telp_regis == '':
        time.sleep(2)
        clear()
        print("Input data registasi!\n")
        regis_cust()

    alamat_regis = input("Masukkan alamat       :")
    if alamat_regis == '':
        alamat_regis = "-"

    pw = input(f"Masukkan password{mandatory}    :")
    if alamat_regis == '':
        print("Input data password!")

    query_insert = "INSERT INTO customer (namacust, usernamecust, emailcust, telpcust, alamatcust, pwcust) VALUES (%s, %s, %s, %s, %s, %s)"
    cur.execute(query_insert, (nama_regis, username_regis, email_regis, telp_regis, alamat_regis, pw))
    time.sleep(2)

    conn.commit()
    print("\n")
    print("+========================================================+")
    print("|           Yeay, registrasi telah berhasil!             |")
    print("+========================================================+\n")
    print("Menuju halaman awal...")
    time.sleep(3)
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
        time.sleep(1)
        login_cust()
    else:
        user_login.append(access_masuk) #digunakan untuk mengidentifikasi user login

    pw_login = input("Masukkan password : ")
    if pw_login == '':
        print("Input password!")
        time.sleep(1)
        login_cust()

    query_login= f"SELECT * from customer WHERE usernamecust = '{access_masuk}' AND pwcust = '{pw_login}'"
    cur.execute(query_login)
    rows = cur.fetchone() 
    
    if rows is None:
        print("Username atau password salah!\n")
        input("Tekan enter untuk mencoba lagi...")
        login_cust()
    else:
        clear()
        print(Fore.GREEN + "Login berhasil!" + Fore.RESET)
        time.sleep(3)
        db_customer()


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
        time.sleep(1)
        login_admin()
    else:
        admin_login.append(access_masuk) #digunakan untuk mengidentifikasi user login

    pw_login = input("Masukkan password : ")
    if pw_login == '':
        print("Input password!")
        time.sleep(1)
        login_admin()

    query_login = f"SELECT * from admin WHERE telpadmin = '{access_masuk}' AND pwadmin = '{pw_login}'"
    cur.execute(query_login)
    rows = cur.fetchone() 
    
    if rows is None:
        print("no. telepon atau password salah\n")
        input("Tekan enter untuk mencoba lagi...")
        login_admin()
    else:
        clear()
        print(Fore.GREEN + "Login berhasil!" + Fore.RESET)
        time.sleep(3)
        db_admin()


#==================================================================================================================
                                                    # CUSTOMER
#==================================================================================================================

#~~~ dashboard customer

def db_customer():
    clear()
    print("+========================================================+")
    print("|              SELAMAT DATANG, CUSTOMER                  |")
    print("+========================================================+")
    print("|   [1]   Booking Peralatan                              |")
    print("|   [2]   Sedang Disewa                                  |")
    print("|   [3]   Riwayat Penyewaan                              |")
    print("|   [4]   Exit                                           |")
    print("+========================================================+")
    pilih_kode = input(" Pilih kode (1/2/3/4): ")

    if pilih_kode == '1':
        clear()
        booking_peralatan()
    elif pilih_kode == '2':
        None
    elif pilih_kode == '3':
        None
    elif pilih_kode == '4':
        None

def booking_peralatan():
    query_read = "SELECT noperalatan, namaperalatan, stokperalatan, hargasewa, keterangan FROM peralatan"
    cur.execute(query_read)
    rows = cur.fetchall()

    headers = ["Kode", "Nama Peralatan", "Stok Peralatan", "Harga Sewa", "Keterangan" ]
    print(tabulate(rows, headers=headers, tablefmt='pretty'))

    pilih = input("Kode peralatan yang ingin dibooking (enter, untuk batal) : ")
    if pilih == '':
        time.sleep(2)
        db_customer()
    else:
        jumlah = input("Jumlah yang ingin disewa    :")
        

   
    


query_update = "UPDATE peralatan SET namaperalatan = %s , stokperalatan = %s, hargasewa = %s, keterangan = %s, jenisperalatan_idjenis = %s WHERE noperalatan = %s"

        cur.execute(query_update, (nama_peralatan, stok, harga, keterangan, kode_jenis, Kode_peralatan))
        conn.commit()

#==================================================================================================================
                                                # END CUSTOMER
#==================================================================================================================


#==================================================================================================================
                                                    # ADMIN
#==================================================================================================================

#~~~ dashboard admin

def db_admin():
    clear()
    print("+========================================================+")
    print("|               SELAMAT DATANG, ADMIN                    |")
    print("+========================================================+")
    print("|   [1]   Kelola Peralatan                               |")
    print("|   [2]   Kelola Penyewaan                               |")
    print("|   [3]   Riwayat Penyewaan                              |")
    print("|   [4]   Exit                                           |")
    print("+========================================================+")
    pilih_kode = input(" Pilih kode (1/2/3/4): ")

    if pilih_kode == '1':
        clear()
        kelola_peralatan()
    elif pilih_kode == '2':
        None
    elif pilih_kode == '3':
        None
    elif pilih_kode == '4':
        None
    
#~~~Kelola Peralatan

def kelola_peralatan():
    clear()
    query = "SELECT * FROM peralatan"
    cur.execute(query)
    rows = cur.fetchall()

    headers = ["Kode", "Nama Peralatan", "Stok Peralatan", "Harga Sewa", "Keterangan", "Kode Jenis"]
    print(tabulate(rows, headers=headers, tablefmt='pretty'))

    print("1. Tambah Peralatan\n2. Update Peralatan\n3. Hapus Peralatan\n4. Kembali\n")
    pilih = input("Pilih Opsi: ")
    if pilih == "1":
        create_peralatan()
    elif pilih == "2":
        update_peralatan()
        print("\n")
    elif pilih == "3":
        delete_peralatan()
    elif pilih == "4":
        db_admin()
    else:
        None

def create_peralatan():
    query_read = "Select * from jenisperalatan"
    
    tanya = int(input("\nIngin memasukkan berapa data?: "))
    for i in range(tanya):
        no_peralatan = input("Kode peralatan (ex. BG01)     : ")
        nama_peralatan = input("Input nama barang             : ")
        stok_peralatan = int(input("Stok yang disewakan           : "))
        harga_sewa = int(input("Harga sewa (ex. 2000)         : "))
        keterangan = input("Keterangan barang             : ")
        cur.execute(query_read)
        data_jenis = cur.fetchall()

        headers = ["Kode Jenis", "Nama Jenis"]
        print(tabulate(data_jenis, headers=headers, tablefmt='pretty'))

        jenis_peralatan = input("Kode jenis (sesuai kode jenis diatas) : ")

        # query = f"INSERT INTO peralatan (noperalatan, namaperalatan, stokperalatan, hargasewa, keterangan, jenisperalatan_idjenis) VALUES ('{no_peralatan}', '{nama_peralatan}', '{stok_peralatan}', '{harga_sewa}','{keterangan}', '{jenis_peralatan}')"
        query = "INSERT INTO peralatan (noperalatan, namaperalatan, stokperalatan, hargasewa, keterangan, jenisperalatan_idjenis) VALUES (%s, %s, %s, %s, %s, %s)"

        cur.execute(query, (no_peralatan, nama_peralatan, stok_peralatan, harga_sewa, 
                            keterangan, jenis_peralatan))
    
    conn.commit()
    time.sleep(2)

    print("\n+========================================================+")
    print("|         Yeay, Create peralatan telah berhasil!         |")
    print("+========================================================+\n")
    time.sleep(3)
    kelola_peralatan()

    cur.close()
    conn.close()

def update_peralatan():
    Kode_peralatan = input("\nKode peralatan yang ingin diupdate : ")
    query_cek = f"SELECT * FROM peralatan WHERE noperalatan = '{Kode_peralatan}'"
    cur.execute(query_cek)
    rows = cur.fetchone()

    if rows is None:
        print("\nKode peralatan tidak tersedia!")
        input("Tekan enter untuk mencoba lagi...")
        update_peralatan()
    else:
        query_select = f"SELECT * FROM peralatan WHERE noperalatan = '{Kode_peralatan}'"
        cur.execute(query_select)
        row_select = cur.fetchone()

        print("\n(jika input tidak diberi value, maka value akan tetap)")
        nama_peralatan = input("Nama Peralatan    :") or row_select[1]
        stok = input("Stok Peralatan    :") or row_select[2]
        stok = int(stok)
        harga = input("Harga Sewa        :") or row_select[3]
        harga = int(harga)
        keterangan = input("Keterangan        :") or row_select[4]
        kode_jenis = input("Kode Jenis        :") or row_select[5]
    
        query_update = "UPDATE peralatan SET namaperalatan = %s , stokperalatan = %s, hargasewa = %s, keterangan = %s, jenisperalatan_idjenis = %s WHERE noperalatan = %s"

        cur.execute(query_update, (nama_peralatan, stok, harga, keterangan, kode_jenis, Kode_peralatan))
        conn.commit()

        time.sleep(2)
        print("\n+========================================================+")
        print("|         Yeay, Update peralatan telah berhasil!         |")
        print("+========================================================+\n")
        
        time.sleep(2)
        kelola_peralatan()

def delete_peralatan():
    delete = input("Kode peralatan yang ingin dihapus (klik enter, untuk batal): ")
    if delete == "":
        time.sleep(2)
        kelola_peralatan()
    else:
        query_delete = "DELETE FROM peralatan WHERE noperalatan = %s"
        cur.execute(query_delete, (delete,))
        conn.commit()

        time.sleep(2)
        print("\n+========================================================+")
        print("|                Delete peralatan berhasil!              |")
        print("+========================================================+\n")

        time.sleep(2)
        delete_peralatan()

#~~~Kelola Penyewaan
def kelola_penyewaan():
    None


#==================================================================================================================
                                                 # END ADMIN
#==================================================================================================================

#~~~Program

halaman_awal()