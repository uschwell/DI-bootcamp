let Quarters  = 0.25
let Dimes = 0.10
let Nickels = 0.05
let Pennies = 0.01

function changeEnough(wallet, price){
	let sum=0;
	//I create a local array of values- not sure if I was allowed to create an object to reference globally here
	let values=[Quarters, Dimes, Nickels, Pennies];
	//we take our wallet, and multiply each coin AMOUNT by that coins VALUE- the total is added to 'sum'
	for(i in wallet){
		sum+=(values[i]*wallet[i]);
	}

	//now we check if we have enough money
	if(sum>=price){
		return true;
	}else{
		return false;
	}
}


//note: this function (as ordered) will ONLY return a true/false statement. It will NOT print anything. If you wish to display the result you will need to save/print it elsewhere
changeEnough([25, 20, 5, 0], 4.25);

//example:
console.log(changeEnough([0, 0, 20, 5], 0.75)); //<----will print "true"
console.log(changeEnough([2, 100, 0, 0], 14.11));//<---will print "false"