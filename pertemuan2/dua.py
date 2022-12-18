# menghitung rata-rata (average)

# input untuk mengatur banyaknya angka
x = int(input('Masukan banyaknya angka = '))

# variabel untuk nilai 0 buat penjumlahan
total = 0

# for dengan parameter perulangan sebanyak variabel x, kemudian melakukan penjumlahan masing-masing inputan 
for i in range(x):
    a = int(input(' Masukan angka = '))
    total = float((total + a))

# meanmpilkan hasil penjumlahan kemudian dibagi banyannya jumlah bilangan 
print('Rata-rata =', total/x)