# Делегирование + мышление ООП




# двигатель и его функции
# def start():
#     print("Запуск")

# def stop():
#     print("Стоп")

# Engine = {
#     "start" : start,
#     "stop" : stop,
# }
# # Engine["start"]()
# # Engine["stop"]()

# def open():
#     print("Капот открыт")
# def close():
#     print("Капот закрыт")

# Bonnet = {
#     "open" : open,
#     "close" : close,
# }

# # основа авто
# Car = {
#     "color" : "",
#     "marka" : "",
#     "engine" : "",
#     "bonnet" : "",
# }

# auto = Car

# auto["marka"] = "audi"
# auto["color"] = "green"
# auto["engine"] = Engine
# # print(auto)
# auto["engine"]["start"]()


# основная функция
# def Car(marka,color,engine):
#     thisMarka = marka
#     thisColor = color
#     # thisEngine = engine

#     activeList = {
#         "showMarka" : showMarka,
#     }

#     def showMarka(param):
#         print(param)

# двигатель

# auto = Car("audi","green")
# import copy
# # создание персонажа
# def attack():
#     print("Включен режим атаки")
# def shot():
#     print("выстрел")
# Person = {
#     "name" : "Варвар",
#     "gender" : "Мужской",
#     # "actions" : {
#     #     "attack" : attack
#     # }
# }


# # создание расы на основе персонажа
# Human = copy.deepcopy(Person)
# Human["race"] = "Человек"
# Human["skills"] = "Быстрый бег", "Красноречие"

# Orc = copy.deepcopy(Person)
# Orc["race"] = "Орк"
# Orc["skills"] = "Выносливость", "Зог-зог"


# # создание ролей на основе рас
# Warrior = copy.deepcopy(Human) or copy.deepcopy(Orc)
# Warrior["role"] = "Воин"
# Warrior["desk"] = "Воин - это..."
# # Warrior["actions"]["attack"]("удар")

# Archer = copy.deepcopy(Human) 
# Archer["role"] = "Лучник"
# Archer["desk"] = "Лучник - это..."
# # Archer["actions"]["attack"]("стрельба")

# Shaman = copy.deepcopy(Orc)
# Shaman["role"] = "Шаман"
# Shaman["desk"] = "Шаман - это..."
# # Shaman["actions"]["attack"]("заклинание")


# print("-------------------------------------------------------")
# print(Person)
# print("-------------------------------------------------------")
# print(Human)
# print("-------------------------------------------------------")
# print(Orc)
# print("-------------------------------------------------------")
# print(Warrior)
# print("-------------------------------------------------------")
# print(Archer)
# print("-------------------------------------------------------")
# print(Shaman)
# print("-------------------------------------------------------")



# Классы в Python



# class Car:
#     def __init__(self,color,marka,motor,wheel,headlights): # создание переменных для класса (объект)
#         self.color = color
#         self.marka = marka
#         self.engine = motor
#         self.wheel = wheel
#         self.headlights = headlights

#     # методы действия с определёнными классами
#     def showColor(self):
#         print(self.color)

#     def showMarka(self):
#         print(self.marka)
    
# class Engine:
#     def __init__(self,HP,volume):
#         self.HP = HP
#         self.volume = volume

#     def start(self):
#         print("Запуск")

#     def stop(self):
#         print("Стоп")    

# class Wheel:
#     def __init__(self,turningRadius,diameterWheel):
#         self.turningRadius = turningRadius
#         self.diameterWheel = diameterWheel

#     def turnLeft(self):
#         print("Поворот влево")

#     def turnRight(self):
#         print("Поворот право")

# class Headlights:
#     def __init__(self,optics):
#         self.optics = optics
        
#     def on(self):
#         print("Вкл фар")

#     def off(self):
#         print("Выкл фар")

# myHeadlights = Headlights("LED")
# myWheel = Wheel("1960","18")
# myEngine = Engine("120","2.0")
# twoEngine = Engine("280","2.2")
# myAuto = Car("green","audi",twoEngine,myWheel,myHeadlights)

# class Abs:
#     def __init__(self,availability):
#         self.availability = availability

# print(myAuto.engine.HP)

# myEngine.start()



# наследование

# class SportCar(Car):
#     def __init__(self, color, marka, motor, wheel, headlights, abs):
#         # self.color = color
#         # self.marka = marka
#         # self.engine = motor
#         # self.wheel = wheel
#         # self.headlights = headlights
#         self.abs = abs
#         super().__init__(color, marka, motor, wheel, headlights)

# class SportEngine(Engine):
#     def __init__(self, HP, volume,turbo):
#         self.turbo = turbo
#         super().__init__(HP, volume)

