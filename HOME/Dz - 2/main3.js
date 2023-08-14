meters = +prompt("Введите кол-во метров:\n")

conv_miles = 0.0006213711922373
conv_inches = 39.37007874016
conv_yards = 1.093613298338

select = +prompt("Выберите:\n 1 - метры в мили \n 2 - метры в дюймы \n 3 - метры в ярды\n")
if (select == 1) {
    miles = meters * conv_miles
    console.log(miles)
} else if (select == 2) {
    inches = meters * conv_inches
    console.log(inches)
} else if (select == 3) {
    yards = meters * conv_yards
    console.log(yards)
} else {
    console.log("Вы не выбрали ни один из вариантов")
}