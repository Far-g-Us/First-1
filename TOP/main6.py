# def f1(a):
    # c = a - 50
    # print(c)
    # return c

# print(f1(100))


# myInfo = {

# }
# print(myInfo)
# #           myInfo
# def regName(massiv,newName):
# #   myInfo["myName"] = newName
#     massiv["myName"] = newName
#     return massiv

# def regGender(massiv):
#     x = int(input("1 - м\n2 - ж\n"))
#     if x == 1:
#         massiv["myGender"] = "м"
#     elif x == 2:
#         massiv["myGender"] = "ж"
#     return massiv

# def globalReg(massiv):
#     # massiv = myInfo
#     regName(massiv,input("Ваше имя"))
#     regGender(massiv)
#     print(massiv)
#     return massiv

# newInfo = globalReg(myInfo)
# print(newInfo)




#----------------------------------------------------------------------------#

# num = {
#     "myNum1" : ""
#     "myNum2" : ""
#     "myNum3" : ""
# }

# def addNum(massiv):
#     myNum1 = int(input("Введите число1: "))
#     myNum2 = int(input("Введите число2: "))
#     myNum3 = int(input("Введите число3: "))
#     return massiv

# def sumNum(massiv):
#     x = int(input("1 - сумма 1 и 3\n2 - сумма 2 и 3\n3 - сумма 1 и 2\n"))
#     for i in range(0,len(num)):
#         if x == "1":
#             num[0] + num[2]
#             massiv["sumNum1"]
#             print(massiv["sumNum1"])
#         elif x == "2":
#             num[1] + num[2]
#             massiv["sumNum2"]
#             print(massiv["sumNum2"])
#         elif x == "3":
#             num[1] + num[2]
#             massiv["sumNum3"]
#             print(massiv["sumNum3"])
#         return massiv
 
#-----------------------------------------------------------------------#

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
