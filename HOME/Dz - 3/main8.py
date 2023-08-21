#-------------Hw-3-#8----------------------------#
#Запросить у пользователя длину окружности и периметр квадрата. 
#Определить, может ли такая окружность поместиться в указанный квадрат.

# import math
# lengthOfCircle = int(input("Введите длину окружности:\n"))
# perimeterOfSquare = int(input("Введите периметр квадрата:\n"))
# if perimeterOfSquare/4>lengthOfCircle/math.pi:
#     print("Круг помещается в квадрат")
# else:
#     print("Круг не помещается в квадрат")
import math

c = float(input("Введите сторону квадрата: "))
r = float(input("Введите радус круга: "))
if (c / 2 / math.pi > r / 4 / 2):
    print("Войдёт")
else:
    print("Не войдёт")
# print('Войдёт!'if c * 2 ** (0.5) < 2 * r else 'Не войдёт')
