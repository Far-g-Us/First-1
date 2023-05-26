#1-й вариант
# x = int(input())
# if x % 4 != 0:
#     print("Обычный")
# elif x % 100 == 0:
#     if x % 400 == 0:
#         print("Високостный")
#     else:
#         print("Обычный")
# else:
#     print("Високостный")
#
#2-й вариант
# x = int(input())
# if x % 4 != 0 or (x % 100 == 0 and x % 400 != 0):
#     print("Обычный")
# else:
#     print("Високостный")


#--------------------------------------------------------------#

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# if a + b <= c or a + c <= b or b + c <= a:
#     print("Треугольник не существует")
# elif a != b and a != c and b != c:
#     print("Разносторонний")
# elif a == b == c:
#     print("Равносторонний")
# else:
#     print("Равнобедренный")

#-----------------------------------------------------------------#

# myName = "Alex"
# start = int(input("Введите начальное значение: "))
# end = int(input("Введите конечное значение: "))
# for i in range(0, 5, 2):  # 0 начало цикла, 5 конец, 2 шаг#
#     print(myName, i)

#------------------------------------#

# myName = "Alex"
# start = int(input("Введите начальное значение: "))
# end = int(input("Введите конечное значение: "))
# for i in range(start, end + 1):
#     print(i)

#------------------------------------#

# myName = "Alex"
# for i in range(0, 2 + 1):
#     print(i)

# for i in myName:
#     print(i)
#     if i == "e":
#         break

# myName = "Alex"
# for i in range(0, 29):
#     if i % 2 !=0:
#         print(i)

# a = 2
# b = 3
# if a + b == 5:
#     for i in range(0,10):
#         print((a+b)*i)

#------------------------------------#

# x = int(input("Введите число на проверку простого числа:\n"))
# for i in range (2,x+1):
#     print(f"делим число {x} на {i}")
#     print(f"остаток {x % i}")
#     if x % i == 0 and x != i:
#         print("Число сложное")
#         break
#     elif i == x:
#         print("Число простое")

#------------------------------------#

# x = int(input("Выводите числа, кратные шести. Назначьте точку окончания вывода\n"))
# for i in range(0, x + 1):
#     if i % 7 == 0 and i % 2 == 0:
#         print(i)

#------------------------------------#

# y = int(input("Для какого числа вывести таблицу умножения\n"))
# print(f"Таблица умножения для числа {y}:")
# for i in range(1, 10):
#     print(f"{i} x {y} = {y*i}")

# sum = 0
# for i in range(0,10):
#     sum = sum + i
#     print(sum)

#------------------------------------#

# i = 0
# b = 10
# while i < 10 and b > 0:
#     print(i)
#     print(b)
#     i = i + 1
#     b = b - 3

# i = 0
# b = 10
# while i != 11 and i < 100:
#     print(i)
#     i = i + 23

#------------------------------------#

# i = 0
# b = 10
# print("Первый цикл")
# while True:
#     print(12)
#     i = i + 1
#     if i > 10:
#         break

# print("Второй цикл")
# x = True
# while x == True:
#     print(i)
#     i = i + 1
#     if i > 15:
#         x = False

#------------------------------------#

# myName = "Alex"
# print(len(myName))
# i = 0
# while i < len(myName):
#     print(i)
#     i+=1

#------------------------------------#

n = int(input("Введите число для расчёта факториала:\n"))
faktor = 1
while n > 1:
    faktor *= n
    n -= 1
print(faktor)

# hhos = int(input("Введите число для расчёта факториала:\n"))
# faktor = 1
# i = 1
# while i <= hhos:
#     faktor = faktor * i
#     i = i + 1
# print(faktor)

#-----------------------------------------------------------------#