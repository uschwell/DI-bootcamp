							//InClass Part 1 (commented out for work on Part 2)

// let userCart = {
// 	username : "John",
// 	password: 1234,
// 	isUserSignedIn : true,
// 	cart : {
// 		apple : 2,
// 		banana : 1,
// 		pear : 5
// 	},
// 	prices : {
// 		apple : 0.5,
// 		banana : 0.8,
// 		pear : 0.2
// 	}
// };
// userCart["username"] = "Josh";
// // console.log(userCart);
// // console.log(userCart["cart"]["pear"]);
// // console.log(userCart["prices"]["pear"]);
// // let numberPear = userCart["cart"]["pear"];
// // let pricePerPear = userCart["prices"]["pear"];
// // let totalPricePear = numberPear * pricePerPear;
// // alert(`The pears cost ${totalPricePear} shekels to ${userCart["username"]}`)

// console.log(`the price of a pear is ${userCart["prices"]["pear"]}`);

// userCart["prices"]["pear"]=(userCart["prices"]["pear"])*1.17;
// console.log(`the price of a pear (with tax) is ${userCart["prices"]["pear"]}`);


// var fruit = window.prompt("Which fruit do you want? ");
// fruit=fruit.toLowerCase();
// // console.log(userCart["cart"][`${fruit}`]);
// // console.log(userCart["prices"][`${fruit}`]);
// var actualPrice= (userCart["cart"][`${fruit}`])*(userCart["prices"][`${fruit}`]);
// alert(`That will cost you ${actualPrice}`);


			//InClass part 2

//InClass 2-part 1
let userCart = {
	username : "John",
	password: 1234,
	isUserSignedIn : true,
	cart : {
		apple : 2,
		banana : 1,
		pear : 5
	},
	prices : {
		apple : 0.5,
		banana : 0.8,
		pear : 0.2
	}
};
//add a new key/value to the userCart Object
userCart["lastname"] = "Smith";


//we check if the user is signed in-if so, we show him his name and password
if(userCart["isUserSignedIn"]){
	console.log(`${userCart["username"]} `);
	console.log(`${userCart["password"]}`);
}else{
	console.log("you need to sign in");
}


//InClass 2- part 2 and part 3
//change the password/username
userCart["username"]="Sammy"
userCart["password"]=123456;

//actual code that checks
if((userCart["username"]=="John")&&(userCart["password"]==1234)){
	alert("You are signed in");
}else if((userCart["username"]=="John")||(userCart["password"]==1234)){
	alert("One credential is false");
}else{
	alert("you need to sign in");
}

