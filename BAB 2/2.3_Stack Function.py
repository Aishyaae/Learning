# Stack sederhana

class Stack:
    def __init__(self):
        self.data = []

    def tambah(self, isi):
        self.data.append(isi)
        print("Data ditambahkan")

    def hapus(self):
        if self.data == []:
            print("Stack kosong")
        else:
            keluar = self.data.pop()
            print(keluar, "dihapus")

    def tampil(self):
        if self.data == []:
            print("Stack kosong")
        else:
            print("Isi Stack:")
            for i in reversed(self.data):
                print(i)

stack = Stack()

while True:
    print("\n=== MENU ===")
    print("1. Tambah data")
    print("2. Hapus data")
    print("3. Tampilkan stack")
    print("4. Keluar")

    pilih = input("Pilih menu: ")

    if pilih == "1":
        data = input("Masukkan data: ")
        stack.tambah(data)

    elif pilih == "2":
        stack.hapus()

    elif pilih == "3":
        stack.tampil()

    elif pilih == "4":
        print("Program selesai")
        break

    else:
        print("Pilihan salah")