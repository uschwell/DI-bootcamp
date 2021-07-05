						//EX1- Age Difference
let age1=prompt("User 1. What year were you born in? ");
let age2=prompt("User 2. What year were you born in? ");

age1= 2021-age1;
age2=2021-age2;
console.log(age1);
console.log(age2);
//we discover which one has the older age
let older;
let younger;
if(age1>age2){
	older=age1;
	younger=age2;
}else if(age2>age1){
	older=age2;
	younger=age1;
}else if(age2==age1){
	alert("You two are the same age!");
}else{
	//edge case- for incorrect inputs
	alert("Incorrect Input");
}

//now we confirm that our desired outcome is even possible
//note: no need for edge cases here- we have already confirmed correct inputs
if((older/2)<younger){
	alert("I'm sorry, you two are too close in age");
}else{
	let halfAge=(older-2*younger);
	console.log(`in exactly ${halfAge} years the younger of you will be half the age of the older`);
}
