
				//Part I:
//note: the function has been slightly altered to align more smoothly with the bonus portion
function playTheGame(){
	let click=confirm("Would you like to play a game?");
	//if they DID click 'OK'
	if(click){
		let entered=prompt("Please enter a number between 0 and 10", "");
		//we try to turn the input into an integer
		entered=parseInt(entered);
		//if the input is incorrect..... No longer needed- I did the 'Bonus' option
		// if(isNaN(entered)){
		// 	console.log("Sorry Not a number, Goodbye");
		// }

		//we keep asking until we receive a permitted input 
		while(isNaN(entered)){
			entered=prompt("I'm sorry that is not a number. Please enter a number between 0 and 10");
			entered=parseInt(entered);
		}

		if((entered>10)||(entered<0)){
			alert("Sorry it’s not a good number, Goodbye");
		}
		//this else is the case in which: a number WAS entered AND it was 0<=number<=10
		else{
			//randomly generate a number between (including) 0 and 10
			let num=(Math.random(10)*10);
			//round the number to the nearest int
			num=Math.round(num);

			// console.log(`entered= ${entered}`);
			// console.log(`created= ${num}`);

			//we print "correct" if the two numbers match
			if(entered==num){
				console.log("Correct");
			}
		}
	}
	//this 'else' is in case they clicked 'Cancel'
	else{
	alert("No problem, Goodbye");
	}
}
