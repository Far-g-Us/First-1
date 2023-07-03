#-------------Hw-9-#5----------------------------#
# Написать программу входа и регистрации
# 1. регистрация пользователя, имя, фамилия, логин, пароль
# 2. данные записываются в объект
# 3. после подтверждения объект попадает в список зарегистрированных пользователей
# 4. + Сделать проверку на повторение логинов, если логин такой уже
# зарегистрирован, то предложить пользователю ввести другой
# 5. При входе проверять, логины и пароли, при неправильном вводе,
# вывести ошибку “Неверный логин или пароль”
# 6. После входа дать пользователю выбор
#   1. Посмотреть информацию
#   2. Выйти
#   3. + Редактирование данных, Имя, фамилия, пароль
#   4. + В списке зарегистрированных пользователей информация тоже
#   должна поменяться

userList = [] # Список пользователей

while True:
    x = int(input("Введите:\n1 - Регистрация нового пользователя\n2 - Вход в личный кабинет\n"))
    if x == 1: #цикл для регистрации пользователя
        print("-----Регистрация-----")
        while True:
            regUser = {
                "userLogin" : "",
                "userPassword" : "",
                "userName" : "",
                "userFirstName" : "",
            }
            while True:
                regLogin = input("Введите логин: ")
                if len(userList) > 0:
                    for i in range(0,len(userList)):
                        if regLogin != userList[i]["userLogin"]:
                            regUser["userLogin"] = regLogin
                        else:
                            print("Данный логин уже занят!\n Введите другой.")
                            regUser["userLogin"] = ""
                            break
                else:
                    regUser["userLogin"] = regLogin
                if len(regUser["userLogin"]) > 0:
                    break
            regUser["userPassword"] = input("Введите пароль нового пользователя: ")
            regUser["userName"] = input("Введите имя нового пользователя: ")
            regUser["userFirstName"] = input("Введите фамилию нового пользователя: ")
            print("Регистрация завершена")
            check = int(input("Выберите:\n1 - подтвердить\n2 - введите данные снова\n"))
            if check == 1:
                userList.append(regUser)
                break
            elif check == 2:
                print("-----Регистрация-----")
    elif x == 2:
        print("--Вход в ЛК--")
        inLogin = input("Введите логин: ")
        inPassword = input("Введите пароль: ")
        for i in range(0,len(userList)):
            if inLogin == userList[i]["userLogin"] and inPassword == userList[i]["userPassword"]:
                    print("Вход выполнен")
                    while True:
                        infoUser = int(input("1 - посмотреть информацию\n2 - редактировать информацию\n3 - выйти\n"))
                        if infoUser == 1:
                            print(f'Имя: {userList[i]["userName"]}\n',
                            f'Фамилия: {userList[i]["userFirstName"]}\n',
                            f'Логин: {userList[i]["userLogin"]}\n',
                            f'Пароль: {userList[i]["userPassword"]}\n')
                        elif infoUser == 2:
                            print("Редактированние данных")
                            upDate = int(input("1 - имя\n2 - фамилию\n3 - пароль\n"))
                            if upDate == 1:
                                print(f'Ваше имя {userList[i]["userName"]}')
                                userList[i]["userName"] = input("Новое имя: ")
                            elif upDate == 2:
                                print(f'Ваша фамилия {userList[i]["userFirstName"]}')
                                userList[i]["userFirstNaem"] = input("Новая фамилия: ")
                            elif upDate == 3:
                                print(f'Ваш пароль {userList[i]["userPassword"]}')
                                userList[i]["userPassword"] = input("Новый пароль: ")
                        elif infoUser == 3:
                            break
            elif len(userList) - 1 == i:
                print("Неверный логин или пароль")
