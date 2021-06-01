'''
Buatlah sebuah program buat memudahkan mengerjakan matematika dengan inputan user
1.buatlah sejumlah penjumlahan dengan rumus n+n-2+sampai n=0
2.mencari FPB 2 bilangan

Input:jumlah = penjumlahan (n);fpb_1 : inputan user angka ke-1 ;fpb_2 = inputan user angka ke-2

Proses:
membuat fungsi penjumlahan
melkukan percabangan
base case 
melakukan rekursif n+n-2
membuat fungsi FPB
base case b ==0
melakukan rekursif a % b

Output:
hasil penjumlahan,hasil FPB 2 bilangan tersebut

'''
def penjumlahan(angka):
  if angka <  1 :
    return 0 
  else :
    return angka + penjumlahan(angka-2)
def FPB(fpb_1,fpb_2):
  if fpb_2 == 0:
    return fpb_1
  else :
    hasil = fpb_1 % fpb_2
    return FPB(fpb_2,hasil)
jumlah = int(input('masukkan angka :'))
fpb_1 = int(input('masukkan angka ke-1 :'))
fpb_2 = int(input('masukkan angka ke-2 :'))
print('hasil penjumlahannya adalah :',penjumlahan(jumlah))
print('hasil FPB dari',fpb_1,'dan',fpb_2,'adalah :',FPB(fpb_1,fpb_1))


