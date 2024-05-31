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
# user_login_value = user_login[0] if user_login else None

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
        user_login.clear()
        login_cust()
    else:
        clear()
        print(Fore.GREEN + "Login berhasil!" + Fore.RESET)
        time.sleep(3)
        db_customer()


#~login admin

admin_login = ''

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
    print("|   [2]   Penyewaan (sedang disewa/ sedang booking)      |")
    print("|   [3]   Riwayat Penyewaan                              |")
    print("|   [4]   Exit                                           |")
    print("+========================================================+")
    pilih_kode = input(" Pilih kode (1/2/3/4): ")

    if pilih_kode == '1':
        clear()
        booking_peralatan()
    elif pilih_kode == '2':
        clear()
        sedang_disewa()
    elif pilih_kode == '3':
        clear()
        riwayat_peminjaman()
    elif pilih_kode == '4':
        None

def booking_peralatan():
    clear()
    query_read = "SELECT noperalatan, namaperalatan, stokperalatan, hargasewa, keterangan FROM peralatan"
    cur.execute(query_read)
    rows = cur.fetchall()

    headers = ["Kode", "Nama Peralatan", "Stok Peralatan", "Harga Sewa", "Keterangan" ]
    print(tabulate(rows, headers=headers, tablefmt='pretty'))

    pilih = input("Kode peralatan yang ingin dibooking (b, untuk batal) : ")
    query_cek = f"SELECT * FROM peralatan WHERE noperalatan = '{pilih}'"
    cur.execute(query_cek)
    rows = cur.fetchone()

    if pilih == 'b':
        time.sleep(2)
        booking_peralatan()
    elif rows is None:
        print("\nKode peralatan tidak tersedia!")
        input("Tekan enter untuk mencoba lagi...")
        booking_peralatan()
    else:
        jumlah = int(input("Jumlah yang ingin disewa    :"))
        jumlah1 = rows[3] * jumlah 
        tgl_pengambilan = input("Tanggal pengambilan (yyyy-mm-dd)   :")
        tgl_pengembalian = input("Tanggal pengembalian (yyyy-mm-dd)   :")
        tgl_pengambilan_date = datetime.strptime(tgl_pengambilan, "%Y-%m-%d")
        tgl_pengembalian_date = datetime.strptime(tgl_pengembalian, "%Y-%m-%d")
        selisih_hari = tgl_pengembalian_date - tgl_pengambilan_date
        selisih_hari_int = selisih_hari.days
        total_harga = jumlah1 * selisih_hari_int

        print("\n+==============================================================+")
        print(f"|   Customer: {user_login}                                       |")
        print(f"|                                                              |")
        print(f"|      Kode Peralatan        : {pilih}                             |")
        print(f"|      Stok yang disewa      : {jumlah}                               |")
        print(f"|      Tanggal Pengambilan   : {tgl_pengambilan}                      |")
        print(f"|      Tanggal Pengembalian  : {tgl_pengembalian}                      |")
        print(f"|      Durasi Penyewaan      : {selisih_hari}                 |")
        print(f"|      Harga Sewa            : {total_harga}                           |")
        print(f"|                                                              |")
        print(f"|             [c] Cancel           [k] konfirmasi              |")
        print("+==============================================================+")
        
        def konfirmasi():
            konfirm = input("(c/k) : ")
            if konfirm == 'c':
                time.sleep(2)
                booking_peralatan()
            elif konfirm == 'k':
                cur.execute("SELECT idcust FROM customer WHERE usernamecust = %s", (user_login[0],))
                idcust = cur.fetchone()[0]

                query_pembayaran = "INSERT INTO pembayaran (keterangan) VALUES(%s) RETURNING idpembayaran"
                cur.execute(query_pembayaran, (f"Pembayaran oleh {user_login}",))
                idpembayaran = cur.fetchone()[0]
                conn.commit()

                query_transaksi = "INSERT INTO transaksi (tglpengambilan, tglpengembalian, customer_idcust, admin_noadmin, pembayaran_idpembayaran) VALUES (%s, %s, %s, %s, %s) RETURNING notransaksi"
                cur.execute(query_transaksi, (tgl_pengambilan, tgl_pengembalian, idcust, 1, idpembayaran))
                conn.commit()
                notransaksi = cur.fetchone()[0]

                query_detail_transaksi = "INSERT INTO detailtransaksi (transaksi_notransaksi, peralatan_noperalatan, statuspengembalian, denda) VALUES (%s,%s,%s,%s)"
                cur.execute(query_detail_transaksi, (notransaksi, pilih, 'Sewa', 0))
                conn.commit()
                
                time.sleep(2)
                            
                print("\n+==========================================================+")
                print("| Yeay booking selesai, ambil peralatan sesuai tanggal ya! |")
                print("+==========================================================+\n")

            else: 
                konfirmasi()

        konfirmasi()

def sedang_disewa():
    print("\n========= SEDANG BOOKING =========\n")
    query_booking = "SELECT peralatan.namaperalatan, transaksi.tglpengambilan,transaksi.tglpengembalian, detailtransaksi.statuspengembalian " \
                    "from detailtransaksi " \
                    "JOIN peralatan ON peralatan.noperalatan = detailtransaksi.peralatan_noperalatan " \
                    "JOIN jenisperalatan ON jenisperalatan.idjenis = peralatan.jenisperalatan_idjenis " \
                    "JOIN transaksi ON transaksi.notransaksi = detailtransaksi.transaksi_notransaksi " \
                    "JOIN customer ON customer.idcust = transaksi.customer_idcust " \
                    "WHERE customer.usernamecust = %s " \
                    "AND now() < transaksi.tglpengambilan "  

    cur.execute(query_booking, (user_login[0],))
    rows = cur.fetchall()

    headers = ["Nama peralatan", "Tanggal Pengambilan", "Tanggal Pengembalian", "Status"]
    print(tabulate(rows, headers=headers, tablefmt='pretty'))

    print("\n========= SEDANG DISEWA =========\n")
    query_sewa ="SELECT peralatan.namaperalatan, transaksi.tglpengambilan,transaksi.tglpengembalian, detailtransaksi.statuspengembalian " \
                "from detailtransaksi " \
                "JOIN peralatan ON peralatan.noperalatan = detailtransaksi.peralatan_noperalatan " \
                "JOIN jenisperalatan ON jenisperalatan.idjenis = peralatan.jenisperalatan_idjenis " \
                "JOIN transaksi ON transaksi.notransaksi = detailtransaksi.transaksi_notransaksi " \
                "JOIN customer ON customer.idcust = transaksi.customer_idcust " \
                "WHERE customer.usernamecust = %s" \
                "AND now() > transaksi.tglpengambilan AND now() < transaksi.tglpengembalian"  

    
    cur.execute(query_sewa, (user_login[0],))
    rows = cur.fetchall()

    headers = ["Nama peralatan", "Tanggal Pengambilan", "Tanggal Pengembalian", "Status"]
    print(tabulate(rows, headers=headers, tablefmt='pretty'))

    


def riwayat_peminjaman():
    query = "SELECT"


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
    delete = input("Kode peralatan yang ingin dihapus (b, untuk batal): ")
    query_cek = f"SELECT * FROM peralatan WHERE noperalatan = '{delete}'"
    cur.execute(query_cek)
    rows = cur.fetchone()

    if delete == 'b':
        time.sleep(2)
        kelola_peralatan()
    elif rows is None:
        print("\nKode peralatan tidak tersedia!")
        input("Tekan enter untuk mencoba lagi...")
        delete_peralatan()
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