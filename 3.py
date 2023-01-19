'''
Soru 3: Baştan ve sonran yazıldığında değişmeyen sayılara palindrom sayılar denir.
Ör: 1001, 23432. 2 haneli sayıların çarpımından elde edilen en büyük palindrom 
sayısı 91 * 99 = 9009'dur. 3 haneli sayıların çarpımından elde edilen en büyük
palindrom sayısını bulan fonksiyonu yazınız.
'''

def palindrom():
    en_buyuk_palindrome = 0
    en_kucuk = 100
    en_buyuk = 999
    for i in range(en_buyuk, en_kucuk, -1):
        for j in range(i, en_kucuk, -1):
            carpim = i * j
            if carpim < en_buyuk_palindrome:
                break
            elif str(carpim) == str(carpim)[::-1]:
                en_buyuk_palindrome = carpim
    return en_buyuk_palindrome

print(palindrom())