#-------------Hw-3-#7----------------------------#
#Запросить у пользователя сумму покупки и вывести сумму к оплате со скидкой: 
#от 200 до 300 – скидка будет 3%, от 300 до 500 – 5%, от 500 и выше – 7%.

summ = int(input("Введите сумму покупки для вычисления скидки:\n"))
if summ>=200 and summ<300:
    print(f"Ваша скидка составляет 3%. Заплатите - {summ*0.97}")
elif summ>=300 and summ<500:
    print(f"Ваша скидка составляет 5%. Заплатите - {summ*0.95}")
elif summ>=500:
    print(f"Ваша скидка составлет 7%. Заплатите - {summ*0.93}")