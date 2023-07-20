from Classes.client.Moderator import *
# class Admin имеет свойства и методы как у class Modarator, но имеет доп метод удаление/создания всех users и status admin, blocking наследуется от Modarator (false)
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