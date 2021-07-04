console.log("EX2");

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
//remove the requested array from moreFruits
let myTemp= moreFruits[1];
//extract the desired array from myTemp
myTemp= myTemp[1];
//Finally, extract and print to console the desired value from
//our final sub-Array
console.log(myTemp[0]);