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
    # was trying to make the sorted array different, let original array untouched. i can't
    sortd_data=[]
    style=0
    print('\n||| Program Insertion Sort, by kelompok 5 |||')
    while True:
        Header("Menu Utama")
        match style%2:
            case 0:
                display(data,sortd_data)
            case 1:
                display2(data,sortd_data)

        
        pilih = options("Tambah Data","Hapus Data","Sort (Menaik)","Sort (Menurun)","Sort (Keduanya)","ganti tampilan","Tutup Program")
        match pilih:
            case 1:
                Tambah(data)
            case 2:
                Hapus(data)
            case 3:
                data=AscSort(data)
            case 4:
                data=DesSort(data)
            case 5:
                data=AscSort(data)
                display(data)
                data=DesSort(data)
            case 6:
                style+=1
            case 7:
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
            angka=(input(f"{i+1}/{n} > "))
            angka=angka.strip()
            if not angka=="":
                try:
                    angka=int(angka)
                except ValueError:
                    try:
                        angka=float(angka)
                    except ValueError:
                        pass
                break
            print("Input Kosong! Mohon masukan angka untuk ditambah.")
            
        data.append(angka)

def Hapus(data):
    Header("Hapus Data")
    if not data:
        print("Data Kosong! Silahkan tambahkan data terlebih dahulu")
        input("(tekan Enter untuk kembali ke Menu Utama)")
        return
    while True:
        try:
            angka=(input("masukkan data yg ingin dihapuskan: "))
            angka=angka.strip()
            if not angka=="":
                break
            print("Input Kosong! Mohon masukan angka untuk ditambah.")
        except ValueError:
            print("Invalid Input! Mohon masukan bilangan bulat")
    not_found=True
    for i in range(len(data)):
        if data[i]==angka:
            print(f"{angka} ditemukan\nMenghapus....")
            data.pop(i)
            not_found=False
            break
    if not_found:print(f"{angka} tidak ditemukan")     
    input("(tekan Enter untuk kembali ke Menu Utama)")

def display(data,srt):
    if data:
        for i in range(len(data)):
            print(data[i],end=" ")
        print()
    else:
        print("-")
    if srt:
        print("Last Sorted:")
        for i in range(len(srt)):
            print(srt[i],end=" ")
        print()

def display2(data,srt): 
    if data:
        for i in range(len(data)):
            print(data[i],end=" > ")
        print()
    else:
        print("-")
    if srt:
        print("Last Sorted:")
        for i in range(len(srt)):
            print(srt[i],end=" ")
        print()

def AscSort(data):
    Header("Sorting Menaik...")
    if len(data)==0:
        print("Data Kosong! Silahkan tambahkan data terlebih dahulu")
        input("(tekan Enter untuk kembali ke Menu Utama)")
        return
    srt=data.copy()
    for i in range(1, len(srt)):
        for k in range(len(srt)):
            if k==i:print(end="| ")
            print(srt[k],end=" ")
        print()
        key = srt[i]
        print("data untuk di insert: ",key)
        j = i-1
        key_smaller=False
        try:
            if key < srt[j]:key_smaller=True
            else:key_smaller=False
        except TypeError:
            try:
                if isinstance(srt[j],str):key_smaller=False
                else:key_smaller=True
            except TypeError or ValueError:
                print("Debugging")

        while j >= 0 and key_smaller:
            try:
                if key < srt[j]:key_smaller=True
                else:key_smaller=False
            except TypeError:
                try:
                    if isinstance(srt[j],str):key_smaller=False
                    else:key_smaller=True
                except TypeError or ValueError:
                    print("Debugging")
            srt[j + 1] = srt[j]
            for k in range(len(srt)):
                print(srt[k],end=" ")
                if k==i:print(end="| ")
            print(f"\n{key} lebih kecil dari {srt[j]}. Menggeser {srt[j]}")
            j -= 1
        if j<0:print(f"\n{key} angka terkecil")
        else:print(f"\n{key} lebih besar dari {srt[j]}")
        srt[j + 1] = key
        for k in range(len(srt)):
            print(srt[k],end=" ")
            if k==i:print(end="| ")
        input("\n(tekan ENTER untuk lanjut ke tahap berikutnya)")
        print("|||||||")
    input("Sudah Selesai💜\n(tekan Enter untuk Lanjut)")
    return srt
   
def DesSort(data):
    Header("Sorting Menaik...")
    if len(data)==0:
        print("Data Kosong! Silahkan tambahkan data terlebih dahulu")
        input("(tekan Enter untuk kembali ke Menu Utama)")
        return
    srt=data.copy()
    for i in range(1, len(srt)):
        for k in range(len(srt)):
            if k==i:print(end="| ")
            print(srt[k],end=" ")
        print()
        key = srt[i]
        print("angka untuk di insert: ",key)
        j = i-1
        key_bigger=False
        try:
            if key > srt[j]:key_bigger=True
            else:key_bigger=False
        except TypeError:
            try:
                if isinstance(srt[j],str):key_bigger=True
                else:key_bigger=False
            except TypeError or ValueError:
                print("Debugging")
        while j >= 0 and key_bigger:
            try:
                if key > srt[j]:key_bigger=True
                else:key_bigger=False
            except TypeError:
                try:
                    if isinstance(srt[j],str):key_bigger=True
                    else:key_bigger=False
                except TypeError or ValueError:
                    print("Debugging")
            srt[j + 1] = srt[j]
            for k in range(len(srt)):
                print(srt[k],end=" ")
                if k==i:print(end="| ")
            print(f"\n{key} lebih besar dari {srt[j]}. Menggeser {srt[j]}")
            j -= 1
        if j<0:print(f"\n{key} angka terbesar")
        else:print(f"\n{key} lebih kecil dari {srt[j]}")
        srt[j + 1] = key
        for k in range(len(srt)):
            print(srt[k],end=" ")
            if k==i:print(end="| ")
        input("\n(tekan ENTER untuk lanjut ke tahap berikutnya)")
        print("|||||||")
    input("Sudah Selesai💜\n(tekan Enter untuk kembali ke Menu Utama)")
    return srt

main()