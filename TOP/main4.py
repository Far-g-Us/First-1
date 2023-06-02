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

    # numberList[i] = numberList[i]**2
    # if numberList[i] % 2 !=0:
    #     numberList.pop(i)
# print(numberList)

# listN = [ [1, 2, 3, 4, 5], 
#           [6, 7, 8, 9, 10],
#         ]
# for i in range(0, len(listN)):
#     print(listN[i])
#     for j in range(0, len(listN[i])):
#         print(listN[i][j])

genderList = ["Мyжской", "Женский"]
raceList = ["Человек", "Эльф", "Гном", "Орк", "Таурен", "Тёмный эльф"]
roleList = ["Воин", "Лучник", "Маг"]

textRace = ""
for i in range (0, len(raceList)):
    textRace += f"{i} - {raceList[i]}\n"
reg_race = False #создали галочку - (нет)
while reg_race == False: # выполнять пока не совпадёт (False)
    # принимает только число
    myRace = int(input(f"Выберите расу:\n{textRace}"))
    if myRace > len(raceList) or myRace < 0:
        print("Ошибка: выбери из перечисленного")
    else:
        for i in range(0, len(raceList)):
            if myRace == i:
                myRace = raceList[i]   # race = raceList[i]
                reg_race = True
                print("Вы выбрали:",myRace)
                break
                
    
textGender = ""
for i in range (0, len(genderList)):
    textGender += f"{i} - {genderList[i]}\n"
reg_gender = False
while reg_gender == False:
    myGender = int(input(f"Выберите пол:\n{textGender}"))
    if myGender > len(genderList) or myGender < 0:
        print("Ошибка: выберите из перечисленного")
    else:
        for i in range (0, len(genderList)):
            if myGender == i:
                myGender = genderList[i]   # gender = genderList[i]
                reg_gender = True
                print("Вы выбрали:",myGender)
                break


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

