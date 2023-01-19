'''
Soru 2: 5 milyondan küçük 3'e bölünebilen Fibonacci sayılarının toplamını
bulan fonksiyon yazınız.
'''

def fibonacci(n=5000000):
    fibArr = [0, 1]
    sayiToplam=0
    i = 2 
    while fibArr[i-1] < n:
        fibArr.append(fibArr[i-1] + fibArr[i-2])
        if fibArr[i] % 3 == 0:
            sayiToplam += fibArr[i]
        i+=1
    return sayiToplam

print(fibonacci(5000000))