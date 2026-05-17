class Stack:
    def __init__(self):
        self.stack = []

    # Push (menambahkan data)
    def push(self, data):
        self.stack.append(data)
        print(f"{data} ditambahkan ke stack")

    # Pop (mengambil data)
    def pop(self):
        if self.is_empty():
            print("Stack kosong!")
        else:
            data = self.stack.pop()
            print(f"{data} dihapus dari stack")
            return data

    # Cek kosong
    def is_empty(self):
        return len(self.stack) == 0

    # Tampilkan isi stack
    def display(self):
        if self.is_empty():
            print("Stack kosong")
        else:
            print("Isi stack (dari bawah ke atas):")
            for item in self.stack:
                print(item)


# Program utama (dinamis)
s = Stack()

while True:
    print("\n=== MENU STACK ===")
    print("1. Push (Tambah data)")
    print("2. Pop (Ambil data)")
    print("3. Tampilkan stack")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        data = input("Masukkan data: ")
        s.push(data)

    elif pilihan == "2":
        s.pop()

    elif pilihan == "3":
        s.display()

    elif pilihan == "4":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid!")