#-------------Hw-4-#1----------------------------#
#Пользователь вводит с клавиатуры два числа (начало и конец диапазона). 
#Требуется проанализировать все числа в этом диапазоне по следующему правилу: 
#если число кратно 7, его надо выводить на экран.
main1 = int(input("Введите число начала диапазона:\n"))
main2 = int(input("Введите число конца диапазона:\n"))

for i in range(main1, main2 + 1): 
    if (i%7 == 0):
        print(i)