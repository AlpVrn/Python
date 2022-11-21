"""sayi=int(input("Bir Sayı Giriniz . "))
sayi1=sayi
if sayi%sayi==0 and sayi%2==1 or sayi==2:
    print('Bu bir asal sayıdır')
else:
    print("Bu bir asal sayı diğildir")
"""

from operator import truediv


sayi=int(input('Sayı Giriniz'))
asalmi = True

if sayi==1:
    print('1 sayısı asal diğildir')

for i in range (2,sayi):
    if sayi % i == 0 :
        asalmi=False
        break

if asalmi:
    print('sayı asaldır')

else:
    print('asal değildir')