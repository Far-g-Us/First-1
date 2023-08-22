let button = document.querySelector("#button");

function solve() {
    let a = Number(document.getElementById("a").value);
    let b = Number(document.getElementById("b").value);
    let c = Number(document.getElementById("c").value);
    
    let discriminant = b * b - 4 * a * c;

    if (discriminant > 0) {
        let x1 = (-b + Math.sqrt(discriminant)) / (2 * a);
        let x2 = (-b + Math.sqrt(discriminant)) / (2 * a);
        document.getElementById("discriminant").innerHTML = discriminant;

        document.getElementById("x1").innerHTML = x1;
        document.getElementById("x2").innerHTML = x2;
    } else if (discriminant === 0) {
        let x = -b / (2 * a);
        document.getElementById("discriminant").innerHTML = "Единственный корень уравнения: x = " + x;
    } else {
        document.getElementById("discriminant").innerHTML = "Уравнение не имеет корней";
    }
}
