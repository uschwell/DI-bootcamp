let back = document.body.querySelectorAll("DIV")[0];
//console.log(back);

let att = document.createAttribute("style");
att.value = "background-color: blue; padding: 5px;";
back.setAttributeNode(att);

		//part 2,3
let myList=document.body.querySelectorAll("li");

let myHide =document.createAttribute("style");
myHide.value = "display: none";
let addBorder=document.createAttribute("style");
addBorder.value = "border: solid green 10px";

myList[0].setAttributeNode(myHide);
myList[1].setAttributeNode(addBorder);
//console.log(myList);


		//change the font size
let allBody=document.body;
let changeFont = document.createAttribute("style");
changeFont.value = "font-size: 25px;";
allBody.setAttributeNode(changeFont);