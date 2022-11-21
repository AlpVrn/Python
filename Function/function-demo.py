#1- Gönderilen bir kelimeyi belirtilen kez ekranda gösterşlen fonksiyonu gösteriniz
"""
from turtle import pen


def sorgu1(kelime,kez):
    sayac=0
    while sayac<kez:
        print(kelime)
        sayac+=1

print(sorgu1('Alp',4))
"""
#2 - Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız
"""def sinirsiz(*kelime):
    dizi=[]
    dizi+=kelime
    print(dizi)
print(sinirsiz(12,34,31,56,87,'ALp','Varna','ALp','Varna','ALp','Varna','ALp','Varna','AHAA','AHAA','AHAA'))
"""
#3 - gönderilen 2 sayı arasındaki asal sayıları bulun
"""
def AsalBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2 + 1):
        if sayi > 1:
            for i in range(2,sayi):
                if (sayi % i) == 0:
                    break
            else:
                print(sayi)

AsalBul(5,79)
"""
#4 - Kendisine gönnderilen bir sayının tam bölenlerini bir liste şekşinde döndürünüz

def bolenHesapla(sayi):
    liste=[]
    for i in range(1,sayi+1):
        if sayi% i == 0:
            liste.append(i)
    print(liste)

bolenHesapla(56)
        