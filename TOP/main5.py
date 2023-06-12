# productList = ["Каша", "Вода"]
# print(productList[0])

# infoProduct = {
#     "nameprodict" : "Каша",
#     "price" : 120,
#     "sale" : 0.2,
# }


# print(infoProduct["price"], infoProduct["sale"])
# myName = input("Введи своё имя: ")
# myAge = int(input("Сколько вам лет?: "))
# infoPerson = {
#     "namePerson" : myName,
#     "agePerson" : myAge,
#     "hobbyPerson" : ["Спорт", "Programing"],
# }
# # print(infoPerson["hobbyPerson"][0])
# # print(infoPerson)

# for key in infoPerson:
#     print(f"{key} - {infoPerson[key]}")

# print(f"Имя пользователя {infoPerson['namePerson']}")

# productList = [
#     #0
#     {
#         "nameProduct" : "Хлеб",
#         "price" : 55,
#         "count" : 37,
#         "category" : "Хлебобулочное",
#     },
#     #1
#     {
#         "nameProduct" : "Молоко",
#         "price" : 101,
#         "count" : 20,
#         "category" : "Молочная",
#     },
#     #2
#     {
#         "nameProduct" : "Кефир",
#         "price" : 99,
#         "count" : 6,
#         "category" : "Молочная",
#     },
#     #3
#     {
#         "nameProduct" : "Мороженое",
#         "price" : 120,
#         "count" : 20,
#         "category" : "Молочная"
#     }
# ]
# for i in range(0, len(productList)):
#     if productList[i]["category"] == "Молочная":
#         productList[i]["price"] = productList[i]["price"] * 2
#         print(f"Название товара - {productList[i]['nameProduct']}")
#         print(f"Цена товара - {productList[i]['price']}")
#         print(f"Кол-во - {productList[i]['count']}")
#         print("----------------------------")

guestList = []
while True:
    nameGuest = input("Введите имя гостя: ")
    ageGuest = int(input("Введите возраст гостя: "))
    infoGuest = {
        "nameGuest" : nameGuest,
        "ageGuest" : ageGuest,
    }
    # print(infoGuest)
    guestList.append(infoGuest)
    if len(guestList) > 3:
        break

for i in range(0, len(guestList)):
    print(f"Имя гостя - {guestList[i]['nameGuest']}")
    print(f"Возраст гостя - {guestList[i]['ageGuest']}")
    print("------------------------------")
    