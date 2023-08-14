zapros = +prompt("Введите трёхзначное число на проверку:\n")
num1 = (~~(zapros/100))
num2 = (~~(zapros/100)% 10)
num3 = (zapros % 10)
if (zapros >= 100 && zapros <= 999) {
    if (num1 == num2 && num1 == num3 && num2 == num3) {
        console.log("В числе есть одинаковые числа")
    } else {
        console.log("В вашем чмсле нет одинаковых чисел")
    }
} else {
    console.log("Вы ввели не трёхзначное число. Напишите трёхзначное число")
}