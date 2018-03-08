a = []
x = input("ÇÖZÜLMESİNİ İSTEDİĞİNİZ KELİMEYİ GİRİNİZ : ")


my_str = x

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("GİRDİĞİNİZ KELİME POLİDROMDUR")

else:
    print("GİRDİĞİNİZ KELİME POLİDROM DEĞİLDİR")