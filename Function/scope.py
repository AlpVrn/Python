"""
x = 'global x'

def function():
    x = 'local x'
    print(x)

function()
print(x)
"""
###################################################
name = 'Alp'
def changeName(new_name):
    #local 
    name = new_name
    print(name) 


changeName('Alp')
print(name)
#######################################################

name = 'global string'
def greeting():
    #name = 'Alp'

    def hello():
        print('hello'+ name)

    hello()
greeting() 
#########3###
x=50
#Bozuk Yapamadım
def test(x):
    global x
    print(f'x : {x}')
    
    x=100
    print(f'changed x to {x}')

test(x)
print(x)