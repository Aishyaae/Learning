def bubblesort_naik(data):
    for i in range(len(data)-1, -1, -1):
        tukar = False
        for j in range(i):
            if data[j] > data[j+1]:
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
                data[j], data[j+1] = data[j+1], data[j]
                tukar = True
        print(data)
        if not tukar:
            break

while True:
    print("Bubble Sort ni pilih dulu yuk sebelum mulai")
    print("1. Urutan Menaik(ascending)")
    print("2. Urutan Menurun(descending)")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan: ")
    if pilihan == "1" or pilihan == "2":
        masukan = input("Masukkan data: ")
        if " " in masukan:
            data = masukan.split()
        else:
            data = list(masukan)

        if pilihan == "1":
            bubblesort_naik(data)
            print("Data sudah terurut!")
        else:
            bubblesort_turun(data)
            print("Data sudah terurut!")
            
        while True:
            print("\n1. Data Selanjutnya")
            print("2. Kembali ke Menu Utama")
            print("3. Keluar")
            lanjut = input("Masukkan pilihan: ")
            if lanjut == "1":
                masukan = input("Masukkan data: ")
                if " " in masukan:
                    data = masukan.split()
                else:
                    data = list(masukan)
                if pilihan == "1":
                    bubblesort_naik(data)
                    print("Data sudah terurut!")
                else:
                    bubblesort_turun(data)                    
                    print("Data sudah terurut!")
            elif lanjut == "2":
                break
            elif lanjut == "3":
                print("Program selesai")
                exit()
            else:
                print("Pilihan tidak ada")
    elif pilihan == "3":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak ada")
