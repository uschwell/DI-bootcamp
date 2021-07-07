		//EX1-Information
		console.log("EX1");
		console.log("part I");
function infoAboutMe(argument) {
	console.log("This Function will talk a little bit about me:");
	console.log("I am a 28 year old Oleh from the United States");
	console.log("I will add more info later....");
}
infoAboutMe();


console.log("__________________________");
console.log("part II");


		//EX1-part II
function infoAboutPerson(personName, personAge, personFavoriteColor) {
	console.log("Your name is: "+personName);
	console.log("You are: "+personAge+" years old");
	console.log("Your favorite color is: " +personFavoriteColor);
}

infoAboutPerson("David", 45, "blue");
infoAboutPerson("Josh", 12, "yellow");

		//EX1-part III

console.log("__________________________");
console.log("part III");


function infoAboutPerson_Pt3(personName, personAge, personFavoriteColor, personHobbies){
	console.log("Your name is: "+personName);
	console.log("You are "+personAge+" years old");
	console.log("Your favorite color is " +personFavoriteColor);
	console.log('Your hobbies include: ');
	for(let i in personHobbies){
		console.log(personHobbies[i]);
	}

}

infoAboutPerson_Pt3("David", 45, "blue", ["tennis", "painting"]);
infoAboutPerson_Pt3("Josh", 12, "yellow", ["videoGame", "hanging out with friends", "playing cards"]);