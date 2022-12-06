import os
# import datetime

# result =dir(os)
# result = os.name

# dizin değiştirme
# os.chdir('C:\\')
# os.chdir('../..')

# klasör oluşturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasor")
# os.rename("newdirectory","AkilliKlasor")
# os.rmdir("a")
# os.removedirs("AkilliKlasor/yeniklasor")

# listeleme
# result=os.listdir()
# result = os.listdir("C:\\")
# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

# etkin dizi öğrenme
# result = os.getcwd()



# result = os.stat("datetime.py")
# result = result.st_size/1024
# result = datetime.datetime.fromtimestamp(result.st_ctime) değiştirilme tarihi
# result = datetime.datetime.fromtimestamp(result.st_mtime) son erişme tarihi
# result = datetime.datetime.fromtimestamp(result.st_atime) değiştirilme tarihi

# os.system("notepad.exe")

# path  

result = os.path.abspath("-os.py")
result = os.path.dirname("C:/Users/teknikservis/Desktop/IleriSeviyePythonModulleriveWebScraping/-os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("_os.py")
result = os.path.exists("C:/Users/teknikservis")
result = os.path.isdir("C:/Users/teknikservis")
result = os.path.isfile("C:/Users/teknikservis/os.py")
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")
# result = result[0]
result = result[1]

print(result)