
					//EX1

// for(let i=0;i<=15;i++){


// 	if((i%2)==0){
// 		console.log(+i + " is an even number");
// 	}else{
// 		console.log("I'm sorry but " +i+ " is not an even number");
// 	}

// }


					//EX2-part 1
	let names= ["john", "sarah", 23, "Rudolf",34];
	let i=0;
	let length=names.length;
	while(i<length){
		if(typeof(names[i])=='string'){
		let word=names[i];
		let c=names[i].charAt(0);
		if(c!=c.toUpperCase()){
			c=c.toUpperCase();
			word=(c+word.slice(1, word.length));
			names[i]=word;
			console.log(names[i]);
			}
		}
		i++;
	}


			//EX2-part 2 (note: will use the previous array)
	for(let i in names){
		if(typeof(names[i])=='string'){
			console.log(names[i]);
		}else{
			break;
		}
	}







				//InClass -sum of array
// let prices = [20, 12, 5, 4, 2];
// let sum=0;
// for(let i in prices){
// 	sum+=prices[i];
// }
// console.log("The sum of all prices is "+sum);

