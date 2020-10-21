print("-----Latihan Buku Telepon-----")
print("------------------------------")
f = open('Buku Telepon.txt','r+')
for line in f:
    print(line.rstrip())
f.close()
print('\n'+'Menu\n'+'1. Tambah Kontak\n'+'2. Edit\n'+'3. Hapus')
a = int(input('Pilih Nomor : '))
d = {}
f = open('Buku Telepon.txt','r+')
lines = f.readlines()
k = v = ''
for i in range(len(lines)):
    if i % 2 == 0:
        k = lines[i].rstrip()
    else:
        v = lines[i].rstrip()
    d[k] = v
f.close()
print(d)
if a == 1:
    print('Tambah Kontak')
    f = open('Buku Telepon.txt', 'a')
    b = input('Masukan Nama : ')
    f.write('\n'+b)
    c = input('Masukan Nomor Telepon : ')
    f.write('\n'+c)
    f.close()
    d[b]=c
    print(d)
elif a == 2:
    print('Edit')
    e = input('Nama kontak yang ingin diedit : ')
    f = input('Masukan nomor baru : ')
    d[e] = f
    f = open('Buku Telepon.txt', 'w')
    for i in d:
        f.write(i)
        f.write('\n')
        f.write(d[i])
        f.write('\n')
elif a == 3:
    print('Hapus Kontak')
    f = open('Buku Telepon.txt', 'w')
    e = input('Nama kontak yang ingin dihapus : ')
    del d[e]
    for i in d:
        f.write(i)
        f.write('\n')
        f.write(d[i])
        f.write('\n')
    f.close()
    print(d)