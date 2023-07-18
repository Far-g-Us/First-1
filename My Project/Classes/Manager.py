class Manager():
    def __init__(self,reg,inlog,userModerAdmin,datalist):
        self.reg = reg 
        self.inlog = inlog
        self.userModerAdmin = userModerAdmin
        self.datalist = datalist
    def work(self):
        print(self)