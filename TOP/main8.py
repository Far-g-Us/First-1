# def f1(a):
    # c = a - 50
    # print(c)
    # return c

# print(f1(100))


# myInfo = {

# }
# print(myInfo)
# #           myInfo
# def regName(massiv,newName):
# #   myInfo["myName"] = newName
#     massiv["myName"] = newName
#     return massiv

# def regGender(massiv):
#     x = int(input("1 - м\n2 - ж\n"))
#     if x == 1:
#         massiv["myGender"] = "м"
#     elif x == 2:
#         massiv["myGender"] = "ж"
#     return massiv

# def globalReg(massiv):
#     # massiv = myInfo
#     regName(massiv,input("Ваше имя"))
#     regGender(massiv)
#     print(massiv)
#     return massiv

# newInfo = globalReg(myInfo)
# print(newInfo)

num = {
    "myNum1" : ""
    "myNum2" : ""
    "myNum3" : ""
}

def addNum(massiv):
    myNum1 = int(input("Введите число1: "))
    myNum2 = int(input("Введите число2: "))
    myNum3 = int(input("Введите число3: "))
    return massiv

def sumNum(massiv):
    x = int(input("1 - сумма 1 и 3\n2 - сумма 2 и 3\n3 - сумма 1 и 2\n"))
    for i in range(0,len(num)):
        if x == "1":
            num[0] + num[2]
            massiv["sumNum1"]
            print(massiv["sumNum1"])
        elif x == "2":
            num[1] + num[2]
            massiv["sumNum2"]
            print(massiv["sumNum2"])
        elif x == "3":
            num[1] + num[2]
            massiv["sumNum3"]
            print(massiv["sumNum3"])
        return massiv
