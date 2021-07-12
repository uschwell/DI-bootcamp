

function madLibs(event){
	 event.preventDefault();
	 //let allNames=
	let temp=document.querySelectorAll("input[type=text]");
	//let temp2=document.querySelectorAll("#noun");


	//console.log(temp);
	//console.log(temp2);
	for (let i=0; i<temp.length; i++){
		// console.log(temp[i].id);
		// console.log(temp[i].value);

		//we check that none of the values have been left empty
		if(temp[i].value==""){
			console.log("Error! One of the fields is empty, try again!")
			return (-1);
		}
	}
		let noun=(temp[0].value);
		let adjective=(temp[1].value);
		let name=(temp[2].value);
		let verb=(temp[3].value);
		let place=(temp[4].value);

		//if we have checked all the code and found all the values filled-we create a story
		console.log(`A vacation is when you take a trip to some ${adjective} place
		with your ${adjective} family. Usually you go to some place
		that is near a/an ${noun} or up on a/an ${noun}.
		A good vacation place is one where you can ride ${noun}s
		or play ${verb} or go hunting for ${noun}s . I like
		to spend my time ${verb}ing or ${verb}ing.
		When parents go on a vacation, they spend their time eating
		three ${noun}s a day, and fathers play golf, and mothers
		sit around ${verb}ing.`);
}