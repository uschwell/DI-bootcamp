						//Part II
//this function will be called from the 'onclick' in the html file and handle running part II
function testManager(){
	let click=confirm("Would you like to play a game?");
	//we prompt for an initial input
	//if they DID click 'OK'
	if(click){
		let entered=prompt("Please enter a number between 0 and 10", "");
		//we check/convert the input to an integer
		entered=checkInput(entered);
		//check the integer
		if((entered>10)||(entered<0)){
			alert("Sorry it’s not a good number, Goodbye");
		}
		//this else is the case in which: a number WAS entered AND it was 0<=number<=10
		else{
			let generatedNum=playTheGame_2();
			//we now run the 'test' function
			test(entered, generatedNum);
		}
	}
	//this 'else' is reached if they clicked 'Cancel' at the beginning
	else{
		alert("No problem, Goodbye");
	}

}


function  test(userNumber,computerNumber){
	let counter=0;
	while(counter<3){
		console.log(`round: ${counter}`);

		//we correctly guess the number- we are done
		if(userNumber==computerNumber){
			alert("WINNER!");
			break;
		}else if(userNumber>computerNumber){
			userNumber=prompt("Your number is bigger then the computer’s, guess again");

		}else if(userNumber<computerNumber){
			userNumber=prompt("Your number is smaller then the computer’s, guess again");
		}
		//if we found the answer, we have broken the loop already, otherwise we will need to try a new input
		userNumber=checkInput(userNumber);
		//increment the loop
		counter++;
	}
	//in case we 'timed out' on tries
	if(counter>=3){
		alert("out of chances");
	}
}


//much of this code is copy pasted from part 1- simply altered to no longer be a stand-alone function
function playTheGame_2(){
			//randomly generate a number between (including) 0 and 10
			let num=(Math.random(10)*10);
			//round the number to the nearest int
			num=Math.round(num);
			//we return the generated random number
			return num;
}


//this function receives an input (either an integer or a string) and will NOT end until it has received input of an integer
//it will return the integer
function checkInput(enteredInput){
		//we try to turn the input into an integer
		enteredInput=parseInt(enteredInput);
		//we keep asking until we receive a permitted input 
		while(isNaN(enteredInput)){
			enteredInput=prompt("I'm sorry that is not a number. Please enter a number between 0 and 10");
			enteredInput=parseInt(enteredInput);
		}

		//we return the eventual integer
		return enteredInput;
}