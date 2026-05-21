print("=== PROGRAM ANTREAN DENGAN KAPASITAS===")

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

def queue_input():
    print("\nIsi antrean sesuai urutan input:")
    if not antrean:
        print("Antrean kosong")
    else:
        nomor = 1
        for i in antrean[:kapasitas]:
            print(f"{nomor}.{i}")
            nomor += 1

def queue_abjad():
    print("\nIsi antrean yang sudah diurutkan:")
    if not antrean:
        print("Antrean kosong")
    else:
        nomor = 1
        for i in sorted(antrean[:kapasitas]):
            print(f"{nomor}. {i}")
            nomor += 1

def kondisi():
    banyak = len(antrean)
    
    if banyak < kapasitas:
        print(f"|| Masih ada {kapasitas-banyak} slot tersisa di antrean!")
    elif banyak == kapasitas:
        print("|| Kapasitas antrean sudah penuh!")
    else:
        print(f"|| Input melebihi kapasitas data! {banyak-kapasitas} data terakhir tidak bisa masuk.")
        del antrean[kapasitas:]

def choice():
    print("\n0. Sudah selesai")
    print("1. Tambah data")
    print("2. Hapus data")
    print("3. Tampilkan data (urutan input)")
    print("4. Tampilkan data (urutan abjad)")
    print ("Pilih langkah anda selanjutnya (0-4): ")


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
            queue_input()
            kondisi()
        elif pilihan == "4":
            queue_abjad()
            kondisi()
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