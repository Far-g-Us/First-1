# v = 90
# t = 1
#                 0          1
# genderList = ["Мужской", "Женский"]
# print(genderList)
#               0  1  2  3  4  5  6  7  8  9
# numberList = [3, 1, 3, 7, 9, 5, 4, 2, 8, 6]   # = 10
# numberList.sort()
# print(len(numberList))

# raceList = ["Человек", "Эльф"]
# print(raceList, "Создали список")
# raceList.append("Гном")
# print(raceList, "raceList.append(\"Гном\")")
# raceList.pop(1)
# print(raceList, "raceList.pop(1)")
# raceList.clear()
# print(raceList, "raceList.clear()")



# numberList = [3, 1, 3, 7, 9, 5, 4, 2, 8, 6]
# print(numberList)
# for i in range (0, len(numberList)):
#     numberList[i] = numberList[i]**2
#     if numberList[i] % 2 !=0:
#         numberList.pop(i)
# print(numberList)

# listN = [ [1, 2, 3, 4, 5], 
#           [6, 7, 8, 9, 10],
#         ]
# for i in range(0, len(listN)):
#     print(listN[i])
#     for j in range(0, len(listN[i])):
#         print(listN[i][j])



# 0 - переменные
# 1 - цикл


# genderList = ["Мyжской", "Женский"] #0.1 - массив для определения пола персонажа
# raceList = ["Человек", "Эльф", "Гном", "Орк", "Таурен", "Тёмный эльф"] #0.2 - массив для выбора расы персонажа
# roleList = ["Воин", "Лучник", "Маг"] #0.3 - массив для выбора роли

# textRace = ""
# for i in range (0, len(raceList)):
#     textRace += f"{i} - {raceList[i]}\n"
# reg_race = False #создали галочку - (нет)
# while reg_race == False: # выполнять пока не совпадёт (False)
#     # принимает только число
#     myRace = int(input(f"Выберите расу:\n{textRace}"))
#     if myRace > len(raceList) or myRace < 0:
#         print("Ошибка: выбери из перечисленного")
#     else:
#         for i in range(0, len(raceList)):
#             if myRace == i:
#                 myRace = raceList[i]   # race = raceList[i]
#                 reg_race = True
#                 print("Вы выбрали:",myRace)
#                 break
                
    
# textGender = ""
# for i in range (0, len(genderList)):
#     textGender += f"{i} - {genderList[i]}\n"
# reg_gender = False
# while reg_gender == False:
#     myGender = int(input(f"Выберите пол:\n{textGender}"))
#     if myGender > len(genderList) or myGender < 0:
#         print("Ошибка: выберите из перечисленного")
#     else:
#         for i in range (0, len(genderList)):
#             if myGender == i:
#                 myGender = genderList[i]   # gender = genderList[i]
#                 reg_gender = True
#                 print("Вы выбрали:",myGender)
#                 break


# textRole = ""
# for i in range (0, len(roleList)):
#     textRole += f"{i} - {roleList[i]}\n"
# reg_role = False
# while reg_role == False:
#     myRole = int(input(f"Выберите роль:\n{textRole}"))
#     if myRole > len(roleList) or myRole < 0:
#         print("Ошибка: выберите из перечисленного")
#     else:
#         for i in range (0, len(roleList)):
#             if myRole == i:
#                 myRole = roleList[i]
#                 reg_role = True
#                 print("Вы выбрали:",myRole)
#                 break

#-----------------------------------------------------------------#


# Задача
# Саша и Маша собирают яблоки на компот
# Т.к. Саша сильнее Маши, он может собирать 6 яблок
# а Маша должна собрать 3 яблока
# Для компота нужно 8 яблок
# Обязательно что бы Маша и Саша принесли 8 яблок
# 9е могут оставить себе

# result = False # False - яблоки не собраны
# masha = 0 # Кол-во собранных яблок
# sasha = 0 # Кол-во собранных яблок
# # Собирать яблоки пока у Маши и Саши не будет 8 шт
# while result == False:
#     # Если Саша собрал меньше чем 6 яблок 
#     # он должен продолжать собирать
#     sasha = int(input("Сколько яблок собрал Саша?: "))
#     if sasha <= 6: 
#         print(f"Саша должен собрать ещё {6 - sasha} яблока")
#     else:
#         print("Саша не может унести яблоки и всё потерял")
#         sasha = 0
    
#     masha = int(input("Сколько яблок собрала Маша: "))
#     if masha <= 3:
#         print(f"Маша должна собрать ещё {3 - masha} яблока")
#     else:
#         print("Маша не может унести яблоки и всё потеряла")
#         masha = 0
#     if masha + sasha >= 8:
#         result = True
#         print(f"Компот готов и осталось {(sasha + masha)- 8} яблок")


guestList = []
guest = 0
while guest < 1:
    reg_guest = 0
    while reg_guest < 1:
        guestList.append(input("Укажите фамилию гостя для добавления в список: "))
        if len(guestList) <= 10 or len(guestList) < 0:
            guestList.append(input("Добавте гостя: "))
            if len(guestList) >= 5:
                guestList.remove(input(f"Укажите фамилию для удаления:\n{guestList} "))
                print(guestList)
    reg_guest = 1
        
            
        



