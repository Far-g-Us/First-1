let palindrom = 0;

do {
    palindrom = Math.abs(
        +prompt("Введите пятизначное число для проверки: ")
    );
} while (palindrom < 10000 || palindrom > 99999);
let pal = [];
for (i = 0; i < 5; i++) {
    pal[i] = palindrom % 10;
    palindrom = Math.trunc(palindrom / 10);
};
if (pal[0] == pal[4] && pal[1] == pal[3]) {
    alert("Число палиндром");
} else {
    alert("Число не палиндром");
};