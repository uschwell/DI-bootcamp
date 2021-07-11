let solarSystem=['mercury','venus', 'earth', 'mars'];






function createPlanet(name, currentSystem){
	let newPlanet=document.body.querySelectorAll("section");
	// console.log(newPlanet);

	 let totalList=newPlanet.firstChild;

	console.log(totalList);
	const planet = document.createElement("div");

	//assign each new planet to have it's name as both an inner text AND an ID
	const node = document.createTextNode(name);

	let identification = document.createAttribute("id");
	identification.value = name;
	planet.setAttributeNode(identification);

	//make new planet have 'planet' class
	let setClass = document.createAttribute("class");
	setClass.value = 'planet';
	planet.setAttributeNode(setClass);

	//generate a new random color and attach it to our new planet
	let randomColor = Math.floor(Math.random()*16777215).toString(16);
	let setStyle = document.createAttribute("style");
	setStyle.value = `background-color: ${randomColor};`;
	planet.setAttributeNode(setStyle);





	// console.log(planet);



	//we add our 'planet' to the (main) NodeList
	newPlanet[0].appendChild(planet);
	// console.log(document.body);

}

// createPlanet("haha", solarSystem);


for(const i in solarSystem){
	createPlanet(solarSystem[i],solarSystem);
}

