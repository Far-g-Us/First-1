# for i in range(1,10):
#     for j in range(1,10):
#         print(i, j)

# import time
# for h in range(0, 24):
#     for m in range(0, 60):
#         for s in range(0, 60):
#             print(f"ч:{h} м:{m} с:{s}")
#             time.sleep(1/10)

# h = 0
# while h < 24:
#     m = 0
#     while m < 60:
#         s = 0
#         while s < 60:
#             print(f"ч:{h} м:{m} с:{s}")
#             s = s + 1
#         m = m + 1
#     h = h + 1

#--------------------------------------------------------------------------#
#Использование циклов внутри циклов
print("Регистрация персонажа")
reg = 0
while reg < 1:
    reg_gender = 0
    while reg_gender < 1:
        gender = input("Выберите пол персонажа:\n 1-муж\n 2-жен\n: ")
        if gender == "1":
            gender = "Мужской"
            reg_gender+=1
        elif gender == "2":
            gender = "Женский"
            reg_gender+=1
        else:
            print("Выберите из перечисленного")
        if reg_gender == 1:
            reg_race = 0
            while reg_race < 1:
                race = input("Выберите расу персонажа:\n 0<-Назад\n 1-человек\n 2-эльфы\n: ")
                if race == "1":
                    race = "Человек"
                    reg_race+=1
                elif race == "2":
                    race = "Эльф"
                    reg_race+=1
                elif race == "0":
                    reg_gender = 0
                    break
                else:
                    print("Выберите из перечисленного")
                if reg_race == 1:
                    reg_role = 0
                    while reg_role < 1:
                        role = input("Выберите расу персонажа:\n 0<-Назад\n 1-маг\n 2-воин\n: ")
                        if role == "1":
                            role = "Маг"
                            reg_role+=1
                        elif role == "2":
                            role = "Воин"
                            reg_role+=1
                        elif role == "0":
                            reg_race = 0
                            break
                else:
                    print("Выберите из перечисленного")
    print(f"ваш пол - {gender}, ваша раса - {race}, ваш класс - {role}")
    reg+= 1