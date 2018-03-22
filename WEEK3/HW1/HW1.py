def rvs(yazi):

    x = len(yazi)
    dizi = []

    for i in range(x):
        x = x - 1
        dizi.extend(yazi[x])

    dizi = ''.join(dizi)
    return dizi

klm = input("Giriniz ")
print(rvs(klm))