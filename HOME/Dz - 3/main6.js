let summa = Math.abs(+prompt("Введите сумму USD для обмена: "));
const eur = Number(1.08);
const uan = Number(0.15);
const azn = Number(0.59);
let rate = "";
do {
  rate = prompt(
    "На какую валюту вы хотите обменять доллары? Введите EUR для обмена на евро, UAN для обмена на юани, либо AZN для азербайджанских манатов."
  );
  rate = rate.toUpperCase();
} while (rate != "EUR" && rate != "UAN" && rate != "AZN");
let convert_summa = 0;
if (rate == "EUR") {
  convert_summa = (summa * eur).toFixed(2);
}
if (rate == "UAN") {
  convert_summa = (summa * uan).toFixed(2);
}
if (rate == "AZN") {
  convert_summa = (summa * azn).toFixed(2);
}