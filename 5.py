'''
Soru 5: Verilen listedeki None değerleri, kendinden önceki None olmayan değerle değiştirip
yeni bir liste oluşturan fonksiyon yazınız. 
Ör: Input: [3, None, 2, None, None, 1, False, None, 10] Output: [3, 3, 2, 2, 2, 1, False, False, 10]. 
Listenin None ile başlamayacağını varsayabilirsiniz.
'''

def none_degistir(liste):
    yeni_liste = []
    none_deger = None
    for deger in liste:
        if deger is not None:
            none_deger = deger
            yeni_liste.append(deger)
        else:
            yeni_liste.append(none_deger)
    print(yeni_liste)

none_degistir((3, None, 2, None, None, 1, False, None, 10))