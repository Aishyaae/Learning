data = []

while True:
    print("\n=== MENU ARRAYLIST ===")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Tampilkan Data Sesuai Abjad")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        isi = input("Masukkan data: ")
        data.append(isi)
        print("Data berhasil ditambahkan!")

    elif pilihan == "2":
        if len(data) == 0:
            print("ArrayList kosong!")
        else:
            print("Data saat ini:", data)

            hapus = input("Masukkan data yang ingin dihapus: ")

            if hapus in data:
                data.remove(hapus)
                print("Data berhasil dihapus!")
            else:
                print("Data tidak ditemukan!")

    elif pilihan == "3":
        if len(data) == 0:
            print("ArrayList kosong!")
        else:
            print("Data sesuai urutan input:")

            for i in range(len(data)):
                print(str(i + 1) + ". " + data[i])

    elif pilihan == "4":
        if len(data) == 0:
            print("ArrayList kosong!")
        else:
            urut = sorted(data)

            print("Data sesuai abjad:")

            for i in range(len(urut)):
                print(str(i + 1) + ". " + urut[i])

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")