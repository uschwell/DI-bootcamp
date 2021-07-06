let people = ["Greg", "Mary", "Devon", "James"];

//remove Greg- step 1
people.shift();

//replace James with Jason-step 2
for(let i in people){
	if(people[i]=='James'){
		people[i]='Jason';
	}
}

//add my name- step 3
people.push("Uriel");

//console.log the array-step 4
 for(let i in people){
 	console.log(people[i]);
 }

//console.log the array until Jason-step 5
  for(let i in people){
 	console.log(people[i]);
 	if(people[i]=='Jason'){
 		break;
 	}
 }

console.log(people);
 //slice out Mary and my name (Uriel)- step 6
 let tempSlice= people.slice(1,3);
 console.log(tempSlice);

//find the index of 'Mary'- step 7
 	let x=people.indexOf("Mary");
 	console.log(x);

 //code that looks for Foo- step 8
 //code returns "-1" because 'Foo' doesn't exist in the array and -1 is the return value for 'failed' (no other way to receive -1 return in THIS function)
 console.log(people.indexOf("Foo"));

 //console.log of "last" which equals the final variable in the array- step 9
 let last=people.length;
 last=people[last-1];
 console.log(last);