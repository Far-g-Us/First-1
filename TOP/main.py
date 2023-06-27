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
import copy
# создание персонажа
def attack():
    print("Включен режим атаки")
def shot():
    print("выстрел")
Person = {
    "name" : "Варвар",
    "gender" : "Мужской",
    # "actions" : {
    #     "attack" : attack
    # }
}


# создание расы на основе персонажа
Human = copy.deepcopy(Person)
Human["race"] = "Человек"
Human["skills"] = "Быстрый бег", "Красноречие"

Orc = copy.deepcopy(Person)
Orc["race"] = "Орк"
Orc["skills"] = "Выносливость", "Зог-зог"


# создание ролей на основе рас
Warrior = copy.deepcopy(Human) or copy.deepcopy(Orc)
Warrior["role"] = "Воин"
Warrior["desk"] = "Воин - это..."
# Warrior["actions"]["attack"]("удар")

Archer = copy.deepcopy(Human) 
Archer["role"] = "Лучник"
Archer["desk"] = "Лучник - это..."
# Archer["actions"]["attack"]("стрельба")

Shaman = copy.deepcopy(Orc)
Shaman["role"] = "Шаман"
Shaman["desk"] = "Шаман - это..."
# Shaman["actions"]["attack"]("заклинание")


print("-------------------------------------------------------")
print(Person)
print("-------------------------------------------------------")
print(Human)
print("-------------------------------------------------------")
print(Orc)
print("-------------------------------------------------------")
print(Warrior)
print("-------------------------------------------------------")
print(Archer)
print("-------------------------------------------------------")
print(Shaman)
print("-------------------------------------------------------")