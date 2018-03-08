import random
sayi1 = 0
sayi2 = 0
cikti = 0
arr = [None] * 100
for i in range(1, 100):
    arr[i] = i
    sayi1 = sayi1 + i

arr[0] = random.randint(1, 99)
print(arr)
toplam2 = sayi1 + arr[0]
sonuc = sayi2 - sayi1
print("\nDuplicate  : " + str(cikti))