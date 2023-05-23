nameGame = "Подземелья"
print("Добро пожаловать \n 'Подземелья'")


print("Выберите пол персонажа:\n", "ж-женский\n", "м-Мужской")
gender = str(input("Введите ж или м :\n"))
if gender == "М" or gender == "м":
  gender = "Мужской"
elif gender == "Ж" or gender == "ж":
  gender = "Женский"
print(f"Вы выбрали {gender} пол")

print("Выберете расу персонажа ч-человек,\n э-эльф")
race = str(input("Введите ч или э:\n"))
if race == "ч" or race == "Ч":
  race = "Человек"
elif race == "э" or race == "Э":
  race = "Эльф"
  
  print(f"Вы выбрали рассу {race}")

if race == "Человек":
  scoreRole = 0  # галочка для выбора класса
  print("Выберете класс:\n", "1-Воин", "2-Лучник", "3-Жрец", "4-Маг")
  role = input("введите 1,2,3 или 4 для выбора класса:")
  if role == "1":
    role = "Воин\n"
  elif role == "2":
    role = "Лучник\n"
  elif role == "3":
    role = "Жрец\n"
  elif role == "4":
    role = "Маг\n"

elif race == "Эльф":
    print("Выберете класс:\n", "1-Воин\n", "2-Лучник\n", "3-Темный Колдун\n",
          "4-Паладин\n")
    role = input("введите 1,2,3 или 4 для выбора класса")
    if role == "1":
      role = "Воин"
    elif role == "2":
      role = "Лучник"
    elif role == "3":
      role = "Темный Колдун"
    elif role == "4":
      role = "Паладин"
print(f"Вы выбрали класс:{role}")

name = str(input("Введите имя вашего персонажа"))
print("\nИнформация о персонаже:\n"
        f"пол персонажа {gender}\n"
        f"Раса персонажа {race}\n"
        f"Класс:{role}\n"
        f"Имя:{name}\n")

