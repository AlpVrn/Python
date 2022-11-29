"""""
Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır

Kullanımı : open(dosya,dosya_erişme_modu)
dosya_erişme_modu => dosya hangi amaçla açtığımızı belirtir
"""

# "w": (Write)  yazma modu. 
""" 
    **Dosyayı konuma oluşturur
    **Dosya içeriğini siler ve yeniden ekleme yapar
"""
# file=open("newfile.txt","w")
# file = open("C:/Users/teknikservis/Desktop/a/newfile2.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding="utf-8")
# file.write("Mehmet Alp Varna ığöüç")
# file.close()

# "a": (Append) ekleme. Dosya konumunda yoksa oluşturur

# file = open("newfile.txt","a",encoding="utf-8")
# file.write(" Mehmet Alp Varna\n ")
# file.close()

# "x": (Create) oluşturma. Dosya zaaten varsa hata verir
file = open("newfile.txt","x",encoding="utf-8")
file.close()
# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir
