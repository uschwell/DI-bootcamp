console.log("Hello World!!!");

let addressNumber=5;
let addressStreet="Ben Yehudah";
let country="Israel";
let email= "genericEmail@gmail.com"

let global_address =`I live in  ${addressStreet} ${addressNumber}  in ${country}`;
// display(global_address);
console.log(global_address);
console.log(`The length of ${country} is- ${country.length}`)
console.log(email.includes("@"));
console.log(email.indexOf("@"));


let myAge=28;
let futureYear=2030;
let temp =((futureYear-2021)+myAge);
console.log("Ex2");
console.log(`I will be ${temp} in ${futureYear}`);


console.log("Arrays");
let pets= ['cat','dog','fish','rabbit','cow'];
console.log(pets[1]);
let tempPets= pets.splice(3,1,'horse');
// console.log(pets);
// console.log(tempPets);
console.log(pets.length);




// MODAL EXAMPLES


// alert("Hello");

// let age = prompt('How old are you?', 20);
// alert(`You are ${age} years old!`); // You are 20 years old!


// let isBoss = confirm("Are you the boss?");
// alert(`Youre the boss! ${isBoss}`); // true if OK is pressed



console.log(false - true);