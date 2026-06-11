def Header(a):
    print(10*'=')
    print(a)
    print(10*'=')

def options (*a):
    while True:
        menu=f"{10*'='}\nopsi:"
        valid=[]
        i=1
        for argument in a:
            menu += f"\n{i}  {argument}"
            i+=1
        menu+=f"\npilihan(1-{i-1}): "
        try:
            pilihan=int(input(menu))
            if 0<pilihan<i:
                break
            print("Input TIDAK VALID! Coba masukan ulang.")
        except ValueError:
            print("Input TIDAK VALID! Coba masukan ulang.")
    return pilihan

def main():
    data=[]
    sortd_data=[]
    print('\n||| Program Insertion Sort, by kelompok 5 |||')
    while True:
        Header("Menu Utama")
        display(data,sortd_data)
        pilih = options("Tambah Data","Hapus Data","Sort (Urutkan)","Tutup Program")
        match pilih:
            case 1:
                Tambah(data)
            case 2:
                Hapus(data)
            case 3:
                AscSort(data,sortd_data)
            case 4:
                break
    print("Menutup Program...")

def Tambah(data):
    Header("Tambah Data")
    while True:
        try:
            n=int(input("Banyak data baru yang akan ditambahkan: ")) 
            break
        except ValueError:
            print("Input TIDAK VALID! Coba masukan ulang.")
    print("masukkan data yg ingin ditambahkan: ")
    for i in range(n):
        while True:
            try:
                angka=int(input(f"{i+1}/{n} > "))
                if not angka=="":
                    break
                print("Input Kosong! Mohon masukan angka untuk ditambah.")
            except ValueError:
                print("Invalid Input! Mohon masukan bilangan bulat")
        data.append(angka)

def Hapus(data):
    Header("Hapus Data")
    if not data:
        print("Data Kosong! Silahkan tambahkan data terlebih dahulu")
    while True:
        try:
            angka=int(input("masukkan data yg ingin ditambahkan: "))
            if not angka=="":
                break
            print("Input Kosong! Mohon masukan angka untuk ditambah.")
        except ValueError:
            print("Invalid Input! Mohon masukan bilangan bulat")
    
    for i in range(len(data)):
        if data[i]==angka:
            print(f"{angka} ditemukan\nMenghapus....")
            data.pop(i)
    print(f"{angka} tidak ditemukan")     

def display(data,srt):
    if data:
        for i in range(len(data)):
            print(data[i],end=" ")
        print()
    else:
        print("-")
    if srt:
        print("Sorted:")
        for i in range(len(srt)):
            print(srt[i],end=" ")
        print()
    
def AscSort(data,srt):
    Header("Sorting Menaik...")
    if len(data)==0:
        print("Data Kosong! Silahkan tambahkan data terlebih dahulu")
        return
    srt=data
    for i in range(1, len(srt)):
        for k in range(len(srt)):
            if k==i:print(end="| ")
            print(srt[k],end=" ")
        print()
        key = srt[i]
        print("angka untuk di insert: ",key)
        j = i-1
        while j >= 0 and key < srt[j]:
            srt[j + 1] = srt[j]
            for k in range(len(srt)):
                print(srt[k],end=" ")
                if k==i:print(end="| ")
            print(f"\n{key} lebih kecil dari {srt[j]}. Menggeser {srt[j]}")
            j -= 1
        if j<0:print(f"\n{key} angka terkecil")
        else:print(f"\n{key} akhirnya lebih besar dari {srt[j]}")
        srt[j + 1] = key
        for k in range(len(srt)):
            print(srt[k],end=" ")
            if k==i:print(end="| ")
        input("\n(tekan ENTER untuk lanjut ke tahap berikutnya)")
    input("(tekan Enter untuk kembali ke Menu Utama)")

main()