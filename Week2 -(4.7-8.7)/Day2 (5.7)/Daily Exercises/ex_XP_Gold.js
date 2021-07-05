		//EX1- The World Translator


let languge=prompt("What language do you speak? ");
languge=languge.toLowerCase();

if (languge=='french'){
	console.log("Bonjour");
}else if(languge=='english'){
	console.log("Hello");
}else if(languge=='hebrew'){
	console.log("Shalom");
}else{
	console.log("01110011 01101111 01110010 01110010 01111001");
}
//note: you guys think you're pretty funny don't you? "Sorry??" :D


			//EX2- The Grade Assigner
let grade=prompt("What is your Grade? ");

if(grade>90){
	console.log("A");
}else if((90>=grade)&&(grade>80)){
	console.log("B");
}else if((80>=grade)&&(grade>=70)){
	console.log("C");
}else if(70>grade){
	console.log("D");
}
//catch an incorrect input
else{
	console.log("incorrect input");
}


					//EX3- Verbing
let verb=prompt("Please enter a verb ");
//note: I cannot check if the input is an actual verb- I must assume totally correct input
//noteII: there are certain edge cases (example:swim->swimMing or run->runNing)- covering those edge cases IS possible but beyond the scope of this program
let verbsize=verb.length;


//first, we check that verb is larger or equal to 3
if(verbsize>=3){
	//now we search if 'verb' ENDS with 'ing' (i.e-for example 'sociolinguistics' will print normally)
	let isConfirmed=verb.includes("ing",verbsize-4);
	if(isConfirmed){
		//if 'verb' DOES end in 'ing'
		console.log(`${verb}ly`);
	}else{
		//if verb DOESN'T end with 'ing'
		console.log(`${verb}ing`);
	}
}
//if verb was SHORTER than 3 we simply print it
else{
	console.log(verb);
}






