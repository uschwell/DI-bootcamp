const inputBox=document.getElementById('inputBox');
const fullText=document.getElementById('fullText');

//summary: we check each letter as it's entered. If its a LETTER then we add it to the 'header' where it is saved
//if input is NOT a letter-we warn the user and continue on
//we then reset the input box so we can repeat
function textOnly(){
	let currentLetter=inputBox.value;
	
	//console.log(`temp= ${currentLetter}`);
	//console.log(`inputBox= ${inputBox}`);
	//console.log(`fullText = ${fullText}`);

	let letters = /^[A-Za-z]+$/;
	 if(currentLetter.match(letters)){
	 	fullText.innerText+=(currentLetter);
     }
   else{
     	alert("That's not a letter!");
     }
     //we reset the input to blank
     inputBox.value="";
}