def selection_sort(data, order="asc"):
    data = data.copy()
    n = len(data)

    print(f"\n=== Pengurutan {'Ascending' if order == 'asc' else 'Descending'} ===")
    print("Data awal :", data)

    for i in range(n - 1):
        indeks = i

        for j in range(i + 1, n):
            if order == "asc":
                if data[j] < data[indeks]:
                    indeks = j
            else:
                if data[j] > data[indeks]:
                    indeks = j

        nilai = data[indeks]

        print(f"\nLangkah {i+1}")
        print(f"Nilai {'terkecil' if order == 'asc' else 'terbesar'} = {nilai}")

        while indeks > i:
            data[indeks] = data[indeks - 1]
            indeks -= 1

        data[i] = nilai

        print("Hasil :", data)

    print(f"\nData setelah diurutkan ({'Ascending' if order == 'asc' else 'Descending'}):", data)


# ================= MENU TIPE DATA =================
print("Pilih tipe data:")
print("1. Integer")
print("2. Float")
print("3. String")

pilihan = input("Masukkan pilihan (1/2/3): ")

if pilihan == "1":
    data = list(map(int, input("Masukkan data integer (pisahkan dengan spasi): ").split()))

elif pilihan == "2":
    data = list(map(float, input("Masukkan data float (pisahkan dengan spasi): ").split()))

elif pilihan == "3":
    data = input("Masukkan data string (pisahkan dengan spasi): ").split()

else:
    print("Pilihan tidak valid!")
    exit()

# menampilkan asc/desc
selection_sort(data, "asc")
selection_sort(data, "desc")