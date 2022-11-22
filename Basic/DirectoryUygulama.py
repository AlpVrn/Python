# HATALI DOSYA !!!!!!!!! https://www.btkakademi.gov.tr/portal/course/player/deliver/sifirdan-ileri-seviye-python-programlama-5877





"""ogrenciler={
    '120':{
        'Ad':'Ali',
        'Soyad':'Yılmaz',
        'Telefon':'1231231230'
    },
    '125':{
        'Ad':'Can',
        'Soyad':'Korkmaz',
        'Telefon':'321321321'
    },
    '128':{
        'Ad':'Volkan',
        'Soyad':'Yükselen',
        'Telefon':'543543543'
    }
}
"""""

ogrenciler={}

number=int(input("ID Girişi Yapınız: "))
name=str(input("İsim Girişi Yapınız"))
surname=str(input("Soyisim Girişi Yapınız"))
Phone=str(input("Son Olarak Telefon Numarası Girişi Yapınız"))

#ogrenciler [number]={
#    'Ad':name,
#    'Soy Ad':surname,
#    'Telefon':Phone
#}
#print(ogrenciler)

ogrenciler.update({
    number: {
        'Ad': name,
        'Soyad':surname,
        'Telefon':Phone
    }
})
print('*'*50)

OgrNo=int(input('ogremci No:'))
Ogrenci=ogrenciler[OgrNo]
print(Ogrenci)



#BURASI HATALI

#print(f'Aradıığnız {OgrNo} nolu öğrenci adı : {ogrenciler[name]} soyadi : {ogrenci[surname]}')