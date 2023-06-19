#-------------Hw-8-#1----------------------------#
#Написать программу входа и регистрации
#	1.регистрация пользователя, имя, фамилия, логин, пароль
#	2.данные записываются в объект
#	3.после подтверждения  объект попадает в список зарегистрированных пользователей
#	4.+ Сделать проверку на повторение логинов, если логин такой уже зарегистрирован, то предложить пользователю ввести другой
#	5.При входе проверять, логины и пароли, при неправильном вводе, вывести ошибку “Неверный логин или пароль”
#	6.После входа дать пользователю выбор
#       1. Посмотреть информацию Имя, Логин, фамилия, пароль
#		2. Выйти
#		3. + Редактирование данных, Имя, фамилия, пароль
 #      4. + В списке зарегистрированных пользователей информация тоже должна поменяться

registered_users = []

class User:
    def __init__ (self,first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

def register():
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    username = input("Введите логин: ")
    password = input("Введите пароль: ")
    for user in registered_users:
        if user.username == username:
            print("Такой логин уже зарегистрирован. Попробуйте другой.")
            return
    new_user = User(first_name, last_name, username, password)
    registered_users.append(new_user)
    print("Регистрация успешна.")

def login():
    username = input("Введите логин: ")
    password = input("Введите пароль: ")
    for user in registered_users:
        if user.username == username and user.password == password:
            return user
    print("Неверный логин или пароль.")
    return None

def edit_profile(user):
    print("Ваш профиль:")
    print(f"Имя: {user.first_name}")
    print(f"Фамилия: {user.last_name}")
    print(f"Логин: {user.username}")
    print(f"ПАроль: {user.password}")
    print("\n1.Изменить имя")
    print("2.Изменить фамилию")
    print("3.Изменить пароль")
    print("4.Назад")

    choice = input("Введите номер действия: ")
    if choice == "1":
        new_first_name = input("Введите новое имя: ")
        user.first_name = new_first_name
    elif choice == "2":
        new_last_name = input("Введите новую фамилию: ")
        user.last_name = new_last_name
    elif choice == "3":
        new_password = input("Введите новый пароль: ")
        user.password = new_password
    elif choice == "4":
        return

def user_menu(user):
    while True:
        print("\nМеню.")
        print("1.Посмотреть профиль")
        print("2.Выйти")
        print("3.Редактировать профиль")
        choice = input("Введите номер дейстивия: ")
        if choice == "1":
            print("Ваш профиль:")
            print(f"Имя: {user.first_name}")
            print(f"Фамилия: {user.last_name}")
            print(f"Логин: {user.username}")
            print(f"ПАроль: {user.password}")
        elif choice == "2":
            break
        elif  choice == "3":
            edit_profile(user)

def main():
    while True:
        print("\n1.Регистрация")
        print("2.Вход")
        print("3.Выход")
        choice = input("Введите номер действия: ")
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                user_menu(user)
        elif choice == "3":
            break
if __name__ == "__main__":
    main()