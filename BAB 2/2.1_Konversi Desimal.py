def konversi_biner(n):
    langkah = []
    hasil = ""
    if n == 0:
        return "0", ["0"]
    while n > 0:
        sisa = n % 2
        # print(f'{n} modulo 2 adalah{sisa}')
        langkah.append(f"{n} ÷ 2 = {n//2} sisa {sisa}")
        hasil = str(sisa) + hasil
        n = n // 2
    return hasil, langkah

def konversi_oktal(n):
    langkah = []
    hasil = ""
    if n == 0:
        return "0", ["0"]
    while n > 0:
        sisa = n % 8
        langkah.append(f"{n} ÷ 8 = {n//8} sisa {sisa}")
        hasil = str(sisa) + hasil
        n = n // 8
    return hasil, langkah

def konversi_heksa(n):
    punya_heksa = "0123456789ABCDEF"
    langkah = []
    hasil = ""
    if n == 0:
        return "0", ["0"]
    while n > 0:
        sisa = n % 16
        langkah.append(f"{n} ÷ 16 = {n//16} sisa {punya_heksa[sisa]}")
        hasil = punya_heksa[sisa] + hasil
        n = n // 16
    return hasil, langkah

while True:
    print("\n Pilih Mau Konversi Kemana ")
    print("1. Biner")
    print("2. Oktal")
    print("3. Heksadesimal")
    print("4. Semua Konversi")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "5":
        print("Program selesai")
        break
    angka = int(input("Masukkan angka desimal: "))

    if angka < 0:
        tanda = "-"
        angka = abs(angka)
    else:
        tanda = ""

    if pilihan == "1":
        hasil, langkah = konversi_biner(angka)
        hasil = tanda + hasil
        print("\nHasil :", hasil)
        print("\nPenjabaran:")
        for i in langkah:
            print(i)
            
    elif pilihan == "2":
        hasil, langkah = konversi_oktal(angka)
        hasil = tanda + hasil
        print("\nHasil :", hasil)
        print("\nPenjabaran:")
        for i in langkah:
            print(i)

    elif pilihan == "3":
        hasil, langkah = konversi_heksa(angka)
        hasil = tanda + hasil
        print("\nHasil :", hasil)
        print("\nPenjabaran:")
        for i in langkah:
            print(i)

    elif pilihan == "4":

        biner, langkah_biner = konversi_biner(angka)
        oktal, langkah_oktal = konversi_oktal(angka)
        heksa, langkah_heksa = konversi_heksa(angka)

        print("Hasil")
        print("Biner\t:", tanda + biner)
        print("Oktal\t:", tanda + oktal)
        print("Heksadesimal\t:", tanda +heksa)
        print("Penjabaran Biner")
        for i in langkah_biner:
            print(i)
        print("Penjabaran Oktal")
        for i in langkah_oktal:
            print(i)     
        print("Penjabaran Heksadesimal")
        for i in langkah_heksa:
            print(i)

    else:
        print("Pilihan tidak tersedia")