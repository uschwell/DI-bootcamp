
//input our sentence and parse into an Array
let input=prompt("Give us a few words, separeated by commas",",");
let array=input.split(",");
//now we must find the longest word
let longest=0;
for(let i in array){
	if(array[i].length>longest){
		longest=((array[i]).length);
	}

}

//now we print our top line
let x="*";
console.log(x.repeat(longest+2));
let space= " ";

//since the first word has no preceding whitespace-we must manually add an extra space
let extra=(longest-array[0].length-1);
console.log(`* ${array[0]}${space.repeat(extra)}*`);

//now we print the other lines
for(let y=1;y in array;y++){
	extra=(longest-array[y].length);
	console.log(`*${array[y]}${space.repeat(extra)}*`);
}

//finally we print our bottom line
console.log(x.repeat(longest+2));