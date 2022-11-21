## class
#class Person :
#    pass
#    #class  attributes
#    adress = 'no info'
#    #constructor (yapıcı ekici)
#    def __init__(self,name,year):
#                #object  attributes
#        self.name=name
#        self.year=year
#        print('init metodu çalıştı')
#        #methods
#
##object (instance)
##okunurluğu çoğaltmak için etiket iyi gidiyo
#p1 = Person(name='ali',year=1990)
#p2 = Person(name='yağmur',year=1995)
#
##updating
#p1.name='Amet'
#p2.name='Obaa'
#Person.adress='KocaELi'
##accesing object attributes
#print(f'{p1.name} kişisi {p1.year} yaşındadır adresi ise {Person.adress}')
#print(f'{p2.name} kişisi {p2.year} yaşındadır adresi ise {Person.adress}')
#print(p1)
#print(p2)
#print(type(p1))
#print(type(p2))
#print(p1==p2)

class Person:
        #class attributes
        address = 'no info'
        #consteuctor (yapıcı metod)
        def __init__(self,name,year):

                #object attributes
                self.name=name
                self.year=year
                print('init metodu çaıştı')

        #instance methods
        def intro(self):
                print('Hello There. I am '+self.name)

        #instance methods
        def calculateAge(self):
                return 2022 - self.year

#objecy (instance)
p1=Person(name = 'Mamut',year = 1990)
p2=Person(name ='Yağmur',year = 1995)

p1.intro()
p2.intro()

print(f'adım: {p1.name} yaşim {p1.calculateAge()}')
print(f'adım: {p2.name} yaşim {p2.calculateAge()}')
#updating
p1.name='amet'
p1.address='kocaeli'



class Circle:
        #Class object attribute
        pi = 3.14

        def __init__(self,yaricap=1) :
                self.yaricap=yaricap
        
        #Methods
        def cevre_hesapla(self):
                return 2 * self.pi * self.yaricap
        
        def alan_hesapla(self):
                return self.pi * (self.yaricap**2)

c1=Circle() # yarıçapı = 1
c2=Circle(5)
print(f'c1 : alan = {c1.alan_hesapla()} cevre = {c1.cevre_hesapla}')
print(f'c2 : alan = {c2.alan_hesapla()} cevre = {c2.cevre_hesapla}')