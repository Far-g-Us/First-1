#-------------Hw-2-#1----------------------------#
x = int(input("Введите число: "))
y = int(input("Введите число: "))
z = int(input("Введите число: "))

numbers = int(input("Выберите: \n1 - сложение \n2 - умножение"))
if numbers == 1:
    print(x+y+z)
elif numbers == 2:
    print(x*y*z)
else:
    print("Вы не выбрали ни один из вариантов")