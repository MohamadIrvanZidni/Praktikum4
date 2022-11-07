# Praktikum4
Repository ini digunakan untuk memenuhi Tugas Bahasa Pemrograman Pertemuan-7

Nama    : Mohamad Irvan Zidni

NIM     : 312210308

Kelas   : TI.22.A.3

| No | Daftar Isi | Link |
| -- | ---------- | ---- |
| 1 | Praktikum 2 | [Click Here](https://github.com/MohamadIrvanZidni/Praktikum4/blob/main/README.md#praktikum-2) |
| 2 | Praktikum 3 | [Click Here](https://github.com/MohamadIrvanZidni/Praktikum4/blob/main/README.md#praktikum-3) |
| 3 | Kondisional & Perulangan | [Click Here](https://github.com/MohamadIrvanZidni/Praktikum4/blob/main/README.md#kondisional-dan-perulangan) |

# Praktikum 2
## Tugas Praktikum
Program untuk menampilkan bilangan terbesar dari 3 bilangan
Code :

![Code](Foto/Code_Praktikum2.png)

    a = int(input("Bilangan Ke-1 : "))
    b = int(input("Bilangan Ke-2 : "))
    c = int(input("Bilangan Ke-3 : "))

    if a>b and a>c :
        print("Bilangan Terbesar Adalah : ", a)
    elif b>a and b>c :
        print("Bilangan Terbesar Adalah : ", b)
    else :
        print("Bilangan Terbesar Adalah : ", c)
Output :

![Output](Foto/Output_Praktikum2.png)

# Praktikum 3
## Latihan 1
Program untuk menampilkan n bilangan acak yang lebih kecil dari 0.5
Code :

![Code](Foto/Code_Latihan1_Praktikum3.png)

    import random

    jumlah = int(input("Masukkan Jumlah N : "))

    for i in range (jumlah) :
        print("Data ke-", i+1, " adalah ", (random.uniform(0.1, 0.5)))    
Output :

![Output](Foto/Output_Latihan1_Praktikum3.png)

## Latihan 2
Program untuk menampilkan bilangan terbesar dari n buah data yang di inputkan

## Tugas Praktikum
Program untuk menghitung jumlah laba hasil investasi seorang pengusaha selama 8 bulan

# Kondisional dan Perulangan
## Kondisional
### Latihan 1
Program untuk menampilkan bilangan terbesar dari 2 bilangan
### Latihan 2
Program untuk mengurutkan data berdasarkan input sejumlah data
## Perulangan
### Latihan 1
Program perulangan bertingkat (nested)
### Latihan 2
Program untuk menampilkan n bilangan acak yang lebih kecil dari 0.5
