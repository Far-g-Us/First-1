age = +prompt("Сколько вам лет:\n")
oblast_prov = age
if (oblast_prov >= 0 && oblast_prov <= 12) {
    console.log("Вы - ребёнок")
} else if (oblast_prov >= 12 && oblast_prov < 18) {
    console.log("Вы - подросток")
} else if (oblast_prov >= 18 && oblast_prov < 60) {
    console.log("Вы - взрослый")
} else if (oblast_prov > 60) {
    console.log("Вы - пенсионер")
} else {
    console.log("Неверно указан возраст")
}