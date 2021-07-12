
		//part 1
var article=document.body.getElementsByTagName("ARTICLE")[0];
var lastArticle=article.getElementsByTagName("p");
article.removeChild(lastArticle[3]);
// console.log(lastArticle);




		//part 2
//let temp=document.getElementsByTagName("ARTICLE");
let temp2= document.getElementsByTagName("H2")[0];

//console.log(temp2[0]);
temp2.addEventListener("click", function(){
		temp2.style.backgroundColor="green";
});


		//part 3 -we can reuse code from the previous section
let randomSize= document.getElementsByTagName("H1")[0];
randomSize.style.fontSize=(Math.floor(Math.random() * 101));

		//part 4-with reusing of 'temp' from part 2
let hideH3= document.getElementsByTagName("H3")[0];
 //console.log(hideH3);
hideH3.addEventListener("click", function(){
		hideH3.style.display="none";
});

		//part 5
function makeBold(){
	//reuse the already found nodes from part 1
	for(let i=0; i<3; i++){
		lastArticle[i].style.fontWeight = "900";
	}
}

		//part 6
function submitted(event){
	event.preventDefault();
	let parentForm=document.body.getElementsByTagName("form");
	//let inputForm=parentForm.getElementsByTagName()
	console.log(parentForm);
	console.log(parentForm[0]);
	
	let inputs=parentForm[0].getElementsByTagName("input");
	console.log(inputs);
	let tag1=parentForm[0].getElementByType("text");
	let tag2=parentForm[0].getElementByType("text");
	console.log(tag1);
	console.log(tag2);
}