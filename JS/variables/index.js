
// variable declaration with initialization
var a = 10; // global
let b = 20; // 
const c = 30; // cannot be re-assigned, cannot be re-declared

// not possible
//c = 50 // re-assignment

//'const' declarations must be initialized
// you can't declare const variable without value.
// const d;

// you can't re-assign const variable
//c = 40;

let name2;
const name3 = "Basith"; 
if (true) {
    let myLet = "Let variable"
    var myVar = "var variable"
    const myConst = "const variable"
    name2 = "meeran";
    console.log(name3);
}


// block scope.
/* 
if() {
}
for() {
}
function myFun() {
} 
while() {
}
*/

console.log(name2);
console.log(myVar);
console.log(name3);

// let and const variable is block scope. You can't use it outside of block scope.
// console.log(myConst);
// console.log(myLet);


//// var - global variable - like public drive or shared drive
var h1 = 100;
h1 = 500;
//console.log("l1 : ", l1);


// const and let are block scope.

//// const - values cannot be changed
const c1 = 30; // cannot be re-assigned, cannot be re-declared
// not possible
//c1 = 50 // re-assignment


//// let - values can be changed
let l1 = 30; // can be re-assigned
l1 = 50 // re-assignment

//console.log("l1 : ", l1);



/// Assignments
let y = 10;
y += 10; // y = y + 10;
y -= 10; // y = y - 10;
y *= 10; // y = y * 10;
console.log("y :" + y);