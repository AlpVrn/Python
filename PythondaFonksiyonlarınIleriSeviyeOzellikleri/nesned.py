# def greeting(name):
#     print('helo',name)



# sayHello=greeting
# del sayHello
# print(sayHello)
# print(greeting)

#encapsultaion
# def outer(num1):
#     print("outer")
#     def inner_increment(num1):#< sadace outer çalıştığında çalışır
#         print("inner")
#         return num1 +1
#     num2 = inner_increment(num1)
#     print(num1,num2)

# print(outer(10))


def factorial(number1):
    
    if not number1>=0:
        raise ValueError("girdiğiniz sayı 0 dan büyük olmalıdır")

    def inner_factorial(number):
        if number<=1:
            return 1

        return number * inner_factorial(number-1)
    return inner_factorial(number1)
#Program değiştirildi
try:
    sayi=int(input("Bir sayi giriniz : "))
    print(factorial(sayi))
except ValueError:
    raise ValueError("Girdiğin değer sayı olmalıdır")
