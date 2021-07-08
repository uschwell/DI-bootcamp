
var leftNum='NaN';
var rightNum='NaN';
var operand="";

function number(num){
	if(leftNum=='NaN'){
		leftNum=num;
		console.log(`leftNum declared ${leftNum}`);
	}else{
		rightNum=num;
		console.log(`rightNum declared ${rightNum}`);
	}

}


function operator(operator){
	if(operand==""){
		operand=operator;
		console.log(`operand declared ${operand}`);
	}
}

function equal(){
	let temp=(`${leftNum}${operand}${rightNum}`);
	//console.log(`temp= ${temp}`);
	let equation=(eval(temp));
	console.log(`${equation}`);

}


//this function clears the latest entry (backspace)
function clear(){
	if(rightNum!='NaN'){
		rightNum='Nan';
	}else if(operand!= ""){
		operand="";
	}else if(leftNum!='Nan'){
		leftNum='Nan';
	}

}

//this function resets EVERYTHING
function reset(){
	var leftNum='NaN';
	var rightNum='NaN';
	var operand="";

}