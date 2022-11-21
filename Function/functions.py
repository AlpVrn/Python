"""
from unicodedata import name


def SayHello(name='User'):
    return('Hello ' + name)


msg=SayHello('Alp')
print(msg)
SayHello()

def toplam(num1,num2):
    return num1+num2

agaaa=toplam(5,8)
print(agaaa)
"""
def hesap(dogum):
    return 2022-dogum

AlpAge=hesap(2004)

from binascii import rledecode_hqx
import re


def emeklilik(DogumYili):
    """
    DOCSTRING : Doğumm yılınza göre emekliliğinze kaç yıl kaldı 
    INTPUT : Doğum Yılı
    OUTPUT : Emeklilik sonucunuz
    """
    
    yas=hesap(DogumYili)
    emeklilik=65-yas

    if emeklilik>0:
        print(f'Emekliliğinize {emeklilik} yıl kaldı')
    else:
        print('Zaten emekli oldunuz')

print(emeklilik(2004))

print(help(emeklilik))

print(help(list.append()))