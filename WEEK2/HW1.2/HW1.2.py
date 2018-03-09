import random
s = 0
arr=[ None ]*100
temp=[ None ]*99
for i in range(1,100):
    arr[i]=i

arr[0]=random.randint(1,99)
print (arr)
random.shufle(arr)
for k in arr:
    c = temp[k-1]
    if c == None:
        temp[k-1]=1
    else:
        print ("Duplicate Sayı: ",k)