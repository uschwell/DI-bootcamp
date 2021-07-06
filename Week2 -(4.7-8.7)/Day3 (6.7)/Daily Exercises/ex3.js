
var input=1000;
do{
	input=prompt("Please enter a number smaller than 10", 10000);
	//parse the input into a number (I assume correct input)
	inputNum=parseInt(input);

}
while(inputNum>10);
console.log("thank you! Have a nice day!");