class Kotak:

    #Konstruktor
    def __init__(self, p, l, t):
        self.panjang= p
        self.lebar= l
        self.tinggi= t

    def cetakdata(self):
        print("panjang: ", self.panjang)
        print("lebar: ", self.lebar)
        print("tinggi: ", self.tinggi)

    def hitungvolume(self):
        return self.panjang * self.lebar * self.tinggi

    def tampilkanvolume(self):
        print("Volume: ", self.hitungvolume())

kotak1= Kotak(3,4,5)
kotak1.cetakdata()
kotak1.tampilkanvolume()