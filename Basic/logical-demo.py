#1
#a=int(input("Bir sayı giriniz"))
#print(a>0 and a<100)


#a=int(input("Bir sayı giriniz"))
#print(a%2==0 and a>0)

"""""
email='A'
password='sifre'

Semail=str(input("E postanızı giriniz"))
Spassword=str(input("Şifrenizi giriniz"))

print(email==Semail and password==Spassword)

"""
"""""
from unittest import result


a=int(input('A: '))
b=int(input("b: "))
c=int(input("c: "))

result=(a>b)and (a>c)
print("A sayısı daha büyüktür =",{result})
result=(b>a)and (b>c)
print("B sayısı daha büyüktür =",{result})

result=(c>b)and (c>a)
print("c sayısı daha büyüktür =",{result})
"""
"""""
from tokenize import Double


vize1=float(input('Bir vize giriniz : '))
vize2=float(input('ikinci vizeyi giriniz'))
final=float(input('finali giriniz'))

sonuc=(((vize1+vize2)/2)*0.6+(final*0.4))
if(sonuc<50 and final<=50):
    print("Geçemedin",sonuc)

elif(sonuc>50 or final>70):
    print('Geçtin!',sonuc)
"""
"""""HATALI
from turtle import numinput


ad=input("adınızı giriniz")
kg=float(input('Kilonuzu Giriniz : ')) 
hg=float(input('Boyunuzu Giriniz :'))

sonuc=(kg) / (hg ** 2)

if(sonuc>=0 and sonuc<18.4):
    print('Zayıf')
elif(sonuc>=18.5 and sonuc<=24.9):
    print('Normal')
elif(sonuc>=24.9 and sonuc<=29.9):
    print('Kilolu')
elif(sonuc>=29.9 and sonuc<=34.9):
    print(ad,' Obez ',sonuc)
    """
