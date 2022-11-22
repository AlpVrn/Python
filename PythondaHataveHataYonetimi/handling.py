#eorror handling => hata yönetimi
try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except (ZeroDivisionError,ValueError) as e:
    print('Yanlış bilgi girdiniz')
    print(e)