// Ошибка в нахождении по пути 8 - 21
x = +prompt("Введите число: ")
y = +prompt("Введите число: ")
z = +prompt("Введите число: ")
m = [x,y,z]

numbers = +prompt("Выберите: \n1 - максимум из трёх \n2 - минимум из трёх \n3 - среднеарифметическое из трёх")
if (numbers == 1) {
    b = max(m)
    console.log(b)
} else if (numbers == 2) {
    b = min(m)
    console.log(b)
} else if (numbers == 3) {
    if (y < x < z || z < x < y) {
        console.log(x)
    } else if (x < y < z || z < y < x) {
        console.log(y)
    } else {
        console.log(z)
    }
} else {
    console.log("Вы не выбрали ни один из вариантов")
}