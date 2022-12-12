import json
import os
class User:
    def __init__(self,username,password,email):
        self.username=username
        self.password=password
        self.email=email

class UserRepository:
    def __init__(self):
        self.users=[]
        self.isLoggedIn = False
        self.currentUser={}

        #load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json','r',encoding='utf-8') as file : 
                users=json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username=user['username'],password=user['password'],email= user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self,user:User):
        self.users.append(user)
        self.savetoFile()
        print("Kullanci oluşturuldu.")
    def login(self,username,password): 
        for user in self.users:
            if user.username==username and user.password==password:
                self.isLoggedIn = True
                self.currentUser=user
                print('loggin yapıldı')
                break
    def logout(self):
        self.isLoggedIn=False
        self.currentUser={}
        print('Cikis Yapildi')

    def identity(self):
        if self.isLoggedIn:
            print(f'username  : {self.currentUser.username}')
        else:
            print('giriş yapılmadı')
    def savetoFile(self):
        list=[]

        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open('users.json','w') as file:
            json.dump(list,file)
repository = UserRepository()


while True:
    print("Menü".center(50,"*") )
    secim=input('1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nSeçiminiz : ')
    
    if secim=="5":
        break
    else:
        if secim=="1":
            username=input("Username : ")
            password=input("Password : ")
            email=input("E-mail : ")

            user = User(username=username,password=password,email=email)
            repository.register(user)

            print(repository.users)
        elif secim=="2":
            if repository.isLoggedIn:
                print("Zaten login olunmuş")
            else:
                username = input('Username : ') #logout
                password = input('Password : ')
                repository.login(username,password)#login
        elif secim=="3":
                repository.logout()#logout
        elif secim=='4':
            repository.identity() #display identity
        else:
            print('Yanlis secim')