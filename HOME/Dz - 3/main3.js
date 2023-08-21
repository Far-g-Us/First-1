let a = prompt("Введите трехзначное целое число: ");
let arr = a.split("");
let count = 0;
if (arr[0] == arr[1]) {
  count++;
}
if (arr[0] == arr[2]) {
  count++;
}
if (arr[1] == arr[2]) {
  count++;
}
if (count == 1) {
  count++;
}
alert(`Обнаружено ${count} одинаковых цифры`);