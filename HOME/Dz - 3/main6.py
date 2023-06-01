#-------------Hw-3-#6----------------------------#
#Написать конвертор валют. Пользователь вводит количество USD, выбирает, в какую валюту хочет перевести: 
#EUR, UAN или AZN, и получает в ответ соответствующую сумму.

# 1-Вариант
usd = float(input("Введите то кол-во USD которое хотите конвертировать:\n"))
conv_usd = usd
conv_eur = 0.93634
conv_uan = 7.12
conv_azn = 1.7
select = int(input("Выберите в какую валюту конвертировать:\n 1 - EUR\n 2 - UAN\n 3 - AZN\n"))
if select == 1:
    s = conv_eur*conv_usd
    print("Сумма перевода из USD в EUR составляет",'{:.2f}'.format(s))
elif select == 2:
    s = conv_uan*conv_usd
    print("Сумма перевода из USD в UAN составляет",'{:.2f}'.format(s))
elif select == 3:
    s = conv_azn*conv_usd
    print("Сумма перевода из USD в AZN составляет",'{:.2f}'.format(s))
else:
    print("Ошибка, написано неправильное число")


# 2-Вариант
usd = float(input("Введите кол-во USD:\n"))
select = int(input("Выберите валюту для конвертации:\n 1 - EUR\n 2 - UAN\n 3 - AZN\n"))
if select == 1:
    eur = usd*0.93634
    print("EUR -"'{:.2f}'.format(eur))
elif select == 2:
    uan = usd*7.12
    print("UAN -"'{:.2f}'.format(uan))
elif select == 3:
    azn = usd*1.7
    print("AZN -"'{:.2f}'.format(azn))
else:
    print("Введено неправильное число")