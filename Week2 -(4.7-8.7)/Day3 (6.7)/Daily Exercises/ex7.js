let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
//declare array here-we will need it later
var semiFinal=names;

//first, we sort all the names into alphabetical order
names=names.sort();

for(let i in names){
	let temp=Array.from(names[i]);
	//note: the names are sorted according to javascript values- therefore upperCase characters will ALWAYS precede lowerCase characters
	sortedTemp= (temp.sort());
	//add the first letter from the sorted names to an overall array
semiFinal[i]=sortedTemp[0];
}
//finally we combine the first letters of the alphabetized names into one final name
console.log(semiFinal);


//note: an interesting point. Since the names are all alphabetized by javascript AND javascript automatically places an
//uppercase letter before a lowercase one. A simpler method for this problem would be: alphabetize the original array,
// and then take the FIRST (uppercase) letter from each. I assumed that this method was not in the spirit of the exercise