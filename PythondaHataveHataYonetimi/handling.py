#eorror handling => hata yönetimi
# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# # except (ZeroDivisionError,ValueError) as e:
# except:
#     print('Yanlış bilgi girdiniz')
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as hata:
        print('Yanlış bilgi girdiniz ' , hata)
    else:
        break
    finally:
        print('Try except sonlandı.')