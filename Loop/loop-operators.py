"""
for item in range(30,100,10):
    print(item)

print(list(range(5,100,10)))

#enumerate
from operator import itemgetter


index=0
greeting='hello there'

for item in enumerate(greeting):
    print(item)

#print(f'index{index} letter {letter}')
    #index+=1

    for letter in greeting:
    print(f'index {index} letter {greeting[index]}')
    index+=1 
"""

list1=[1,2,3,4,5]
list2=['a','b','c','d','e']
list3=[100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for za in list(zip(list1,list2,list3)):
    print(za)
    
for item in zip(list1,list2,list3):
    print(item)
for a,b,c in zip(list1,list2,list3):
    
    print(a,b,c)