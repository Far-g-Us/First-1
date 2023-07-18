class Registration():
    def create_user(self,users_list):
        users_list.append({
        "first_name" : input(),
        "last_name" : input(),
        "birthday" : input(),
        "gender" : input(),
        "login" : input(),
        "password" : input()
    },)