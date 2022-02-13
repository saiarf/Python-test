class Buku:
    
    #Variable statics
    jumlah = 0

    #konstruktor
    def __init__(self, inputNama, inputPenerbit, inputJudul):
        self.nama= inputNama
        self.penerbit= inputPenerbit
        self.judul= inputJudul
        Buku.jumlah +=1

buku1=Buku("Buku pelajaran","Gramedia","Pemrograman dengan python") #object
buku2=Buku("Buku Remaja","Gramedia","Kreativitas")
buku3=Buku("Buku Novel","Gramedia","Negeri Para Bedebah")

print("tampilkan Informasi dari buku yang di beli= ", buku1.judul)
print(Buku.jumlah)

#print(buku2.__dict__)
#print(Buku.__dict__)