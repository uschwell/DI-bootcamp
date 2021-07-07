let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}


function checkBasket(){
	let input=prompt("what item are you searching for? ");
	let flag=1;
	//make sure that we don't fail because of an error in upper/lower case
	input=input.toLowerCase();
	for(const i in amazonBasket){
		if(i==input){
		console.log("That item is already in your basket!");
		flag=0;
		}
	}
	if(flag){
		console.log("You have not selected that item yet-would you like me to find it for you?");
	}

}




checkBasket();