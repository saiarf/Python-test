data_mahasiswa1 = {'ID':5008,"Nama":"A","Prodi":"TI","Kelas":"2A"}
data_mahasiswa2 = {'ID':5121,"Nama":"B","Prodi":"TI","Kelas":"2B"}
data_mahasiswa3 = {'ID':5135,"Nama":"C","Prodi":"TI","Kelas":"2C"}

print(data_mahasiswa1["Nama"])
print(data_mahasiswa2.keys())
print(data_mahasiswa3.values())
print(data_mahasiswa2.items())
print(130*'=')

datalis = {5008:data_mahasiswa1,5121:data_mahasiswa2,5135:data_mahasiswa3}
print(datalis[5121])
print(datalis[5008])
print(datalis[5135])