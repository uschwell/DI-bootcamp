function isDivisible(divisor){
	console.log(`All numbers between 0 and 500 that evenly divide by ${divisor}`);
	let sum=0;
	for(let i=0;i<=500;i++){
		if((i%divisor)==0){
			console.log(i);
			sum+=i;
		}
	}
	console.log(`The sum of all those divisors is ${sum}`);

}

isDivisible(23);
// isDivisible(25);
// isDivisible(10);