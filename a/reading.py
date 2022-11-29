# try:
#     file = open("newfile2.txt","r")
# except FileNotFoundError as miss:
#     print("Dosya bulunamıyor",miss)
# finally:
#     print("dosya kapandı")
#     file.close()

file = open("newfile.txt","r",encoding="utf-8")

# # for döngüsü

# for i in file:
#     print(i,end="")


# Read Fonksiyonu

# content1= file.read()
# print("içerik 1")
# print(content1)

# file = open("newfile.txt","r",encoding="utf-8")
# content2=file.read()

# print("içerik 2")
# print(content2)

# kaynak=file.read(5)
# kaynak = file.read(3)
# kaynak = file.read(8)
# print(kaynak)
# *********************** readline() fonksiyonu


# print(file.readline(),end="")


#************ readlines() fonksiyonu 

liste= file.readlines()

print(liste[0])

file.close()