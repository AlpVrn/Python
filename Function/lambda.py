from inspect import istraceback
import numbers
import re
from unittest import result

square = lambda num:num ** 2
numbers=[1,3,5,9,4,8,24,6,9,75]
"""

def square(num):return num **2

print(list(map(square,numbers)))

for item in map(square,numbers):
    print(item)
"""
#print(list(map(lambda num:num ** 2,numbers)))
#print(list(map(square,numbers)))
check_even= lambda num : num %2==0
"""
def check_even(num): return num%2==0
result= list(list(filter(check_even,numbers)))
result = list(filter(lambda num : num%2==0,numbers))
result = list(filter(,numbers))
print(result)7
"""
#result = list(filter(check_even,numbers))
result = check_even(numbers[2])
print(result)