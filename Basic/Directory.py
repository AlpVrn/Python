from urllib.request import AbstractDigestAuthHandler


sehirler=['Kocaeli','İstanbul']
#plaka=[41,34]
#
#print(plaka[sehirler.index('İstanbul')])
#
#plaka = {'Kocaeli' : 41,'İstanbul':34}
#
#print(plaka['Kocaeli'])
#print(plaka['İstanbul'])
#
#plaka['Ankara']=6
#plaka['Kocaeli']='new value'
#
#
#print(plaka)


user={
    'alpvarna':{
        'age':18,
        'roles':['admin','user'],
        'email':'alpvrn@gmail.com',
        'adres':'İstanbul',
        'phone':'123123123'
    },

    'mehmet':{
        'age':18,
        'roles':['user'],
        'email':'mhmt@gmail.com',
        'adres':'Kocaeli',
        'phone':'123454321'
    }

}

print(user['alpvarna'])
print(user['alpvarna']['roles'][0])
