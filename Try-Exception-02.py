#Percobaan-04 (Value Error dan Zero Division Error
print("Program Pembagian")
while True:
    try:
        penyebut = int(input("Masukan angka penyebut: "))
        pembilang = int(input("Masukan angka pembilang: "))
        hasil = penyebut/pembilang
        break
    except ValueError:
        print("yang anda masukan bukan angka\n")
    except ZeroDivisionError:
        print("Mohon masukan angka selain angka Nol \n")

print("Berhasil, Hasilnya adalah: ",hasil)
print(50*"=")

#Percobaan-05 (Bentuk umum dari Value Error dan Zero Division Error)
print("Program Pembagian")
while True:
    try:
        penyebut = int(input("Masukan angka penyebut: "))
        pembilang = int(input("Masukan angka pembilang: "))
        hasil = penyebut/pembilang
        break
    except Exception as err:
        print(err)

print("Berhasil, Hasilnya adalah: ",hasil)
print(50*"=")