# myHeadlights = Headlights("Halogen")
# myWheel = Wheel("1820","19")
# myAbs = Abs("Yes")
# porsheEngine = SportEngine("540","6.0",2)
# twoAuto = SportCar("blue","porshe",porsheEngine,myWheel,myHeadlights,myAbs)




# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def __init__(self,name,sound):
#         self.name = name
#         self.sound = sound
    
#     def activeSound(self):
#         print(self.sound)

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Мяу")

#     def porr(self):
#         print("Мурлыкает")

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Гав")

#     def digHole(self):
#         print("Копает яму")

# class Donkey(Animal):
#     def __init__(self, name, sound):
#         super().__init__(name, "иа-иа")

# myCat = Cat("Вася")
# myCat.porr()

# myDonkey = Animal("Вася")
# myDonkey.activeSound()

# class human(ABC):
#     @abstractmethod
#     def __init__(self,name,nationality):
#         self.name = name
#         self.nationality = nationality

# class Man(human):
#     def __init__(self, name, nationality):
#         self.gender = "Мужской"
#         super().__init__(name, nationality)

# class Woman(human):
#     def __init__(self, name, nationality):
#         self.gender = "Женский"
#         super().__init__(name, nationality)

# man = Man("Alex","China")    
# women = Woman("Vera","Italia")

# class Grandfather(ABC):
#     def __init__(self,name,haircolor):
#         self.name = name
#         self.haircolor = haircolor
    
#     def cookingBorsh(self):
#         print("Варим борщ")
    
#     def repeirCar(self):
#         print("Ремонтирует автомобиль")

# class Father(Grandfather):
#     def __init__(self,name,haircolor):
#         super().__init__(name,haircolor)

# Michail = Father("Михаил","Русый")
# Michail.cookingBorsh()

# class Bird():
#     def __init__(self,name,sound):
#         self.name = name
#         self.sound = sound

#     def eat(self):
#         print("Кушает")

#     def hunting(self):
#         print("Охотится")

#     def activeSound(self):
#         print(self.sound)

# class flyBird(Bird):
#     def __init__(self, name,sound):
#         super().__init__(name,sound)
    
#     def fly(self):
#         print("Летает")

# class noFly(Bird):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def walk(self):
#         print("Ходит")

# class Crow(flyBird):
#     def __init__(self, name,):
#         super().__init__(name,"Кар")
    
    

# crow = Crow("Вася")
# crow.activeSound()


base_list = [
    {
        "first_name" : "Денис",
        "last_name" : "Кириллов",
        "birthday" : "01.06.2001",
        "gender" : "Мужской",
        "login" : "denis161",
        "password" : "12345"
    },
    {
        "first_name" : "Кирилл",
        "last_name" : "Кириллов",
        "birthday" : "17.08.2006",
        "gender" : "Мужской",
        "login" : "kirillooo",
        "password" : "12345"
    },
    {
        "first_name" : "Максим",
        "last_name" : "Максимов",
        "birthday" : "11.04.2000",
        "gender" : "Мужской",
        "login" : "maks07",
        "password" : "12345"
    },
    {
        "first_name" : "Руслан",
        "last_name" : "Русланов",
        "birthday" : "11.02.2000",
        "gender" : "Мужской",
        "login" : "russlan",
        "password" : "12345"
    },
    {
        "first_name" : "Екатерина",
        "last_name" : "Исаева",
        "birthday" : "25.10.2000",
        "gender" : "Женский",
        "login" : "ekaterina25e",
        "password" : "12345"
    },
]
registered_users = [

]
class User():
    def __init__(self,user_id,first_name, last_name, birthday , gender, login, password) :
       self.user_id = user_id
       self.first_name = first_name
       self.last_name = last_name
       self.birthday = birthday
       self.gender = gender
       self.login = login
       self.password = password
       #-----------------------
       self.status = "user"
       self.blocking = False

    # Если в классе есть методы с словом update, значит этот метод для изменения информации
    def update_first_name(self, new_first_name):
        self.first_name = new_first_name
        print(f"новое имя : {self.first_name}")
    def update_last_name(self, new_last_name):
        self.last_name = new_last_name
    def update_birthday(self, new_birthday):
        self.birthday = new_birthday
    def update_gender(self, new_gender):
        self.gender = new_gender
    def update_password(self, new_password):
        if self.password == input("Введите старый пароль: "):
            self.password = new_password

