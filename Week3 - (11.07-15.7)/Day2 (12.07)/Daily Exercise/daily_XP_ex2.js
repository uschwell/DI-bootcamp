

function getBold_items(){
 let allBold= document.querySelectorAll("strong");
 return allBold;
}



function highlight(){
	let toBold=getBold_items();
	for(let i=0; i<toBold.length; i++){
		toBold[i].style.color="blue";
	}
}


function return_normal(){
	let unBold=getBold_items();
	for(let i=0; i<unBold.length; i++){
		unBold[i].style.color="black";
	}
}




getBold_items();
highlight();
return_normal();