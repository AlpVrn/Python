"""""
from tkinter import E


x=int(input("X ye sayı verin = "))
y=int(input("Y ye sayı verin = "))

if x>y:
    print('X Y den daha büyük')
elif x==y:
    print('Sayılar aynıdır')

else:
    print('Y X ten daha büyük')
    """

sayi=int(input("Sayı giriniz = "))
if sayi<0:
    print("Sayı negatiftir",sayi)
elif sayi==0:
    print('Sayı nötrdür ')
else:
    print("Sayı pozitiftir",sayi)