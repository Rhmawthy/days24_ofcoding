#membuat list dalam list

data1= ["D",0,2,2,2]
data2= [0,3,3]

gab_list = [ data1,data2 ]
print (gab_list)

# membuat list dalam list ini biasa di gunakan ketika kita membuat data yang berseri

#contoh penggunaan dalam mebuat biodata mahasiswa
print ("peserta pertama")
mahasiswa_1 = input ("masukkan nama anda:"),input ("masukkan NIM:")

print ("peserta kedua")
mahasiswa_2 = input ("masukkan nama anda:"),input ("masukkan NIM:")

list_mahasiswa = [mahasiswa_1,mahasiswa_2]

for mahasiswa in list_mahasiswa:
    print("Nama\t:", mahasiswa[0])
    print("NIM\t:", mahasiswa[1],"\n")
    



