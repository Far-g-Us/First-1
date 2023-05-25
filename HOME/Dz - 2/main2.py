#-------------Hw-2-#2----------------------------#
x = int(input("Введите число: "))
y = int(input("Введите число: "))
z = int(input("Введите число: "))
m = [x,y,z]
numbers = int(input("Выберите: 1 - максимум из трёх, 2 - минимум из трёх, 3 - среднеарифметическое из трёх "))
if numbers == 1:
    b = max(m)
    print(m)
elif numbers == 2:
    b = min(m)
    print(b)
elif numbers == 3:
    if y < x < z or z < x < y:
        print('Среднее:', x)
    elif x < y < z or z < y < x:
        print('Среднее:', y)
    else:
        print('Среднее:', z)
else:
    print("Вы не выбрали ни один из вариантов")


# if numbers == 1:
#     m = x
#     if m < y:
#         m = y
#     if m < z:
#         m = z
#     print(m)
# elif numbers == 2:
#     m = [x, y, z]
#     b = min(m)
#     print(b)