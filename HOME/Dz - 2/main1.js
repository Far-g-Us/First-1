x = +prompt("Введите число: ")
y = +prompt("Введите число: ")
z = +prompt("Введите число: ")

numbers = +prompt("Выберите: \n1 - сложение \n2 - умножение")
if (numbers == 1) {
    console.log(x+y+z)
} else if (numbers == 2) {
    console.log(x*y*z)
} else {
    console.log("Вы не выбрали ни один из вариантов")
}