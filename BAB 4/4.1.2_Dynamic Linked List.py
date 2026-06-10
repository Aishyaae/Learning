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

class Node:
    def __init__(self,data,Code):
        self.data = data
        self.code = Code
        self.next = None    

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,data,code):
        New_Link=Node(data,code)
        if not self.head:
            self.head=New_Link
            return
        Current=self.head
        while Current.next:
            Current=Current.next
        Current.next=New_Link
    
    def cut(self,index):
        current=self.head
        prev=None
        while index>1:
            prev = current
            current = current.next
            index -= 1
        if prev is None:
            self.head=current.next
        else:
            prev.next=current.next
            
    def display(self):
        print("Status Linked list:\nIndex\tData")
        if not self.head:
            print("-\t-")
        current=self.head
        i=1
        while current:
            print(f"{i}\t{current.data}")
            i+=1
            current=current.next
    
    def length(self):
        if not self.head:
            return 0
        current=self.head
        i=1
        while current.next:
            current=current.next
            i+=1
        return i

def main ():
    print('\n||| Program Linked List, by kelompok 5 |||')
    ll=LinkedList()
    code_list=[]
    while True:
        Header("Menu Utama")
        linear_display(ll)
        pilih = options("Link Baru","Hapus Link","Tutup Program")
        match pilih:
            case 1:
                New(ll,code_list)
            case 2:
                Del(ll,code_list)
            case 3:
                break
    print("Menutup Program...")

def linear_display(ll):
    print("Status Linked list:")
    if ll.head is None:
        print("-")
    current=ll.head
    i=1
    while current:
        if current.next is not None:
            print(f"{current.data} -> ",end="")
        else:
            print(f"{current.data}")
        i+=1
        current=current.next

def New(a,codes): # Adding Codes in progress
    Header("Tambah Data")
    while True:
        try:
            n=int(input("Banyak data baru yang akan ditambahkan: ")) 
            break
        except ValueError:
            print("Input TIDAK VALID! Coba masukan ulang.")
    print("masukkan data beserta code dari data yg ingin ditambahkan: ")
    for i in range(n):
        while True:
            data=str(input(f"Data {i+1}/{n}\t > "))
            if not data=="":
                while True:
                    code=str(input(f"Code dari data\t > "))
                    code=code.upper()
                    if len(code)>4:
                        print("Code tidak bisa lebih dari 5 karakter (contoh: KDQF)")
                    elif code in codes:
                        print("Masukan Code yang Unik. Berikut daftar Code yang sudah terpakai:\n", codes)
                    else:
                        break
                break
            print("Input Kosong! Mohon masukan data untuk ditambah.")
        a.add(data,code)


    
def Del(a,codes):
    Header("Hapus Data")
    batas=a.length()
    if batas==0:
        print("Linked List kosong. Silahkan tambahkan data.")
        return
    a.display()
    
    
    # while True: #GAK JADI. Niatnya supaya User dapat sekaligus hapus banyak. 
    #     try:
    #         n=int(input(f"Banyak data yang akan dihapuskan (1-{batas}): "))
    #         if 0<n<=batas:
    #             break
    #     except ValueError:
    #         print("Input tidak valid! Coba masukan ulang.")

    while True:
        try:
            index=int(input(f"Pilih Index Data yang akan dihapus (1-{batas}):\n> "))
            if 0<index<=batas:
                break
            print(f"Masukan Index yang tersedia (0-{batas}). Silahkan Coba lagi ")
        except ValueError:
            print("Input tidak valid! Coba masukan ulang.")
    a.cut(index)

main()

