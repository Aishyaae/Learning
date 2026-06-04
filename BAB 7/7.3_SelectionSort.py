def selection_sort(data):
    n = len(data)

    print("Data awal :", data)

    for i in range(n - 1):
        indeks_min = i

        for j in range(i + 1, n):
            if data[j] < data[indeks_min]:
                indeks_min = j

        print(f"\nLangkah {i+1}")
        print(f"Nilai terkecil ditemukan: {data[indeks_min]}")
        print(f"Tukar {data[i]} dengan {data[indeks_min]}")

        data[i], data[indeks_min] = data[indeks_min], data[i]

        print("Hasil:", data)

    print("\nData setelah diurutkan :", data)

angka = list(map(int, input("Masukkan angka (pisahkan dengan spasi): ").split()))

selection_sort(angka)