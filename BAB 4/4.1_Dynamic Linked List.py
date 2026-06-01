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

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None    

def main ():
    print('\n||| Program Linked List, by kelompok 5 |||')
    again = True
    head = None
    link_id=1
    while again:
        Header("Menu Utama")
        Show(head)
        pilih = options("Link Baru","Hapus Link","Tutup Program")
        match pilih:
            case 1:
                New(link_id,head)
                link_id+=1
            case 2:
                Cut()
            case 3:
                break
    print("Menutup Program...")

def Show (a):
    current = a
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print ("None")

def New(a,b):
    Header("New Link")
    data = str(input("masukkan data yg ingin ditambahkan: "))
    globals()[a + '_link'] = Node(data)
    while b:
        print("test")


def Cut ():
    pass 


main()


# AGH SALAH JALAN. BIKIN FILE BARU AJA