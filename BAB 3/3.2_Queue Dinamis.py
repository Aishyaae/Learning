print("=== PROGRAM ANTREAN ===")

def add():
    print("\nMasukkan data ke antrean (enter 2x untuk selesai): ")
    while True:
        data = input ("> ")
        if data == "":
            break
        
        antrean.append(data)
 
def delete():
    print("\nMasukkan nama data yang ingin anda hapus: ")
    nama = input("> ")
    antrean.remove(nama)
    print(f"'{nama}' telah dihapus dari antrean.")

def queue():
    banyak = len(antrean)

    print("\nIsi antrean sesuai urutan input:")
    if not antrean:
        print("Antrean kosong")
    else:
        data_tampil = antrean[:kapasitas]
        print(" - ".join(data_tampil))
        # for data in (antrean[:kapasitas]):
        #     print(data)

    print("Isi antrean yang sudah diurutkan:")
    if not antrean:
        print("Antrean kosong")
    else:
        data_urut = sorted(antrean[:kapasitas])
        print(" - ".join(data_urut))
        # for data in sorted(antrean[:kapasitas]):
        #     print(data)

    if banyak < kapasitas:
        print(f"\nMasih ada {kapasitas-banyak} slot tersisa di antrean!")
    elif banyak == kapasitas:
        print("\nKapasitas antrean sudah penuh!")
    else:
        print(f"\nInput melebihi kapasitas data! {banyak-kapasitas} data terakhir tidak bisa masuk.")
        del antrean[kapasitas:]

def choice():
    print("\n0. Sudah selesai")
    print("1. Tambah data")
    print("2. Hapus data")
    print("3. Tampilkan data")
    print ("Pilih langkah anda selanjutnya (0-3): ")


while True:
    print("\nMasukkan kapasitas antrean: ")
    kapasitas = int(input ("> "))
    antrean = []
    add()

    #OUTPUT queue
    while True:
        choice()
        pilihan = input("> ")
        if pilihan == "0":
            break
        elif pilihan == "1":
            add()
        elif pilihan == "2":
            delete()
        elif pilihan == "3":
            queue()
        else:
            print("Pilihan gak valid. Coba lagi")

    while True:
        print("\nApakah anda ingin memulai program baru? (yes/no)")
        pilihan = input("> ").lower()
        if pilihan in ['yes', 'no']:
            break
        print('\nMohon input "yes" or "no"')

    if pilihan == 'no':
        print("\nTerima kasih sudah menggunakan program ini!")
        break