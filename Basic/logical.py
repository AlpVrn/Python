from cgitb import reset
from re import T
from unittest import result


x=5
sorgu=5<=x<10
hak=5
devam ='e'

print(sorgu)

sorgu=x>5 and x<10
sorgu =(hak>0) and (devam=='e')

#or

sorgu=(x>0) or (x%2==0)

#True ,False =>True
#True,True=>True
#False,False=>False

result= not(x>0)

#x,5-10 arasında olan bir çift sayı mı?
 
(x>5) and (x<10) and (x%2==0)

print(result)