# class
class Person :
    pass
    #class  attributes
    adress = 'no info'
    #constructor (yapıcı ekici)
    def __init__(self,name,year):
                #object  attributes
        self.name=name
        self.year=year
        print('init metodu çalıştı')
        #methods

#object (instance)
#okunurluğu çoğaltmak için etiket iyi gidiyo
p1 = Person(name='ali',year=1990)
p2 = Person(name='yağmur',year=1995)

#updating
p1.name='Amet'
p2.name='Obaa'
Person.adress='KocaELi'
#accesing object attributes
print(f'{p1.name} kişisi {p1.year} yaşındadır adresi ise {Person.adress}')
print(f'{p2.name} kişisi {p2.year} yaşındadır adresi ise {Person.adress}')
print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1==p2)