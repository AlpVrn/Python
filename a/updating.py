# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     file.write("deneme")

# with open("newfile.txt","r+" ,encoding="utf-8" , errors="ignore") as file:
#     print(file.read())

# ********* Sayfa sonunda güncelleme

# with open("newfile.txt","a",encoding="utf-8")as file:
#     file.write("AlpCartcurt Varna")

#************ Sayfa başında güncelleme ***********
# with open("newfile.txt","r+" ,encoding="utf-8",errors="ignore") as file:
#     contenct= file.read()
#     contenct = "mehmet ALp Varna \n"+contenct 
#     file.seek(0)
#     file.write(contenct)
#     print(contenct)

# with open("newfile.txt","r" ,encoding="utf-8" , errors="ignore") as file:
#     print(file.read())


# ********** Sayfa ortasında güncelleme *********

with open("newfile.txt","r+",encoding="utf-8")as file:
    list = file.readlines()
    list.insert(1,"AAAAAA\n")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8")as file:
    print(file.read())
