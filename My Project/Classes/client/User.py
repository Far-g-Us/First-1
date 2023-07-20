# class User - объект пользователя имеющий свои данные и свой функционал, может взаимодействовать только с самим собой, вводимые данные характерны для всех пользователей вне зависимости от статуса ("user","moderator","admin")
# status и blocking - постоянные значения при создании класса, могут быть изменены только class Moderator и Admin

class User():
    def __init__(self,user_id,first_name, last_name, birthday , gender, login, password):
       self.user_id = user_id
       self.first_name = first_name
       self.last_name = last_name
       self.birthday = birthday
       self.gender = gender
       self.login = login
       self.password = password
       #--------------------------
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
        if self.password == input("Введите старый пароль: "): # пример написания изменения информации
            self.password = new_password
