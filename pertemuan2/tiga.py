# Mencetak persegi

# input untuk banyaknya sisi persegi
x = int(input('Masukan sebuah bilangan bulat = '))
print() #print untuk menambah baris baru seperi <br>

# for pertama untuk membuat perulangan secara vertikal
for i in range(x):
    # for kedua untuk membuat perulangan secara horizontal
    for k in range(x):
        # print ' #' untuk mengatur karakter dan menampilkan perulangan secara horizontal, end untuk mengatur akhiran supaya berbentuk persegi 
        print(' #',end='')
    print() # untuk menampilkan perulangan secara vertikal
print() #print untuk menambah baris baru seperi <br>