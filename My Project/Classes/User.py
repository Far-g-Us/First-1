# class User - объект пользователя имеющий свои данные и свой функционал, может взаимодействовать только с самим собой, вводимые данные характерны для всех пользователей вне зависимости от статуса ("user","moderator","admin")
# status и blocking - постоянные значения при создании класса, могут быть изменены только class Moderator и Admin

class User():
    def __init__(self,user_id,first_name, last_name, birthday , gender, login, password) :
       self.user_id = user_id
       self.first_name = first_name
       self.last_name = last_name
       self.birthday = birthday
       self.gender = gender
       self.login = login
       self.password = password
       #-----------------------
       self.status = "user"
       self.blocking = False

    # Если в классе есть методы с словом update, значит этот метод для изменения информации
    def update_first_name(self, new_first_name):
        self.first_name = new_first_name
        print(f"новое имя : {self.first_name}")
    def update_last_name(self, new_last_name):
        self.last_name = new_last_name
    def update_birthday(self, new_birthday):
        self.birthday = new_birthday
    def update_gender(self, new_gender):
        self.gender = new_gender
    def update_password(self, new_password):
        if self.password == input("Введите старый пароль: "):
            self.password = new_password

# class Moderator имеет свойства и методы как у class User, но имеет доп метод блокировки users и status moderator , blocking наследуется от User (false) 
class Moderator(User):
    def __init__(self, user_id, first_name, last_name, birthday, gender, login, password):
        super().__init__(user_id, first_name, last_name, birthday, gender, login, password)
        self.status = "moderator"
    # блокировка пользователей
    def blocking_user(self, users_list):
        text_user_list = f"id | first_name | blocking | status \n"
        for i in range(0,len(users_list)):
            text_user_list += f"{users_list[i].user_id}  {users_list[i].first_name}  {users_list[i].blocking} {users_list[i].status}\n"
        print(text_user_list)
        input_user_id = int(input("Введите id пользователя для блокировки"))
        for i in range(0,len(users_list)):
            if self.status == "moderator":
                if input_user_id == i and users_list[i]['status'] != "moderator" and users_list[i]['status'] != "admin":
                    if users_list[i]['blocking'] == True:
                        print("пользователь уже заблокирован")
                        break
                    else:
                        users_list[i]['blocking'] = True
                        print("пользователь успешно заблокирован")
                        break
            elif self.status == "admin":
                if input_user_id == i:
                    if users_list[i]['blocking'] == True:
                        print("пользователь уже заблокирован")
                        break
                    else:
                        users_list[i]['blocking'] = True
                        print("пользователь успешно заблокирован")
                        break
# class Admin имеет свойства и методы как у class Modarator, но имеет доп метод удаление/создания всех users и status admin , blocking наследуется от Modarator (false)
class Admin(Moderator):
    def __init__(self, user_id, first_name, last_name, birthday, gender, login, password):
        super().__init__(user_id, first_name, last_name, birthday, gender, login, password)
        self.status = "admin"
    def delete_user_list(self, users_list):
        users_list.clear()
        print("База данных пуста")
                                # massiv - массив данных
    def create_user_list(self, massiv, users_list):
        for i in range(0,len(massiv)):
            users_list.append(User(user_id=i+1, 
                                first_name=massiv[i]["first_name"],
                                last_name=massiv[i]["last_name"],
                                birthday=massiv[i]["birthday"],
                                gender=massiv[i]["gender"],
                                login=massiv[i]["login"],
                                password=massiv[i]["password"]))