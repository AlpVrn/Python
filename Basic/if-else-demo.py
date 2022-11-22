"""""
name=input('İsim Giriniz : ')
age=int(input('Yaş Giriniz : '))
study=input('Eğitim Durumunuzu Giririniz : ')

if age>=18:
    if study=='Lise' or study=='Uni':
        print('Ehliyet Alabilirsiniz sayın ',name)
    else:
        print('Ehliyet Alamazsınız sayın ',name)
else:
    print('Ehliyet Alamazsınız sayın ',name)
"""
"""""
from turtle import pen


not1=int(input('1. Notunuzu Giriniz : '))
not2=int(input('2. Notunuzu Giriniz : '))

ortlama=(not1+not2)/2

if ortlama>=0 and ortlama<24:
    print('0')
elif ortlama>24 and ortlama<44:
    print("1")
elif ortlama>44 and ortlama<=54:
    print("2")
elif ortlama>54 and ortlama<69:
    print("3")
elif ortlama>=70 and ortlama<84:
    print("4")
elif ortlama>84 and ortlama<=100:
    print("5")
"""

#HATALI gibi
import datetime

history=input('Araç Gününü Giriniz (2018/8/1)')
history =history.split('/')

#print(history[0])
#print(history[1])
#print(history[2])int(
trafigecikis=datetime.datetime(int(history[0]),int(history[1]),int(history[2]))
simdi=datetime.datetime.now()
fark=simdi-trafigecikis
days=fark.days
if days<=365:
    print('Araç 1. Yılında')
elif days>=365 and days<365*2:
    print('Araç 2. Yılında')
elif days>=365*2 and days<365*3:
    print('Araç 3. Yılında')

else:
    print("Hatalı Giriş")