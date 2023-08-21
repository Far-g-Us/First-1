let res = Number(0);
alert(
    "Какая кнопка справа от кнопки «N»?"
);
let question_a = confirm("M или m?");
let question_b = confirm("J или j?");
let question_c = confirm("C или с?");
if (question_a == true) {
    res += 2;
}
alert(
    "Какая кнопка слева от кнопки «К»?"
);
question_c = confirm("G или g?");
question_a = confirm("J или j?");
question_b = confirm("X или x?");
if (question_a == true) {
    res += 2;
}
alert(
    "Какая кнопка справа от кнопки «Z»?"
);
question_a = confirm("O или o?");
question_b = confirm("S или s?");
question_c = confirm("X или x?");
if (question_c == true) {
    res += 2;
}
if (res > 0) {
    alert(
      `Вы близки к провалу! ${(res /= 2)} неправильных ответа и ${res} штрафных балла!`
    );
  } else {
    alert("0 штрафных баллов, поздравляем!");
  }