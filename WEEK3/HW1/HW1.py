def rvs(a):
    x = []
    for i in range(len(a)):
        x.append(a[i])
    for j in range(int(len(x) / 2)):
        x[j], x[len(x) - 1 - j] = x[len(x) - 1 - j], x[j]
    return x
var = input("YAZINIZI GİRİNİZ: ")
print(rvs(var))