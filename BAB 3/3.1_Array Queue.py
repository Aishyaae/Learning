from collections import deque
# Konsistensi design. 
def Header(a):
    print(10*'-')
    print(a)
    print(10*'-')

def options (*a):
    while True:
        menu="opsi:"
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
        except ValueError:
            print("Input tidak valid! Coba masukan ulang.")
    return pilihan

print('\n||| Program Array Queue, by kelompok 5 |||')
again = True
while again:
    Header("Pilih Jenis Queue")
    Jenis = options("Queue Berbatas","Queue Tidak Berbatas","Tutup Program")
    match Jenis:
        case 1:
            Code_Sakhinah()
        case 2:
            Code_Pasha()
        case 3:
            again=false
print("Menutup Program...")

def Code_Sakhinah():
    pass

def Code_Pasha():
    antrian=deque()
    while True:
        Header("Queue Tak Terbatas, by Pasha")
        print (f"Status Queue:\n")
        Jenis = options("Masukan Queue","Keluarkan Queue","Ganti Jenis Queue")
        match Jenis:
            case 1:
                tambah_tak_berbatas()
            case 2:
                keluar_tak_berbatas()
            case 3:
                break
        
def tambah_tak_berbatas():
    pass

def keluar_tak_berbatas():
    pass