class Moderator(User):
    def __init__(self, user_id, first_name, last_name, birthday, gender, login, password):
        super().__init__(user_id, first_name, last_name, birthday, gender, login, password)
        self.status = "moderator"
    # блокировка пользователей
    def blocking_user(self, users_list):
        text_user_list = f"id | first_name | blocking | status \n"
        for i in range(0,len(users_list)):
            text_user_list += f"{users_list[i].user_id}  {users_list[i].first_name}  {users_list[i].blocking} {users_list[i].status}\n"
        print(text_user_list)
        input_user_id = int(input("Введите id пользователя для блокировки"))
        for i in range(0,len(users_list)):
            if self.status == "moderator":
                if input_user_id == i and users_list[i]['status'] != "moderator" and users_list[i]['status'] != "admin":
                    if users_list[i]['blocking'] == True:
                        print("пользователь уже заблокирован")
                        break
                    else:
                        users_list[i]['blocking'] = True
                        print("пользователь успешно заблокирован")
                        break
            elif self.status == "admin":
                if input_user_id == i:
                    if users_list[i]['blocking'] == True:
                        print("пользователь уже заблокирован")
                        break
                    else:
                        users_list[i]['blocking'] = True
                        print("пользователь успешно заблокирован")
                        break

class Admin(Moderator):
    def __init__(self, user_id, first_name, last_name, birthday, gender, login, password):
        super().__init__(user_id, first_name, last_name, birthday, gender, login, password)
        self.status = "admin"
    def delete_user_list(self, users_list):
        users_list.clear()
        print("База данных пуста")
                                # massiv - массиом данных
    def create_user_list(self, massiv, users_list):
        print(len(users_list))
        for i in range(0,len(massiv)):
            users_list.append(User(user_id=i+1, 
                                first_name=massiv[i]["first_name"],
                                last_name=massiv[i]["last_name"],
                                birthday=massiv[i]["birthday"],
                                gender=massiv[i]["gender"],
                                login=massiv[i]["login"],
                                password=massiv[i]["password"]))

class Registration():
    def create_user(self,users_list):
        users_list.append(User( len(users_list),
                                input("введите имя: "),
                                input("введите фамилию: "),
                                input("Дата рождения(дд.мм.гггг): "),
                                input("Введите пол: "),
                                input("Введдите логин:"),
                                input("введите пароль: ")))

class InLog():
    def __init__(self, login, password):
        self.login = login
        self.password = password
    def log_in_account(self,users_list):
        for i in range(len(users_list)):
            if users_list[i].login == self.login and users_list[i].password == self.password:
                print("вход выполнен")
                break
            elif i == len(registered_users):
                print("Ошибка")



class Manager():
    def __init__(self,reg,inlog,userModerAdmin,datalist):
        self.reg = reg 
        self.inlog = inlog
        self.userModerAdmin = userModerAdmin
        self.datalist = datalist
    def work(self):
        print(self)
        

my_reg = Registration
my_inLog = InLog
my_person_list = [User,Moderator,Admin]
my_base = []
# my_person_list[0](10,"admin","admin","01.01.1970","Мужской","admin","admin")
myManager = Manager(my_reg,my_inLog,my_person_list,my_base)
myManager.userModerAdmin[0](10,"admin","admin","01.01.1970","Мужской","admin","admin")
myManager.inlog("admin","admin")
# class Manager(Registration,InLog):
#     def __init__(self) -> None:
#         super().__init__()


# proverka = Registration()
# proverka.create_user()

# myAdmin = Admin(10,"admin","admin","01.01.1970","Мужской","admin","admin")
# myAdmin.create_user_list(base_list,registered_users)

# myLogin = InLog(input("Введите логин:"),input("введите пароль"))
# myLogin.log_in_account()



# print(len(registered_users))
# myAdmin.blocking_user(registered_users)
# print(registered_users)
# print(registered_users[0].first_name)
# registered_users[0].update_first_name("Denis")
# print(registered_users[0].first_name)


# base_list = [
#     {
#         "first_name" : "Денис",
#         "last_name" : "Кириллов",
#         "birthday" : "01.06.2001",
#         "gender" : "Мужской",
#         "login" : "denis161",
#         "password" : "12345"
#     },
#     {
#         "first_name" : "Кирилл",
#         "last_name" : "Кириллов",
#         "birthday" : "17.08.2006",
#         "gender" : "Мужской",
#         "login" : "kirillooo",
#         "password" : "12345"
#     },]


# primer = [
#     User(0,"name","last_name","01.06.2001","Мужской","login","pass"),
#     User(1,"name","last_name","01.06.2001","Мужской","login","pass"),
# ]



["747278"/"747234"/"747316"/"747226"/"744698"/"747154"]