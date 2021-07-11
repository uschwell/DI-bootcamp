		//EX2-part1
//we find the two lists
let bothlists=document.body.querySelectorAll("ul.list");

//we select the 0-th list
let myList=bothlists[0];
console.log(myList);

//we get the actual <li> and change its inner text
let nameList=myList.lastElementChild;
nameList.innerHTML="Richard";


			//EX2-part2
//we select the 1st element of both lists and replace them with 'name'
let name='uri';

//note: I repeat myself from part 1 so I can leave part1 as its own solution
let myListZero=bothlists[0];
let myListOne=bothlists[1];
myListZero.firstElementChild.innerHTML=name;
myListOne.firstElementChild.innerHTML=name;
console.log(myListZero);
console.log(myListOne);

		//EX2-part3
//I will reuse the <ul>list we have from part 2
let temp= myListOne.querySelectorAll("li");
myListOne.removeChild(temp[1]);
console.log(myListOne);