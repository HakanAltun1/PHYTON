while True:
    ilk = input("İLK: ")
    ilk = int(ilk) - 1
    iki = input("İLK: ")
    iki = int(iki)
    a = input("String: ")
    a2 = a[iki:]
    a = a[:ilk]
    print (a,a2)
