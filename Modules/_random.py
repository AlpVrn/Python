import random

# result = dir(random)
# result = help(random)

# result = random.random()* 100#0.0 - 1.0
# result = int(random.uniform(100,1000))
result = random.randint(1,100)

greeting = 'hello there'
names = ['ali','yağmur','deniz','cenk']
result = names[random.randint(0,len(names)-1)]
result = random.choice(names)
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
result= liste

liste = range(100)
result= random.sample(liste,3)
result = random.sample(names,2)
print(result) 