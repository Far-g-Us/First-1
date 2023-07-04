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




from abc import ABC,abstractmethod

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

class Bird():
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def eat(self):
        print("Кушает")

    def hunting(self):
        print("Охотится")

    def activeSound(self):
        print(self.sound)

class flyBird(Bird):
    def __init__(self, name,sound):
        super().__init__(name,sound)
    
    def fly(self):
        print("Летает")

class noFly(Bird):
    def __init__(self, name):
        super().__init__(name)
    
    def walk(self):
        print("Ходит")

class Crow(flyBird):
    def __init__(self, name,):
        super().__init__(name,"Кар")
    
    

crow = Crow("Вася")
crow.activeSound()