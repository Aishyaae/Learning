def Header(a):
    print(10*'=')
    print(a)
    print(10*'=')

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

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None    

class LinkedList:
    def __init__(self):
        self.head=None

    def add(self,data):
        New_Link=Node(data)
        if not self.head:
            self.head=New_Link
            return
        Current=self.head
        while Current:
            Current=Current.next
        Current.next=New_Link
    
    def cut(self,index):
        current=self.head
        prev=None
        while index>1:
            prev = current
            current = current.next
            index-=1
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
    
    def length(self):
        if not self.head:
            return 0
        current=self.head
        i=1
        while current:
            i+=1
        return i


def main ():
    print('\n||| Program Linked List, by kelompok 5 |||')
    head=LinkedList()
    while True:
        Header("Menu Utama")
        head.display()
        pilih = options("Link Baru","Hapus Link","Tutup Program")
        match pilih:
            case 1:
                New(head)
            case 2:
                Del(head)
            case 3:
                break
    print("Menutup Program...")

def New(a):
    Header("Tambah Data")
    n=int(input("Banyak data baru yang akan ditambahkan: ")) 
    print("masukkan data yg ingin ditambahkan: ")
    for i in n:
        a.add(str(input("> ")))
    
def Del(a):
    Header("Hapus Data")
    a.display()
    while True:
        batas=a.length()
        try:
            n=int(input(f"Banyak data yang akan dihapuskan (1-{batas}): "))
            if 0<n<=batas:
                break
        except ValueError:
            print("Input tidak valid! Coba masukan ulang.")
    
    for i in n:
        while True:
            try:
                a.cut(int(input))
            except ValueError:
                print("Input tidak valid! Coba masukan ulang.")

    
    





main()

