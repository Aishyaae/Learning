print("=== PROGRAM MEMBALIK STRING ===")

while True: 
    list_paragraf = []
    print("\nMasukkan kalimat anda (enter 2x untuk selesai): ")
    while True:
        teks = input ("> ")
        if teks == "":
            break
        
        list_paragraf.append(teks)

    #REVERSE STRING
    print("\n=== HASIL PEMBALIKAN STRING ===")

    if not list_paragraf:
        print("Anda tidak menginput apapun")
    else:
        for teks in list_paragraf:
            reverse = teks[::-1]
            print(reverse)
            print()

    while True:
        print("Apakah anda ingin lanjut (yes/no)")
        pilihan = input("> ").lower()
        if pilihan in ['yes', 'no']:
            break
        print('\nMohon input "yes" atau "no"')

    if pilihan == 'no':
        print("\nTerima kasih sudah menggunakan program ini!")
        break
