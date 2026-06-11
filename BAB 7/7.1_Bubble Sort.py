def bubblesort_naik(data):
    for i in range(len(data)-1, -1, -1):
        tukar = False
        for j in range(i):
            if data[j] > data[j+1]:
                print(f"Tukar {data[j]} dengan {data[j+1]}")
                data[j], data[j+1] = data[j+1], data[j]
                tukar = True
                print(data)
        if not tukar:
            break


def bubblesort_turun(data):
    for i in range(len(data)-1, -1, -1):
        tukar = False
        for j in range(i):
            if data[j] < data[j+1]:
                print(f"Tukar {data[j]} dengan {data[j+1]}")
                data[j], data[j+1] = data[j+1], data[j]
                tukar = True
                print(data)
        if not tukar:
            break


data = []

while True:
    print("BUBBLE SORT")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Menaik(Ascending)")
    print("4. Menurun(Descending)")
    print("5. Tampilkan Menaik & Menurun")
    print("6. Tampilkan Data")
    print("7. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        angka = float(input("Masukkan data: "))
        if angka.is_integer():
            angka = int(angka)
        data.append(angka)
        print("Data:", data)

    elif pilihan == "2":
        print("Data:", data)
        hapus = float(input("Hapus data: "))
        if hapus.is_integer():
            hapus = int(hapus)
        if hapus in data:
            data.remove(hapus)
            print("Data:", data)
        else:
            print("Data tidak ditemukan")

    elif pilihan == "3":
        print("Proses Bubble Sort Menaik:")
        bubblesort_naik(data.copy())
        print("Data sudah terurut!")

    elif pilihan == "4":
        print("Proses Bubble Sort Menurun:")
        bubblesort_turun(data.copy())
        print("Data sudah terurut!")

    elif pilihan == "5":
        print("Proses Bubble Sort Menaik:")
        bubblesort_naik(data.copy())

        print("\nProses Bubble Sort Menurun:")
        bubblesort_turun(data.copy())

    elif pilihan == "6":
        print("Data saat ini:", data)

    elif pilihan == "7":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")
