#-------------Hw-10-#1----------------------------#
# 1. Закомментировать данный код
# 2. Задание объекты хранят имя и статус клиента
# Написать код, который будет удалять объекты
# если у клиента статус “не оплачен” то удалить его из списка



# numberList = [1,2,3,4,5,6,7,8,9,22,11,10,6,5,22]
# def delNumber(massiv):
#     print("вошел", massiv, "кол-во",len(massiv) )
#     for i in range(0,len(massiv)):
#         if i == len(massiv):
#             return massiv
        
#         elif massiv[i] % 2 == 0 :
#             massiv.pop(i)
#             print("вышел", massiv)
#             delNumber(massiv)

# delNumber(numberList)

clientList = [
    {
    "clientName" : "Alex",
    "paymentStatus" : "paid"
    },
    {
    "clientName" : "John",
    "paymentStatus" : "not paid"
    },
    {
    "clientName" : "Jax",
    "paymentStatus" : "not paid"
    },
    {
    "clientName" : "Jerax",
    "paymentStatus" : "paid"
    }
]

def numClient(massiv):
    print(massiv)
    for i in range(0,len(massiv)):
        if i == len(massiv):
            return massiv
        elif massiv[i]["paymentStatus"] == "not paid":
            massiv.pop(i)
            print("BAN", massiv)
            numClient(massiv)

numClient(clientList)