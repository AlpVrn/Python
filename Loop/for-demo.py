sayilar=[1,3,5,7,9,12,19,21]
urunler=[ 
    {'name':'samsung S6','price':'3000'},
    {'name':'samsung S7','price':'4000'},
    {'name':'samsung S7','price':'5000'},
    {'name':'samsung S9','price':'6000'},
    {'name':'samsung S10','price':'7000'}
]

"""
SORU 1
toplam=[]
tek=[]
for say in sayilar:
    if say%3==0:
        tek+=[say]
    else:
        toplam+=[say]

print(toplam)
print(tek)

"""
#Soru2
"""
toplam=0
for say in sayilar:
    toplam+=say

print(toplam)
"""
#Soru 3
"""
sonuc=0
for say in sayilar:
    if say%2==1:
        print("Teklik xD : ",say**2)
    else:
        print("Tek olmayan sayı : ",say)


sehirler=['Kocaeli','istanbul','Ankara','İzmir','Rize']

for sehir in sehirler:
    if len(sehir)<=5:
        print(sehir)


SORU 5
toplam=0
urunler=[ 
    {'name':'samsung S6','price':'3000'},
    {'name':'samsung S7','price':'4000'},
    {'name':'samsung S7','price':'5000'},
    {'name':'samsung S9','price':'6000'},
    {'name':'samsung S10','price':'7000'}
]
for urun in urunler:
    fiyat = int(urun['price'])
    toplam+=fiyat

print(toplam)



fiyat=0
for urun in urunler:
    if int(urun['price'])<=5000:
        print(urun['name'])

"""

