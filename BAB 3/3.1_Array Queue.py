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
        except ValueError:
            print("\nInput tidak valid! Coba masukan ulang.\n")
        if 0<pilihan<i:
            break
        else:
            print("\nInput tidak valid! Coba masukan ulang.\n")
    return pilihan

# Layer 1
def main():
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
                again=False
    print("Menutup Program...")

# layer 2
def Code_Sakhinah():
    n=int (input ("masukkan ukuran array: "))
    queue =[0]*n
    while True:
        Header("Queue Terbatas, by Sakinah")
        display(queue)
        Jenis = options("Enqueue","dequeue","Ganti Jenis Queue","Kembali")
        match Jenis:
            case 1:
                enqueue(n,queue)
            case 2:
                dequeue(n,queue)
            case 3:
                Code_Pasha()
                break
            case 4:
                q=False
                break

def enqueue(n,queue):
    if queue.count(0)==0:
        print("queue overflow")
    else:
        top=int(input("masukkan data yg ingin ditambahkan: "))
        for i in range (0,n):
            if queue[i]==0:
                queue[i]=top
                break

def dequeue(n,queue):
    if queue.count(0) == len(queue):
        print("queue underflow")
    else:
        for i in range(0,n):
            if queue[i] != 0:
                queue[i] = 0
                break

def display(queue):
    print("status queue: ")
    for i in queue:
        if i!=0:
            print(i)




def Code_Pasha():
    antrian=deque()
    while True:
        Header("Queue Tak Terbatas, by Pasha")
        print (status(antrian))
        Jenis = options("Masukan data ke Queue","Keluarkan data dari Queue","Ganti Jenis Queue","Kembali")
        match Jenis:
            case 1:
                tambah_tak_berbatas(antrian)
            case 2:
                keluar_tak_berbatas(antrian)
            case 3:
                Code_Sakhinah()
                break
            case 4:
                break
        
def tambah_tak_berbatas(a):
    Header("Menambah Data")
    while True:
        try:
            n=int(input("Banyak Data untuk dimasukan: "))
            break
        except ValueError:
            print("\nInput tidak valid! Coba masukan ulang.\n")
    for i in range(n):
        while True:
            data=str(input(f"{i+1}/{n}: "))
            if data!="":
                break
            print ("Mohon Masukan data🙏🏻")
        a.append(data)

def keluar_tak_berbatas(a):
    if len(a)==0:
        print("Underflow (Queue Kosong)")
        return
    Header("Mengurangi Data")
    n=int(input(f"Banyak Data Tersedia: {len(a)}\nBanyak Data untuk dikeluarkan: "))
    for i in range(n):
        print(f"{i}/{n} Data terhapus: ",a.popleft())

def status(a):
    teks="Status:"
    j=0
    for i in a:
        teks += f"\n{j+1}/{len(a)}  {a[j]}"
        j+=1
    print(teks)


main()