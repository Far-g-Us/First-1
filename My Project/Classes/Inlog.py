class InLog():
    def __init__(self, login, password):
        self.login = login
        self.password = password
    def log_in_account(self,users_list):
        for i in range(len(users_list)):
            if users_list[i].login == self.login and users_list[i].password == self.password:
                print("вход выполнен")
                break
            elif i == len(users_list):
                print("Ошибка")