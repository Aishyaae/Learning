def Header(a):
    print(40*'=')
    print(a)
    print(40*'=')

def options (*a):
    while True:
        menu=f"{40*'='}\nopsi:"
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

    def recursive(self,current,dataa):
        if current.data > dataa:
            if current.left:
                self.recursive(current.left,dataa)
                return
            current.left=Node(dataa)
        elif current.data < dataa:
            if current.right:
                self.recursive(current.right,dataa)
                return
            current.right=Node(dataa)
    
    def search(self,curr,data,Route=""):
        if curr is None:
            print(f"{data} Tidak ditemukan")
        elif curr.data==data:
            print(f"{data} Ditemukan\n Rute: {Route} ")
            return curr
        elif curr.data>data:
            New_Route=Route + "L"
            return self.search(curr.left,data,New_Route)
        elif curr.data<data:
            New_Route=Route + "R"
            return self.search(curr.right,data,New_Route)
            
        

    def cut(self,data):
        print (f"Mencari {data}.....")
        location=self.search(self.root,data)
        if not location:
            return
        print (f"Menghapus {data}.....")
        self.root=self.DEL(self.root,data)

    def DEL(self,root,data):
        if root.data>data:
            root.left = self.DEL(root.left,data)
        elif root.data<data:
            root.right = self.DEL(root.right,data)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            succ=self.successor(root)
            root.data=succ.data
            root.right=self.DEL(root.right,succ.data)
        return root

    def successor(self,curr):
        curr=curr.right
        while curr.left:
            curr=curr.left
        return curr
            
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

    def Traversal(self):
        Header("Traversal")
        self.display()
        if self.root:
            print("Preorder:")
            self.Traversal_Preorder(self.root)
            print()
            print("Inorder:")
            self.Traversal_Inorder(self.root)
            print()
            print("Postorder:")
            self.Traversal_Postorder(self.root)
            print()
            input("(tekan Enter untuk kembali ke Menu Utama)")
        else:
            print("Data Kosong! Silahkan isi Data.")
            input("(tekan Enter untuk kembali ke Menu Utama)")

    def Traversal_Preorder(self,curr):
        if curr:
            print(curr,end=" ")
            self.Traversal_Preorder(curr.left)
            self.Traversal_Preorder(curr.right)

    def Traversal_Inorder(self,curr):
        if curr:
            self.Traversal_Inorder(curr.left)
            print(curr,end=" ")
            self.Traversal_Inorder(curr.right)

    def Traversal_Postorder(self,curr):
        if curr:
            self.Traversal_Postorder(curr.left)
            self.Traversal_Postorder(curr.right)
            print(curr,end=" ")

def main():
    print('\n||| Program Binary Seacrh Tree, by kelompok 5 |||')
    root=BST()
    while True:
        Header("Menu Utama")
        root.display()
        pilih = options("Tambah Data","Hapus Data","Traverse Tree","Search Data","Tutup Program")
        match pilih:
            case 1:
                Add(root)
            case 2:
                Del(root)
            case 3:
                root.Traversal()
            case 4:
                search(root)
            case 5:
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
            try:
                data=int(input(f"{i+1}/{n} > "))
                if not data=="":
                    break
                print("Input Kosong! Mohon masukan data untuk ditambah.")
            except ValueError:
                print("Invalid Input! Mohon masukan bilangan bulat")
            
            
        a.add(data)

def Del(root):
    Header("Hapus Data")
    if not root.root:
        print("Data Kosong! Silahkan isi Data.")
        input("(tekan Enter untuk kembali ke Menu Utama)")
        return
    
    data=int(input("Masukkan data yg ingin ditemukan dan hapuskan : "))
    root.cut(data)
    input("(tekan Enter untuk kembali ke Menu Utama)")
    
def search(root):
    Header("Search Data")
    if not root.root:
        print("Data Kosong! Silahkan isi Data.")
        input("(tekan Enter untuk kembali ke Menu Utama)")
        return
    data=int(input("Masukkan data yg ingin ditemukan: "))
    print (f"Mencari {data}.....")
    root.search(root.root,data)
    input("(tekan Enter untuk kembali ke Menu Utama)")


main()