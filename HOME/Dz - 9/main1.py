# Вывести на экран, карточку пользователя заполнить(Имя, Фамилия, возраст, год
# рождения). Вывести в одном print через префикс “f”.

userList = []
while True:
    print("-----Регистрация-----")
    while True:
        regUser = {
            "userName" : "",
            "userFirstName" : "",
            "userAge" : "",
            "userYearBirth" : "",
        }
        while True:
            regUser["userName"] = input("Введите имя: ")
            regUser["userFirstName"] = input("Введите фамилию: ")
            regUser["userAge"] = input("Введите возраст: ")
            regUser["userYearBirth"] = input("Введите год рождения: ")
            print("Регистрация завершена")
            userList.append(regUser)
            break
        for i in range(0,len(userList)):
                    print(f'Имя: {userList[i]["userName"]}\n',
                      f'Фамилия: {userList[i]["userFirstName"]}\n',
                      f'Логин: {userList[i]["userAge"]}\n',
                      f'Пароль: {userList[i]["userYearBirth"]}\n')
        break
    break

            

