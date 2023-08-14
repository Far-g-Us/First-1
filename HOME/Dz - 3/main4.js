age = +prompt("Введите год для проверки:\n")
if ((age % 4) != 0) {
    console.log("Год обычный")
} else if ((age % 4) == 0) {
    if ((age % 100) != 0) {
        console.log("Год високостный")
    } else if ((age % 100) == 0) {
        if ((age % 400) != 0) {
            console.log("Год не високостный")
        } else {
            console.log("Год високостный")
        }
    }
}