import re
x=10

# if x > 5:
#     raise Exception("x 5 den büyük değer almaz")

# def check_password(pws):
    
#     if len(pws)<8:
#         raise Exception("Parola en az 7 karakter olmalıdır")
#     elif not re.search("[a-z]",pws):
#         raise Exception("parola küçük harf içermektedir")
#     elif not re.search("[A-Z ]",pws):
#         raise Exception("parola büyük harf içermelidir")
#     elif not re.search("[0-9]",pws):
#         raise Exception("parola rakam içermelidir")
#     elif not re.search("[_@$]",pws):
#         raise Exception("parola alpha numeric karakter içermelidir")
#     elif re.search("\s",pws):
#         raise Exception("Parola boşluk içermemlidir")
#     else:
#         print('geçerli parola')
    
# password="12345678aA$"

# try:
#     check_password(password)
# except Exception as ex :
#     print(ex)
# else:
#     print('Geçerli parola : else')
# finally:
#     print('validation tamamlandı')

class person:
    def __init__(self,name,year):
        if len(name)>10:
            raise Exception("name alanı fazla karakter içeriyor")
        else:
            self.name=name

person("Aliiiiiiiiiiiiii",1989)