#-------------Hw-14-#1----------------------------#
# С ПОМОЩЬЮ ЦИКЛОВ и ФУНКЦИЙ
# СОЗДАТЬ json ПРИГЛАШЕННЫХ ГОСТЕЙ НА МЕРОПРИЯТИЕ ФУНКЦИОНАЛ
# 1. Метод добавления в список (указать только имя гостя) после ввода вернуться в выбор методов
# 2. Метод удаления гостя (по номеру или по имени) + этот гость улетает в блэк лист
# 3. Просмотр гостей
# 4. Если гостей больше 5 и меньше 10, то предложить пользователю закончить цикл
# Нельзя приглашать более 10 гостей и не меньше
# 5. Доп задание - Создать массив с именами тех людей которых нельзя приглашать + хорошее оформление + Комментарии

import json

guest_list = []
blacklist = ["John", "Jane", "Alex", "Olivia"] # Массив имен гостей, которых нельзя приглашать

def add_guest():
    name = input("Введите имя гостя: ")
    guest_list.append(name)
    print("Гость успешно добавлен!")

def remove_guest():
    choice = input("Выберите способ удаления гостя:\n1. По номеру\n2. По имени\n")
    if choice == "1":
        index = int(input("Введите номер гостя для удаления: "))
        if index < len(guest_list):
            guest = guest_list.pop(index)
            blacklist.append(guest)
            print(f"Гость {guest} успешно удален и добавлен в блэк лист!")
        else:
            print("Ошибка: введенный номер гостя не существует.")
    elif choice == "2":
        name = input("Введите имя гостя для удаления: ")
        if name in guest_list:
            guest_list.remove(name)
            blacklist.append(name)
            print(f"Гость {name} успешно удален и добавлен в блэк лист!")
        else:
            print("Ошибка: введенное имя гостя не найдено.")
    else:
        print("Ошибка: неверный выбор!")

def view_guests():
    if len(guest_list) > 0:
        print("Список гостей:")
        for i, guest in enumerate(guest_list):
            print(f"{i}. {guest}")
    else:
        print("Список гостей пуст.")

def invite_guest():
    while len(guest_list) < 10:
        if len(guest_list) >= 5 and len(guest_list) < 10:
            choice = input("У вас уже достаточно гостей. Хотите завершить приглашение? (да/нет)\n")
            if choice.lower() == "да":
                break
            add_guest()

def main():
    while True:
        print("\nВыберите метод:\n1. Добавление гостя\n2. Удаление гостя\n3. Просмотр гостей\n4. Приглашение гостей\n5. Выход")
        choice = input("Введите номер метода: ")

        if choice == "1":
            add_guest()
        elif choice == "2":
            remove_guest()
        elif choice == "3":
            view_guests()
        elif choice == "4":
            invite_guest()
        elif choice == "5":
            break
        else:
            print("Ошибка: неверный выбор!")

with open("guests.json", "w") as file:
    json.dump(guest_list, file)

print("Данные сохранены в файл guests.json.")

if __name__ == "__main__":
    main()
