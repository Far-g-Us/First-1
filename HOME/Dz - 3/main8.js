sk = Math.abs(+prompt("Введите сторону квадрата:"));
rk = Math.abs(+prompt("Введите радус круга:"));

if (sk / 2 / Math.PI > rk / 4 / 2) {
    alert("Войдёт");
} else {
    alert("Не войдёт")
}
