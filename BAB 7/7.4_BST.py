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
    # Add new data
    def add(self,data):
        if not self.root:
            self.root =Node(data)
        else:
            self.add_recursive(self.root,data)
    def add_recursive(self,current,new_data):
        if current.data > new_data:
            if current.left:
                self.add_recursive(current.left,new_data)
                return
            current.left=Node(new_data)
        elif current.data < new_data:
            if current.right:
                self.add_recursive(current.right,new_data)
                return
            current.right=Node(new_data)
    # Search 
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
    # Delete
    def cut(self,data):
        print (f"Mencari {data}.....")
        location=self.search(self.root,data)
        if not location:
            return
        print (f"Menghapus {data}.....")
        self.root=self.cut_recursive(self.root,data)
    # note to self, we forgor how this cut_recursion works. thx past us for making this.
    def cut_recursive(self,root,target_data):
        if root.data>target_data:
            root.left = self.cut_recursive(root.left,target_data)
        elif root.data<target_data:
            root.right = self.cut_recursive(root.right,target_data)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            succ=self.successor(root)
            root.data=succ.data
            root.right=self.cut_recursive(root.right,succ.data)
        return root

    def successor(self,curr):
        curr=curr.right
        while curr.left:
            curr=curr.left
        return curr
    # The Displays    
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
    
    def display2(self):
        if not self.root:
            print("-")
        else:
            self.display2_recursive(self.root,first=True)
    def display2_recursive(self,current,prefix="",is_left=True,first=False):
        if not self.root:
            print("-")
        else:
            show=self.tree_to_matrix(self.root)
            self.print_2d_array(show)
    def find_height_for_display2(self,root):
        if not root:
            return -1

        left_height = self.find_height_for_display2(root.left)
        right_height = self.find_height_for_display2(root.right)

        return max(left_height, right_height) + 1 
    def inorder_for_diplay2(self,root, row, col, height, ans):
        if not root:
            return
        offset = 2 ** (height - row - 1)
        if root.left:
            self.inorder_for_diplay2(root.left, row + 1, col - offset, 
                    height, ans)
        ans[row][col] = str(root.data)
        if root.right:
            self.inorder_for_diplay2(root.right, row + 1, col + offset, 
                    height, ans)
    def tree_to_matrix(self,root):    
        height = self.find_height_for_display2(root)
        rows = height + 1
        cols = 2 ** (height + 1) - 1
        ans = [["" for _ in range(cols)] for _ in range(rows)]
        self.inorder_for_diplay2(root, 0, (cols - 1) // 2, height, ans)
        return ans
    def print_2d_array(arr):
        for row in arr:
            for cell in row:
                if cell == "":
                    print(" ", end="")
                else:
                    print(cell, end="")
            print()

    # The Traversals
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
    Style=0
    while True:
        Header("Menu Utama")
        match Style%2:
            case 0:
                root.display()
            case 1:
                root.display2()
        
        pilih = options("Tambah Data","Hapus Data","Traverse Tree","Search Data","Ganti Display","Tutup Program")
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
                Style+=1
            case 6:
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
    
    while True:
        data=int(input("Masukkan data yg ingin ditemukan dan hapuskan : "))
        input("(Biarkan input kosong untuk kembali ke Menu Utama)")
        if data=="":
            return
        root.cut(data)
    
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
# "Take a deep breath but they couldn't"