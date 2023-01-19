'''
Soru 1: Asal çarpanları sadece 2, 3 ya da 5'ten oluşan, 1 milyon'dan küçük
doğal sayıların toplamını bulan fonksiyon yazınız. Asal çarpanı 2, 3 yada 5 
olan sayılar: 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20 ...
'''

def asal_carpan_topla(n=1000000):
    toplam, i = 0, 0
    for i in range(n):
        if (i % 2 == 0) or (i % 3 == 0) or (i % 5 == 0):
            toplam+=i
    return toplam

print(asal_carpan_topla(1000000))