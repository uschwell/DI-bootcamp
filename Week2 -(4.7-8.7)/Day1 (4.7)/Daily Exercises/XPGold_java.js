console.log("EX1");

let me = ["my","favorite","color","is","blue"];
console.log(me.join());


//Note: the challenge said to slice off the FIRST two characters- while your example showed a switching of the LAST
//two. I did the former (note: doing the latter would be even simpler- just use a pop())
console.log("EX2");
let str1 = "mix";
let str2 = "pod";

//slice off the first letter of str1 and graft it onto the last 2 letters of str2 (and vice versa)
let temp1=(str2.slice(0,1)+ str1.slice(1,3));
let temp2=(str1.slice(0,1)+ str2.slice(1,3));;


// console.log(temp1);
// console.log(temp2);

console.log(`${temp1} ${temp2}`);






console.log("EX3");
var num1 = prompt("Please enter a number");
var num2 = prompt("Please enter a second number");

alert(parseInt(num1)+parseInt(num2));