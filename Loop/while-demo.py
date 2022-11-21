import numbers


sayilar=[1,3,5,7,9,12,19,21]
"""SORU1
sayac=0

while sayac<len(sayilar):
    print(sayilar[sayac])
    sayac+=1
    """
"""SORU2
a=int(input("Başlangıç Saysısını Giriniz : "))
b=int(input("Bitiş Saysısını Giriniz : "))

while a<b:
    
    if(a%2==1):
        print(a)
    a+=1
    """
"""SORU3
sayi=100

while 0<sayi:
    print(sayi)
    sayi-=1
"""
"""
alinan=[]
sayac=0
while sayac<5:
    f=int(input('Sayı Girini'))
    alinan.append(f)
    sayac+=1

alinan.sort()
print(alinan)
"""

urunler=[]

adet=int(input('Kaç ürün eklemek istiyorsunuz'))

i=0

while i<adet:
    name = input('Ürün ismi ')
    price=input('Ürün fiyatı')
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1

for urun in urunler:
    print(f'Ürün Adı : {urun["name"]} ürün fiyatı : {urun["price"]}')


