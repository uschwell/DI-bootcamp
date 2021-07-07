

function tipCalc(price){
	let tip=0;
	if(price<50){
		tip=(price*0.2);
	}else if(50<=price<=200){
		tip=(price*0.15);
		//if we havent stopped anything else- we can assume the price was over $200
	}else{
		tip=(price*0.1);
	}

	//note: there are two ways to solve this exercise- we can print the desired outputs here and now
	//OR we can return the information and let John do with it what he wants- I will do BOTH
	console.log(`You should leave a $${tip} tip`);
	console.log(`Your final bill is ${price+tip}`);

	let toReturn={
		tipAmount: tip,
		finalBill: (tip+price)
	};
	return toReturn;
}

//this function call is enough when we console.log from inside the function
let cost = parseInt(prompt("How much did your meal cost? (In U.S Dollars please) "));
tipCalc(cost);

//this function call is what we need when we want to keep the results to ourselves
console.log("the 2nd method:");
let temp=tipCalc(cost);
console.log(temp);