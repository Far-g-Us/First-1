#-------------Hw-3-#2----------------------------#
meters = int(input("Введите кол-во метров: "))

conv_miles = 0.0006213711922373
conv_inches = 39.37007874016
conv_yards = 1.093613298338

select = int(input("Выберите: 1 - метры в мили, 2 - метры в дюймы, 3 - метры в ярды "))
if select == 1:
    miles = meters * conv_miles
    print("%0.3f метров равно %0.3f мили" %(meters, miles))
elif select == 2:
    inches = meters * conv_inches
    print("%0.3f метров равно %0.3f дюймов" %(meters,inches))
elif select == 3:
    yards = meters * conv_yards
    print("%0.3f метров равно %0.3f ярдов" %(meters,yards))
else:
    print("Вы не выбрали ни один из вариантов")