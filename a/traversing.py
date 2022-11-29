with open("newfile.txt","r",encoding="utf-8") as file:
    contenct = file.read(10)
    print(contenct)
    file.seek(0)
    print(file.tell())
    contenct2 = file.read()
    print(contenct2)