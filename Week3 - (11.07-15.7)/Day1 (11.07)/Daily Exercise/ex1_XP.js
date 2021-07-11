
		//EX1-part 1
let nav= document.getElementById("navBar");
nav.setAttribute("id","socialNetworkNavigation");
// console.log(nav);


		//EX1-part 2
let newList= nav.children[0];

let node = document.createElement("LI");
let textnode = document.createTextNode("Logout");
node.appendChild(textnode);
newList.appendChild(node);

// console.log(newList);

		//EX1-part3
let firstList=newList.firstElementChild;
let lastList=newList.lastElementChild;
// console.log(firstList);
// console.log(lastList);