// console.log("########")
// let int = 1
// let str = "2"
// let float = true || false

// let minus = document.getElementById("minus")

// console.log(minus);
// console.log(minus);
// console.log(out);

// let h1 = document.querySelector("#h1");
// h1.innerHTML = "YandexMarket";

// let title = document.querySelector("title");
// title.innerHTML = "Home";

let munis = document.querySelector("#minus");
let plus = document.querySelector("#plus");
let out = document.querySelector("#out");


let i = 0;


function plusOut() {
    i++;
    out.innerHTML = i;
}

function minusOut() {
    i--;
    out.innerHTML = i;
}

plus.addEventListener("click", plusOut);
minus.addEventListener("click", minusOut);



let number1 = document.querySelector("#number1");
let number2 = document.querySelector("#number2");

let calcPlus = document.querySelector("#calcPlus");
let calcMinus = document.querySelector("#calcMinus");
let calcMul = document.querySelector("#calcMul");
let calcDiv = document.querySelector("#calcDiv");

let otvet = document.querySelector("#otvet");

function fPlus(){
    otvet.innerHTML = Number(number1.value) + Number(number2.value);
}
calcPlus.addEventListener("click", fPlus);

function fMinus(){
    otvet.innerHTML = Number(number1.value) - Number(number2.value);
}
calcMinus.addEventListener("click", fMinus);

function fMul(){
    otvet.innerHTML = Number(number1.value) * Number(number2.value);
}
calcMul.addEventListener("click", fMul);

function fDiv(){
    otvet.innerHTML = Number(number1.value) / Number(number2.value);
}
calcDiv.addEventListener("click", fDiv);


let body = document.body;

// body.style.backgroundColor = "green";



























// ["/r/jailbreak/"]