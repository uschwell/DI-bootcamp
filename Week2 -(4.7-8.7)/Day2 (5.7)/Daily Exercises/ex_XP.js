				//EX1- Simple If/Else Statement

let x=5;
let y=3;

if(x>y){
	console.log("x is the bigger number");
}else if (y>x){
	console.log("y is the bigger number");
}
//"else"- assuming input IS an actual integer then we only reach here IF x==y
else if(x==y){
	console.log("x and y are equal");
}
//final else to catch all excetions (i.e x,y not integers, compatible)
else{
	console.log("error: incorrect input");
}

				//EX2- Chihuahua
var newDog="Chihuahua";
//print the strings length, in upperCase and in lowerCase 
console.log(newDog.length);
console.log(newDog.toLowerCase());
console.log(newDog.toUpperCase());

//check if the string is Chihuahua and output accordingly
if(newDog == 'Chihuahua'){
	console.log("I love Chihuahuas, it’s my favorite dog breed");
}else{
	console.log("I dont care, I prefer cats");
}


				//EX3- Even Or Odd
var userInput=prompt("Please enter a number ");
//check if the input is even/odd or if the user did NOT enter a number
if(userInput%2==0){
	console.log(`${userInput} is an even number`)
}else if(userInput%2==1){
	console.log(`${userInput} is an odd number`)
}else{
	console.log("incorrect input, please try again");
}

			
			//EX4- Group Chat
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let userAmount=users.length;
//check how many users we have and output accordingly
if(userAmount==0){
	console.log("no one is online");
}else if(userAmount==1){
	console.log(`${users[0]} is online`);
}else if(userAmount==2){
	console.log(`${users[0]} and ${users[1]} is online`);
}else if(userAmount>2){
	console.log(`${users[0]}, ${users[1]} and (${userAmount-2}) more users are online`);
}