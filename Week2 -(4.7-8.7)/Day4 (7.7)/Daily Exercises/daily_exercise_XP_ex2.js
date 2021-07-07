		//EX2

function checkDriverAge(driverAge){
	if(driverAge==18){	
		console.log("Congratulations on your first year of driving. Enjoy the ride!");
	} else if(driverAge>18){
		console.log("You are old enough to drive, Powering On. Enjoy the ride!");

	}else if(driverAge<18){
		console.log("Sorry, you are too young to drive this car. Powering off");
	}else{
		//print this for incorrect input
		console.log("I'm sorry could you repeat that?");
	}

}

let ageInput=prompt("What is your age?");
//we convert the input (string) into an integer-we assume legitimate inputs
let ageInt=parseInt(ageInput);
checkDriverAge(ageInput);


