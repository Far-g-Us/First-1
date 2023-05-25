#-------------Hw-2-#1----------------------------#
x = int(input("Введите число: "))
y = int(input("Введите число: "))
z = int(input("Введите число: "))

numbers = int(input("Выберите: 1 - сложение, 2 - умножение "))
if numbers == 1:
    print(x+y+z)
elif numbers == 2:
    print(x*y*z)
else:
    print("Вы не выбрали ни один из вариантов")