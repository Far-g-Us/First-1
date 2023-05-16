# type_int = 1 #целые числа
# type_float = 1,23 #числа с точкой
# type_str = "Строки пишутся в кавычках" 
# type_bool_one = True #булево значение правда, истина 
# type_bool_two = False #булевы значение ложь
# type_none = None

# a = 123
# print(a *2, type(a))
# a = str(a)
# print(a *2, type(a))
# a = float(a)
# print(a *2, type(a))

# b = "123"
# print(b, type(b))
# b = int(b)
# print(b, type(b))

# c = int(input("Введите число - мы умножим его на 2: ")) #input() по умолчанию является строкой
# c = int(c) #из строки в число
# print(c *2, type(c))


#--------------------------------------------------------------#


# print("Заполните информацию")

# myName = input("Введите имя: ")
# print("Имя:", myName)

# myFamily = input("Введите фамилию: ")
# print("Фамилия:", myFamily)

# myAge = input("Введите ваш возраст: ")
# myAge = int(myAge)
# print("Возраст:", myAge)

# myCountry = input("Ваша страна: ")
# print("Страна:", myCountry)


#--------------------------------------------------------------#


# print("Заполните информацию")

# myName = input("Введите имя: ")
# myFamily = input("Введите фамилию: ")
# myAge = int(input("Введите ваш возраст: "))
# myCountry = input("Введите страну: ")

# print("Имя:", myName)
# print("Фамилия:", myFamily)
# print("Возраст:", myAge)
# print("Страна:", myCountry)


#----------------------------------------------------------------#


# myName = "Ден"
# print("Привет"+ " " + myName)
# print(f"Привет {myName}")
# print("Привет"," ","Ден")


#-----------------------------------------------------------------#


# z = int(input("Введите число: "))
# b = z//10
# c = z%10
# print(b)
# print(c)

# z =int(input("Введите число: "))
# x1 = z//100
# x2 = (z//10)%10
# x3 = z%10
# print(x1)
# print(x2)
# print(x3)
# c = x1+x2+x3
# print(c)

# x =int(input("Введите число: "))
# x1 = x%10
# print(x1)
# x = 123
# x2 = x%10
# print(x2)
# x = 12
# x3 = x%10
# print(x3)
# x = 1
# x4 = x%10
# print(x4)


#---------------------------------------------------------------------------#


# z =str(input("Введите 1 число: "))
# x =str(input("Введите 2 число: "))
# print(z + x)

z =str(input("Введите 1 число: "))
x =str(input("Введите 2 число: "))
c = z + x 
c = int(c)
print(c)