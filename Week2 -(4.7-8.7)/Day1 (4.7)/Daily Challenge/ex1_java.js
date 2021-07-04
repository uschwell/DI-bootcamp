console.log("EX1");

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
// remove Bananna
let tempFruits= fruits.slice(1);

//sort tempFruits Alphabetically
tempFruits.sort();
//add "Kiwi"
tempFruits.push("Kiwi");
//Remove "Apples" from the start of the array
tempFruits.shift();

//Finally, reverse the current string and print it to console
tempFruits.reverse();
console.log(tempFruits);