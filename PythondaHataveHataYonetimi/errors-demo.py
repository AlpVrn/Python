import re
liste = ["1","2","3","5a","10b","abc","10","50"]

# # 1: liste elemanları içindeki sayısal değerleri bulunuz
# for x in liste:
#     try:
#         print(int(x))
#     except(ValueError):
#         continue
#2 : kullanıcı 'q' değerini girmedikçe aldığınız her input sayı
#olduğundan emin olunuz aksi halde hata mesajı yazınız
# while True:
#     try:
#         deger=int(input('Bir sayı giriniz'))
#         if deger=="q":
#             break
#     except Exception as a:
#         print('aaa tekrar dene')
# print('Floop is over')

# while True:
#     sayi = input('sayi : ')
#     if sayi =='q':
#         break

#     try:
#         result = float(sayi)
#         print('girdiğiniz sayi ' , result)
#     except ValueError:
#         print('geçersiz sayi')
#         continue


#3: girilen parola içinde türkçe karakter hatası veriniz
# password=input('Bir sifre giriniz turkce karakter kullanmayaniz')
# if(re.search("[ı,ğ,ü,ö,ç]",password)):
#     raise Exception("türkçe karakter kullanma")


#4 faktoriyel fonksiyonu oluşturup fonksiyona 
# geleen değer için hata veriniz


def calculationFactorial ():
  try:
    number = int (input("Lütfen faktöriyelini bulmak istediğiniz sayıyı giriniz...\n"))
    factorial = 1
    
    if number >= 0:
        for i in range (1, number+1): #range varsayılan olarak 0'dan başlar ve son değeri kapsamaz
        factorial = factorial*i
        print("Girdiğiniz sayının faktöriyeli:",factorial)
  except Exception as a:
      print(f"hat",a)

calculationFactorial ()