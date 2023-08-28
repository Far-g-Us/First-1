// let main1 = parseInt(prompt("Введите число начала диапазона: "));
// let main2 = parseInt(prompt("Введите число конца диапазона: "));
let main1 = +prompt("Введите число начала диапазона: ");
let main2 = +prompt("Введите число конца диапазона: ");

for (let i = main1; i <= main2; i++) {
    if (i % 7 === 0) {
        console.log(i);
    }
}
