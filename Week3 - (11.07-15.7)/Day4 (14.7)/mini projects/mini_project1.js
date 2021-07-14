const panel=document.getElementById('controlPanel');
const drawSpace=document.getElementById('drawingSpace');
let colorList=["White","Black","Grey","Red","Orange","Yellow","LightGreen","Green","SkyBlue","LightBlue",
"Blue","DarkTurquoise","Purple","DarkViolet","DeepPink","DeepSkyBlue", "Pink","seagreen","darkgoldenrod", "Magenta",
 "MidnightBlue", "RoyalBlue" ];
const gridBoxArray=[];

let currentColor;

					//LEFT SCREEN CODE
function addBoxes(rows, columns){
	let counter=0;
	for(let row=0;row<rows; row++){
		for(let col=0; col<columns;col++){
			let temp = document.createElement("DIV");
			temp.setAttribute("class", "buttonBox");
			temp.setAttribute("style", `background-color: ${colorList[counter]}`);
			// console.log(`${colorList[(row+col)]}`);
			temp.setAttribute('clickable','true');
			panel.appendChild(temp);
			temp.addEventListener('click', click_handler);
			counter++;
		}

	}
}


function click_handler(e){
	  e.preventDefault();
	//first-we unselect any previous buttons

	//then, we highlight the currently selected button
	panel.classList.add('highlight');
	currentColor= e.target.style.backgroundColor;
}


				//RIGHT SCREEN CODING

			//js code for the right side of screen
function addCanvas(){
	//we figure out how large the boxes must be to fill our entire canvas
	totalWidth=drawSpace.offsetWidth;
	totalHeight=drawSpace.offsetHeight;
	gridWidth=(totalWidth/60);
	gridHeight=(totalHeight/24);

//useful printouts for troubleshooting	
	// console.log(`totalWidth= ${totalWidth}`);
	// console.log(`totalHeight= ${totalHeight}`);
	// console.log(`gridHeight= ${gridHeight}`);
	// console.log(`gridWidth= ${gridWidth}`);

	for(let row=0;row<24; row++){
		for(let col=0; col<60;col++){
			let temp = document.createElement("DIV");
			temp.setAttribute("style", `width:${gridWidth}`);
			temp.setAttribute("style", `height:${gridHeight}`);
			temp.setAttribute("class", "gridBox");
			temp.setAttribute('clickable','true');
			// console.log(`box= ${temp}`);
			gridBoxArray.push(temp);

			drawSpace.appendChild(temp);
			//temp.addEventListener('click', click_handler);

			//event that triggers every time the mouse moves over a canvas box
			temp.addEventListener('mouseover', click_drag);
		}

	}
}


function click_drag(e){
	  e.preventDefault();
	  let buttonsPressed = e.buttons;
	  //we check if you ALSO had the left mouse button clicked
	  if(buttonsPressed==1){
	  		e.target.style.backgroundColor=currentColor;
	  }

}






//function to reset the entire canvas
function clearAll(){
	let temp2=drawSpace.getElementsByClassName("gridBox");
	//reset the background color of the cnavas boxes to white
	for(const i in gridBoxArray){
		temp2[i].style.backgroundColor='white';
	}
}