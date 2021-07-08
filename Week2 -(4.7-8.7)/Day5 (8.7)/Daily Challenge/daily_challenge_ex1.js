function bottlesOfBeer(num){

	let currentNum=num;
	let subtract=1;
	let bottlesRemoved=0;
	console.log(`${currentNum} bottles of beer on the wall ${currentNum} bottles of beer Take 1 down, pass it around ${currentNum-1} bottles of beer on the wall`);
	bottlesRemoved++;
	subtract++;

	while(num>(bottlesRemoved+subtract)){
		//currentNum exists merely for ease of writing. It is remade every loop (and I could just as easily write (num-bottlesRemoved) every time)
		currentNum=(num- bottlesRemoved);
		console.log(`${currentNum} bottles of beer on the wall ${currentNum} bottles of beer Take ${subtract} down, pass them around ${currentNum-subtract} bottles of beer on the wall`);
		//we INCREMENT how many bottles of beer we've already drunk
		bottlesRemoved+=subtract;
		//we increment subtract
		subtract++;
	}
	//we only reach the final stanza as soon as we need to remove either the last bottles OR if the bottles remaining are less than the amount we need to remove
	currentNum=(num- bottlesRemoved);
	console.log(`${currentNum} bottles of beer on the wall ${currentNum} bottles of beer Take them all down, pass them around NO more bottles of beer on the wall`);

}


//note:it was my understanding that for this function we were not allowed to DECREASE the amount of beers we had, but we WERE
//allowed to INCREASE values. so we simply kept increasing the amount of beers that we have already drunk.

let beers=prompt("How many bottles of beer are on the wall?");
bottlesOfBeer(beers);
