#-------------Hw-3-#3----------------------------#
#Запросить у пользователя трехзначное и число и проверить,
#есть ли в нем одинаковые цифры.

zapros = int(input("Введите трёхзначное число на проверку:\n"))
num1 = int(zapros//100)
num2 = int((zapros//10) % 10)
num3 = int(zapros % 10)
if zapros >= 100 and zapros <= 999:
    if num1 == num2 and num1 == num3 and num2 == num3:
        print("В числе есть одинаковые числа")
    else:
        print("В вашем чмсле нет одинаковых чисел")
else:
    print("Вы ввели не трёхзначное число. Напишите трёхзначное число")