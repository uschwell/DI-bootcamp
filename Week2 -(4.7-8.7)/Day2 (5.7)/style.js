//Practice

// let username="Mr Smith";
// let pass= 1234;

// let cart ={
// 	username: "Smith",
// 	password: "1234",
// 	isSignedIn: true,
// 	cart :{
// 		apple: 2,
// 		banana: 1,
// 		pear :5,
// 	},
// 	prices:{
// 		apple: 0.5,
// 		banana: 0.8,
// 		pear: 0.2,
// 	},
// };

// console.log(cart["username"]);
// console.log(cart["password"]);

// let numberPear= (cart["cart"]["pear"]);
// let pearPrice=(cart["prices"]["pear"]);
// let pearTotal= numberPear*pearPrice;
// console.log(pearTotal);




//Objects EX1

let user={
	username: "Mr Smith",
	password: 1234,

};

 // console.log(user["username"]);
 // console.log(user["password"]);

 let database=[user];
 // console.log(database);

let news1={
	username: "Aa",
	timeline: "misc",
};


let news2={
	username: "Bb",
	timeline: "misc",
};
let news3={
	username: "Cc",
	timeline: "misc",
};

let newsfeed=[news1,news2,news3];
console.log(newsfeed);