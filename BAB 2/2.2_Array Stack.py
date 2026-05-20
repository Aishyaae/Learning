print("=== PROGRAM TUMPUKAN BERBATAS ===")

def push():
    print("\nMasukkan data ke tumpukan (enter 2x untuk selesai): ")
    while True:
        data = input ("> ")
        if data == "":
            break
        
        tumpukan.append(data)

def pop():
    if tumpukan:
        terhapus = tumpukan.pop()
        print(f"'{terhapus}' telah dihapus dari tumpukan.")
    else:
        print("Tumpukan kosong. Tidak bisa menghapus data")

def stack():
    print("\nIsi tumpukan:")
    banyak = len(tumpukan)
    if not tumpukan:
        print("| Tumpukan kosong. Tidak ada yang bisa ditampilkan")
    else:
        for data in reversed(tumpukan[:kapasitas]):
            print(data)
        if banyak < kapasitas:
            print(f"| Terdapat {kapasitas-banyak} slot tersisa di tumpukan!")
        elif banyak == kapasitas:
            print("| Kapasitas tumpukan sudah penuh!")
        else:
            print(f"| Input melebihi kapasitas data! {banyak-kapasitas} data terakhir tidak bisa masuk.")
            tumpukan.pop()

def choice():
    print("\n0. Sudah selesai")
    print("1. Push data")
    print("2. Pop data")
    print ("Pilih langkah anda selanjutnya (0-2): ")


while True:
    print("\nMasukkan kapasitas tumpukan: ")
    kapasitas = int(input ("> "))
    tumpukan = []
    push()

    #OUTPUT STACK
    while True:
        stack()
        choice()
        pilihan = input("> ")
        if pilihan == "0":
            break
        elif pilihan == "1":
            push()
        elif pilihan == "2":
            pop()
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