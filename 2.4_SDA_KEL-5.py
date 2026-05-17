def Header(a):
    print(10*'-')
    print(a)
    print(10*'-')


def reverse (a):
    rev=""
    for i in range(len(a)):
        rev += a[len(a)-i-1]
        print(rev)
    return rev
       
def options (*a):
    while True:
        menu="opsi:"
        valid=[]
        i=1
        for argument in a:
            menu += f"\n{i}  {argument}"
            i+=1
        menu+=f"\npilihan(1-{i-1}): "
        try
        pilihan=int(input(menu))
        if 
    return pilihan

def case1():
    Header("Balik kalimat")
    Text=str(input("Masukan Kalimat untuk dibalik:\n"))
    terbalik=reverse(Text)
    return Text,terbalik

def case2():
    pass

def case3():
    pass
     

print('\n||| Program Pembalik String, by kelompok 5 |||')
again = True
while again:
    Header("Menu Utama")
    Choice = options("Balik kalimat","Balik Paragraf per baris","Balik Seluruh Paragraf")
    match Choice:
        case 1:
            before,after=case1()
        case 2:
            before,after=case2()
        case 3:
            before,after=case3()

    Header("Hasil Pembalikan")
    print(f"Sebelum:\n{before}\nSesudah:\n{after}")

    if 2==options("Jalankan Ulang Program","Tutup Program"):
        again=False
print("Menutup Program...")