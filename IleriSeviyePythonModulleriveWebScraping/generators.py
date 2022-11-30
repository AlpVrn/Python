# def cube():
#     for i in range(500):
#         yield i ** 3 # Bellekte yer kaplamadığı için sadece o anlık lazım olan yerlerde kullanılır

# # iterator = iter(generator)

# for i in cube:
#     print(i)

generator = (i**3  for i in range(5))

# print(next(generator))

for i in generator:
    print(i)