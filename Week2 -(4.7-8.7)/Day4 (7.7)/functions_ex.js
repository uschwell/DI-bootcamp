		//EX1
function myAge(age){
	console.log("My Mothers age is: "+(age*2));
	console.log("My Fathers age is: "+(age*2*1.2));
}

let age= prompt("what is my age again? ");

myAge(age);


		//EX2

function myAge2(age2){
	//return my Mothers age
	return (age2*2);
}

let ageInput2=prompt("what's my age?");
let motherAge=myAge2(ageInput2);
console.log("Again, my Mothers age is: "+motherAge);