// console.log(2+2*2);
// let int = 1;
// let str = "1";
// let bool = true || false;
// let massiv = [1,2,3,4,5,6];
// let obj = {
//     "name" : "name",
//     "age" : 22,
// }
// class Auto{
//     constructor(name,age){
//         this.name = name;
//         this.age = age;
//     }
//     changeName(){
//         console.log(this.name)
//     }
// }
// class AutoV2 extends Auto{
//     constructor(name,age){
//         this.name = name;
//         this.age = age;
//     }
// }

// function sum(a,b){
//     return a + b
// }

// let sum2 = (a,b) => {
//     return a + b
// }
// console.log(5/0)

// // let x = prompt("Введите ваше имя"); // строка
// // let y = +prompt("введите только число"); // число +
// // console.log(x,y)

// let i = 0;

// while(i < 10){
//     i++;
//     console.log(i)
// }

// for(let i = 0; i < 10; i++){
//     console.log(i)
// }

// let z = 1;
// let k = 2;

// if(z < k){
//     console.log("z < k")
// }
// else if(k < z){
//     console.log("k < z")
// }
// else if(k == z){
//     console.log("k = z")
// }
// else{
//     console.log("ошибка")
// }

// let hi = "hisdasdsadsad"
// console.log(`${hi} adsdsaas`)
// console.log(hi + " adsdsaas")

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