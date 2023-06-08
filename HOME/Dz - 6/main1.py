print("Регистрация персонажа")
reg = 0
while reg < 1:
    reg_gender = 0
    while reg_gender < 1:
        gender = input("Выберите пол персонажа:\n 1-Муж\n 2-Жен\n")
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
                race = input("Выберите расу персонажа:\n 1 - Человек\n 2 - Эльфы\n 0 - Назад\n")
                if race == "1":
                    race = "Человек"
                    reg_race+=1
                    reg_role = 0
                    while reg_role < 1:
                        role = input("Выберите класс персонажа:\n 1 - Лучник\n 2 - Воин\n 0 - Назад\n")
                        if role == "1":
                            role = "Лучник"
                            reg_role+=1
                        elif role == "2":
                            role = "Воин"
                            reg_role+=1
                        elif role == "0":
                            reg_race = 0
                            break
                        else:
                            print("Выберите из перечисленного")
                elif race == "2":
                    race = "Эльф"
                    reg_race+=1
                    while reg_role < 1:
                        role = input("Выберите класс персонажа:\n 1 - Маг\n 2 - Воин\n 0 - Назад\n start - В начало\n")
                        if role == "1":
                            role = "Маг"
                            reg_role+=1
                        elif role == "2":
                            role = "Воин"
                            reg_role+=1
                        elif role == "0":
                            reg_race = 0
                            break
                        elif role == "start":
                            reg_gender = 0
                            break
                elif  race == "0":
                    reg_gender = 0
                    break
                else:
                    print("Выберите из перечисленного")
    print(f"ваш пол - {gender}, ваша раса - {race}, ваш класс - {role}")
    reg+=1