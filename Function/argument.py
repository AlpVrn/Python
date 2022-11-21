"""def changeName(name):
    n='Ada'

name = 'Yiğit'

changeName(name)
print(name)


def change(n):
    n[0] = 'İstanbul'

sehirler = ['ankara','izmir']

change(sehirler)

print(sehirler)

sehirler=['ankara','izmir']
n= sehirler[:]
n[0]='İstanbul' 
print(sehirler)
print(n)


def add(a,b,C=0):
    return sum((a,b,C))

print(add(10,20))
print(add(10,20,30))

def add(*params):
    print(params)
    return sum((params))
print(add(10,20))
print(add(10,20,30,46,42,56,87,23,41))
"""
from inspect import ArgSpec
from re import A


def displayUser(**args):
    for key ,value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name= 'Çınar',age = 2, city = 'İstanbul')
displayUser(name='Alp',age=18,city='Kocaeli',phone = '0555433444')
displayUser(name='Mehmet',age=14,city='Kocaeli',phone = '0555433444',email='mehmet@gmail.com')

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,70,key1='value 1', key2='value 2')