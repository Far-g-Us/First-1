main1 = +prompt("Введите число начала диапазона: ");
main2 = +prompt("Введите число конца диапазона: ");


console.log("Все числа диапазона:");
for (let i = main1; i <= main2; i++) {
    console.log(i);
}

console.log("Все числа диапазона в убывающем порядке:");
for (let i = main2; i >= main1; i--) {
    console.log(i);
}

console.log("Все числаб кратные 7:");
for (let i = main1; i <= main2; i++) {
    if (i % 7 === 0) {
        console.log(i);
    }
}

let count = 0;
for (let i = main1; i <= main2; i++) {
    if (i % 5 === 0) {
        count++;
    }
}
console.log("Количество чисел, кратных 5:" + count);
