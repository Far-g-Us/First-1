# class Manager():
#     def __init__(self,reg,inlog,userModerAdmin,datalist):
#         self.reg = reg 
#         self.inlog = inlog
#         self.userModerAdmin = userModerAdmin
#         self.datalist = datalist
#     def work(self):
#         print(self)

from .client.User import *
from .client.Moderator import *
from .client.Admin import *
from .sign.Inlog import *
from .sign.Registration import *
