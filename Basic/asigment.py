#x,y,z=5,16,20

# X=X+,-,*,/,%5

#x +=5
#x -=5
#x *=5
#x /=5
#x %=5
#y //=5
#y **= 5 

#print(x,y,z)
 
from ast import Try


values = 1,2,3,4,5

print(values)
print(type(values))

x,y,*z=values


print(x,y,z)
print(x,y,z[1])

