import random

jumlah = int(input("Masukkan Jumlah N : "))

for i in range (jumlah) :
    print("Data ke-", i+1, " adalah ", (random.uniform(0.1, 0.5)))    