from asyncio import futures
from turtle import clear
from xml.dom.expatbuilder import FragmentBuilder


fruits={'orange','apple','banana'}

print(fruits)

for x in fruits:
    print(x)

fruits.add('cherry')
print(fruits)

fruits.update(['mango','grape','apple'])
print(fruits)

mylist=[1,2,5,4,4,2,1]

print(mylist)
print(set(mylist))


fruits.remove('mango')
fruits.discard('apple')

print(fruits)

fruits.pop()
print(fruits)


fruits.clear()
print(fruits)
