def konversi(n, basis):
    simbol_heksa = "0123456789ABCDEF"
    langkah = []
    bagian_bulat = int(n)
    bagian_pecahan = n - bagian_bulat
    hasil_bulat = ""
    if bagian_bulat == 0:
        hasil_bulat = "0"
    while bagian_bulat > 0:
        sisa = bagian_bulat % basis
        langkah.append (f"{bagian_bulat} ÷ {basis} = {bagian_bulat//basis} sisa {simbol_heksa[sisa]}")
        hasil_bulat = simbol_heksa[sisa] + hasil_bulat
        bagian_bulat = bagian_bulat // basis
        
    hasil_pecahan = ""
    if bagian_pecahan > 0:
        langkah.append("\nKonversi Pecahan")
        for i in range(10):
            bagian_pecahan = bagian_pecahan * basis
            digit = int(bagian_pecahan)
            langkah.append(f"{bagian_pecahan/basis} x {basis} = {bagian_pecahan}")
            hasil_pecahan += simbol_heksa[digit]
            bagian_pecahan = bagian_pecahan - digit
            if bagian_pecahan == 0:
                break
    if hasil_pecahan != "":
        hasil = hasil_bulat + "." + hasil_pecahan
    else:
        hasil = hasil_bulat
    return hasil, langkah

while True:
    print("\nMau Konversi Kemana")
    print("1. Biner")
    print("2. Oktal")
    print("3. Heksadesimal")
    print("4. Semua")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "5":
        print("Program selesai")
        break
    angka = float(input("Masukkan angka desimal: "))
    if angka < 0:
        tanda = "-"
        angka = abs(angka)
    else:
        tanda = ""
        
    if pilihan == "1":
        hasil, langkah = konversi(angka, 2)
        print("\nHasil Biner :", tanda + hasil)
        print("\nPenjabaran:")
        for i in langkah:
            print(i)

    elif pilihan == "2":
        hasil, langkah = konversi(angka, 8)
        print("\nHasil Oktal :", tanda + hasil)
        print("\nPenjabaran:")
        for i in langkah:
            print(i)

    elif pilihan == "3":
        hasil, langkah = konversi(angka, 16)
        print("\nHasil Heksadesimal :", tanda + hasil)
        print("\nPenjabaran:")
        for i in langkah:
            print(i)

    elif pilihan == "4":
        biner, langkah_biner = konversi(angka, 2)
        oktal, langkah_oktal = konversi(angka, 8)
        heksa, langkah_heksa = konversi(angka, 16)

        print("\nPenjabarannya Biner")
        for i in langkah_biner:
            print(i)

        print("\nPenjabarannya Oktal")
        for i in langkah_oktal:
            print(i)

        print("\nPenjabarannya Heksa")
        for i in langkah_heksa:
            print(i)

        print("\nHasil")
        print("Biner         :", tanda + biner)
        print("Oktal         :", tanda + oktal)
        print("Heksadesimal  :", tanda + heksa)

    else:
        print("Pilihan tidak tersedia")