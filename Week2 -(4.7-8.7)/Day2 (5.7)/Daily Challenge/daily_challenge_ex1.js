let sentence='The movie is not that bad, I like it';
//let sentence='This movie is not so bad !';
//let sentence='This dinner is bad !';

//we search our sentence for the desired substrings
let wordnot=sentence.search("not");
let wordbad=sentence.search("bad");

//note: if 'bad' exists and 'not' doesn't we get a (wordbad>wordnot)~~(num>-1)- we output accordingly
if((wordbad!=(-1))&&(wordnot==(-1))){
	console.log(sentence);
}
//check if the word 'not' comes before the word 'bad'
else if(wordbad>wordnot){
	let slice1=sentence.slice(0,wordnot);
	let slice2=sentence.slice(wordbad+3);
	console.log(`${slice1} good${slice2}`);
}
//else if 'bad' comes before 'not' (they cannot be equal-its a sentence!)
else{
	console.log(sentence);
}
