import random

rastgele=random.randint(0,100)
print(rastgele)
can=int(input('Kaç can istiyon : '))
sayac=0
while can>0:
    can-=1
    tahmin=int(input('Tahmin Girin : '))
    sayac+=1

    if rastgele==tahmin:
        print(f'Tebrikler Bildiniz: {sayac}. kerede Tahmin Ettiniz Puanınız {100-(100/can)*(sayac-1)}')
        break
    elif rastgele>tahmin:
        print('Üs sayı deneyin')
    else:
        print('Alt sayı deneyin')

    if can==0:
        print(f'Hakkınız Bitmiştir Tutulan sayı : {rastgele}')