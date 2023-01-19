'''
Soru 4: Pozitif tam sayılar kümesinde kendisinden ve 1'den başka böleni olmayan sayılara asal sayılar denir. 
İlk on asal sayı 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 biçiminde sıralanır. 1. asal sayı 2, 10. asal sayı 29'dur.
10101. asal sayıyı bulan fonksiyonu yazınız.
'''

def asal(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def asal_listele(n):
    asal_liste = []
    for i in range(2, n+1):
        if asal(i):
            asal_liste.append(i)
    return asal_liste

asal_sayi_list = asal_listele(200000) # 200.000 sayıyı asal mı diye kontrol ettik ve asal olanları listeye aktardık
print(f"10101. asal sayı: {asal_sayi_list[10101]}") # bu listede 10101. asal sayının kaç olduğunu bulduk