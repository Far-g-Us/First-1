#-------------Hw-3-#1----------------------------#
#Запросить у пользователя его возраст и определить, кем он
#является: ребенком (0–2), подростком (12–18), взрослым
#(18_60) или пенсионером (60– ...).

age = input("Сколько вам лет?\n")
if str.isdigit(age):
    oblast_prov = int(age)
    if oblast_prov >= 0 and oblast_prov <= 12:
        print("Вы - ребёнок")
    elif oblast_prov >= 12 and oblast_prov < 18:
        print("Вы - подросток")
    elif oblast_prov >= 18 and oblast_prov < 60:
        print("Вы - взрослый")
    elif oblast_prov >= 60:
        print("Вы - пенсионер")
    else:
        print("Неверно указан возраст")
else:
    print ("Ошибка, введите возраст снова, используя только цифры.")