'''
Soru 6: Verilen cümledeki kelimelerin ortalama uzunluğunu bulan fonksiyon yazınız.
",.!?:;" gibi noktalama işaretlerini kelime uzunluğuna dahil etmeyiniz.
ör: avg_len("Elma, portakal, armut") -> 5.66
'''

import string

def avg_len(*args):
    yeni_cumle = ""
    sayac, uzunluk_tpl = 0, 0
    for arg in args:
        for i in arg:
            if i not in string.punctuation:
                yeni_cumle += i
        cumle_list = yeni_cumle.split()

        for i in cumle_list:
            uzunluk_tpl+=len(i)
            sayac+=1

    print(uzunluk_tpl/sayac)

avg_len("Elma, Portakal, Armut")