#Inheritance (Kalıtım) : Miras alma

#Person => name, lastname, age, eat (), run(), drink()
#Student(Person), Teacher(Person)

#Animal =>Dog(Animal), Cat(Animal)

class Person():
    def __init__(self,fname,lname) :
        self.firstName=fname
        self.lastName=lname 
        print('Person created')

    def who_i_am(self):
        print('I am a person')
    
    def eat(self):
        print('I am eating')




class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.stundentNumber = number
        print('Student created')

    #override
    def who_i_am(self):
        print('I am Student')

    def SayHello(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self, fname, lname,branch):
        super().__init__(fname,lname,)
        self.branch = branch
        
    def who_i_am(self):
        print(f'I am a {self.branch} teacher')
 
p1=Person('Ali','Yılmaz')
s1=Student('Çınar','Turan',1234)
t1=Teacher('Alp','Varna','SeSa')

t1.who_i_am()

print(p1.firstName + ' ' + p1.lastName )
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.stundentNumber))

p1.who_i_am()
s1.who_i_am()
p1.eat()
s1.eat()
s1.SayHello()