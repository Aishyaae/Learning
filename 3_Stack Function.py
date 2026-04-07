print("=== PROGRAM TUMPUKAN ===")

while True:
    tumpukan = []
    print("\nMasukkan data ke tumpukan (enter 2x untuk selesai): ")
    while True:
        data = input ("> ")
        if data == "":
            break
        
        tumpukan.append(data)

    #OUTPUT STACK
    print("\nIsi tumpukan:")

    if not tumpukan:
        print("Tumpukan kosong")
    else:
        for data in reversed(tumpukan):
            print(data)

    while True:
        print("\nApakah anda ingin lanjut? (yes/no)")
        pilihan = input("> ").lower()
        if pilihan in ['yes', 'no']:
            break
        print('\nMohon input "yes" or "no"')

    if pilihan == 'no':
        print("\nTerima kasih sudah menggunakan program ini!")
        break

   #hal-hal yang patut dierhitungkan
   #1. apakah ingin menambahkan stack lama atau memulai stack baru saja
   #2. apakah boleh ada duplikasi data?
   #kalau sesuai ppt si gini doang, apakah harus lengkap dengan pop, peek, clear, remove dll dari fungsi stack?