"""
Percobaan-01

try:
    a = 1/0
except:
    print("Error Pembagi Nol")

print("akhir dari program")
print(50*'=')"""

#Percobaan-02
while True:
    try:
        angka = int(input("Masukan Angka: "))
        break
    except:
        print("yang anda masukan bukan angka")

print("Berhasil, Angka yang anda masukan adalah: ",angka)
print(50*"=")

"""#Percobaan-03
print("Program Pembagian")
while True:
    try:
        penyebut = int(input("Masukan angka penyebut: "))
        pembilang = int(input("Masukan angka pembilang: "))
        hasil = penyebut/pembilang
        break
    except:
        print("yang anda masukan bukan angka")

print("Berhasil, Hasilnya adalah: ",hasil)
print(50*"=")"""