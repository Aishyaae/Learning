
def bubblesort(data):
    for i in range(len(data)-1,-1,-1):
        for j in range (i):
            if data[j] > data[j+1]:
                sementara = data[j]
                data[j]=data[j+1] 
                data[j+1]=sementara
        print(f"{data}")
data = list(input("Masukkan data: "))
bubblesort(data)

while True:
    print("\nBubble Sort")
    print("1. Data Selanjutnya")
    print("2. Keluar")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        data = list(input("Masukkan data: "))
        bubblesort(data)

    elif pilihan == "2":
        print("Program selesai")
        break

    else:
        print("Pilihan Tidak Ada")