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
        print("Nilai terpilih :", nilai)

        while indeks > i:
            data[indeks] = data[indeks - 1]
            indeks -= 1

        data[i] = nilai

        print("Hasil :", data)

    return data


# ================= INPUT =================
input_user = input("Masukkan data campuran (pisahkan dengan spasi): ").split()

angka = []
teks = []

for item in input_user:
    try:
        if "." in item:
            angka.append(float(item))
        else:
            angka.append(int(item))
    except:
        teks.append(item)

print("\nData angka :", angka)
print("Data string :", teks)

# asc
angka_asc = selection_sort(angka, "asc")
teks_asc = selection_sort(teks, "asc")

print("\nHasil akhir Ascending :")
print(angka_asc + teks_asc)

# desc
angka_desc = selection_sort(angka, "desc")
teks_desc = selection_sort(teks, "desc")

print("\nHasil akhir Descending :")
print(angka_desc + teks_desc)

# menampilkan asc/desc
selection_sort(data, "asc")
selection_sort(data, "desc")

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
