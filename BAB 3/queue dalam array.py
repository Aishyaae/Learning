
n=int (input ("masukkan ukuran array:"))
queue=[0]*n

print("1.Enqueue")
print("2.dequeue")
print("3.Tampilkan Data")
print("4.Keluar Dari Program")

def enqueue():
    if queue.count(0)==0:
        print("queue overflow")
    else:
        top=int(input("masukkan data yg ingin ditambahkan:"))
        for i in range (0,n):
            if queue[i]==0:
                queue[i]=top
                break

def dequeue():
    if queue.count(0) == len(queue):
        print("queue underflow")
    else:
        for i in range(0,n):
            if queue[i] != 0:
                queue[i] = 0
                break

def display():
    for i in queue:
        if i!=0:
            print(i)

while True:
    pilihan=int(input("masukkan pilihan:"))
    if pilihan == 1:
        enqueue()
    elif pilihan == 2:
        dequeue()
    elif pilihan == 3:
        display()
    elif pilihan == 4:
        print("Keluar")
        break
    else:
        print("invalid number")

