import psycopg2

conn = psycopg2.connect(database='Basda', user='postgres', password='iwanganteng', host='localhost', port=5432)
cur = conn.cursor()

def Option():
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
    for row in data:
        print(row)
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
    # cur.close() 
    # conn.close()

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



Option()