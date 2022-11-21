#Bankamatik Uygulaması

from glob import iglob
from tkinter import E


AlpHesap = {
    'ad' : 'Alp Varna',
    'hesapNo' : '13245678',
    'bakiye' : 2000,
    'ekHesap' : 2000
}

MehmetHesap = {
    'ad' : 'Mehmet Varna',
    'hesapNo' : '13245678',
    'bakiye' : 2000,
    'ekHesap' : 1000
}

def paraCek(hesap,miktar):
    print(f'Merhaba '+hesap['ad'])

    if (hesap['bakiye']>= miktar):
        hesap['bakiye'] -=miktar
        print('Paranızı Alabilirsiniz.')
    else:
        toplam = hesap['bakiye']+hesap['ekHesap']

        if (toplam>=miktar):
            ekHesapKullanimi = input('ek hesap kullanmak ister misiniz (e/h) = ')
            
            if ekHesapKullanimi== 'e':
                ekHesapKullanilicakMiktar= miktar - hesap['bakiye']
                hesap['bakiye']=0
                hesap['ekHesap'] -=ekHesapKullanilicakMiktar
                print('paranızı alabilirsiniz')

            else:
                print(f"{hesap['hesapNo']} nolu hesabınıza ek hesap ile birlikte {toplam}  bulunmaktadır: (Bakiye {hesap['bakiye']} Ek Hesap {hesap['ekHesap']})")
        
        else:
            print('üzgünüz bakiye yetersizdir')

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabın Bakiye {hesap['bakiye']} Ek Hesap {hesap['ekHesap']} TL si vardır")

bakiyeSorgula(AlpHesap)
bakiyeSorgula(MehmetHesap)
print("***************")
paraCek(MehmetHesap,3000)
paraCek(AlpHesap,3000)
print("***************")
bakiyeSorgula(AlpHesap)
bakiyeSorgula(MehmetHesap)