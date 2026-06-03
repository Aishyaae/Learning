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
    def __init__(self,data):
        self.data =data
        self.left =None
        self.right =None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root =None

    def add(self,data):
        if not self.root:
            self.root =Node(data)
        else:
            self.recursive(self.root,data)

    def recursive(self,current,data):
        if current.data > data:
            if current.left:
                self.recursive(current.left,data)
                return
            current.left=Node(data)
        elif current.data < data:
            if current.right:
                self.recursive(current.right,data)
                return
            current.right=Node(data)
    
    def cut(self,data):
        pass
            
    def display(self):
        if not self.root:
            print("-")
        else:
            self.display_recursive(self.root,first=True)
    
    def display_recursive(self,current,prefix="",is_left=True,first=False):
        if first:
            print(current)
            new_prefix =""
        else:
            print(prefix +( "├── " if is_left else "└── ") + str(current))
            new_prefix = prefix + ("│   " if is_left else "    ")
        if current.left or current.right:
            if current.left:
                self.display_recursive(current.left, new_prefix, True)
            else:
                print(new_prefix + "├── None")
            if current.right:
                self.display_recursive(current.right, new_prefix, False)
            else:
                print(new_prefix + "└── None")
    
    def length(self):
        if not self.root:
            return 0
        current=self.root
        i=1
        while current:
            current=current.next
            i+=1
        return i


def main():
    print('\n||| Program Binary Seacrh Tree, by kelompok 5 |||')
    root=BST()
    while True:
        Header("Menu Utama")
        root.display()
        pilih = options("Tambah Data","Hapus Data","Tutup Program")
        match pilih:
            case 1:
                Add(root)
            case 2:
                Del(root)
            case 3:
                break
    print("Menutup Program...")
    
def Add(a):
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
            data=str(input(f"{i+1}/{n} > "))
            if not data=="":
                break
            print("Input Kosong! Mohon masukan data untuk ditambah.")
        a.add(data)

def Del(a):
    Header("Hapus Data")
    print("masukkan data yg ingin dihapuskan: ")


main()