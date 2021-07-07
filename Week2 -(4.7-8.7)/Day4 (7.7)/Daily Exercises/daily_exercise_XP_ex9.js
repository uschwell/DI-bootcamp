// 			//Part I
function hotelCost(nights){
		//we take the raw input and try to convert it into an integer
		let thisNights=parseInt(nights);
		//if the input is incorrect we keep asking until we get a correct input
		while((isNaN(thisNights))||(thisNights==0)){
			thisNights =prompt("I'm sorry, could you repeat that? How many nights will you be staying with us?","");
			thisNights=parseInt(thisNights);
		}
		let totalCost=(nights*140);
		//note: same as in EX_8 I am BOTH printing the result here AND returning the final cost
		//(feel free to comment-out whichever is not needed/wanted)
		//console.log(`Thank you, the total price will be $${totalCost}`);
		return totalCost;
	}


//let nights =prompt("How many nights will you be staying with us?");
//we both call the function AND print the result
//console.log(hotelCost(nights));


		//Part II
function planeRideCost(){
	let ticketPrice=300;
	let destination= prompt("Welcome, what is your destination?", "");
	while((destination=="")&&(typeof(destination)=='string')){
		destination=prompt("I'm sorry, could you repeat that? Welcome, what is your destination?", "")
	}
	//note: the relevant names ARE Case-sensitive
	if(destination=="London"){
		ticketPrice=183;
	}else if(destination=="Paris"){
		ticketPrice=200;
	}

	 //note: same as in EX_8 I am BOTH printing the result here AND returning the final cost
 	//(feel free to comment-out whichever is not needed/wanted)
	//console.log(`The price of your ticket will be $${ticketPrice}`);
	return ticketPrice;
}

//planeRideCost();




		//Part III
function rentalCarCost(days){
		//we take the raw input and try to convert it into an integer
		days=parseInt(days);
		//if the input is incorrect we keep asking until we get a correct input
		while(isNaN(days)){
			days =prompt("I'm sorry, could you repeat that? How many days do you want the car for?");
		}
		let totalCost=(days*40);
		if(days>10){
			totalCost=(totalCost*0.95);
		}
		//note: same as in EX_8 I am BOTH printing the result here AND returning the final cost
		//(feel free to comment-out whichever is not needed/wanted)
		//console.log(`Thank you, the total price will be $${totalCost}`);
		return totalCost;
	}

	// let days=prompt("How many days do you want to rent the the car for?");
	// rentalCarCost(days);



		//Part IV
	function totalVacationCost(){
		let hotelPrice =prompt("How many nights will you be wanting a hotel for?");
		hotelPrice=rentalCarCost(hotelPrice);
		let planePrice=prompt("Where would you like to travel to?");
		planePrice=planeRideCost(planePrice);
		let rentalCarPrice=prompt("How many days will you be wanting to rent a car for?")
		rentalCarPrice=rentalCarCost(rentalCarPrice);

		let totalVacationPrice=(hotelPrice+planePrice+rentalCarPrice);
		console.log(`Thank you for your patience the total cost of your vacation is $${totalVacationPrice}`);
		console.log(`Price Breakdown:`);
		console.log(`Hotel: ${hotelPrice}`);
		console.log(`Plane Ticket: ${planePrice}`);
		console.log(`Car Rental: ${rentalCarPrice}`);

	}

	totalVacationCost();