

// function sayHi(phrase, who) {
//   alert( phrase + ', ' + who );
// }

// setTimeout(sayHi, 10000, "Hello", "John");


// setInterval(function() {
//       console.log("are we there yet?");
// }, 5000);

const box = document.getElementById('box');
let id;
let left = 0;
let screenWidth = window.screen.availWidth;
function move() {
  id = setInterval(function(){
    if(left > screenWidth-20){
      stop();
      console.log("stopRight");
    }
    left += 5;
    // box.style.left = left + 'px';
    box.style.left = `${left}px`
  },5)
}


function back() {
  id = setInterval(function(){
    if(left <= 0){
      	stop();
  		console.log("stopLeft");
	}	
    left -= 5;
    // box.style.left = left + 'px';
    box.style.left = `${left}px`
  },5)
}


function stop() {
  clearInterval(id)
}



		//drag the second box!!

box2.addEventListener('dragstart', function(e){
	let x=e.clientX;
	let y=e.clientY;
	console.log(`drag: ${x} ${y}`)

})



box2.addEventListener('drag', function(e){
	let x=e.clientX;
	let y=e.clientY;
	console.log(`drag: ${x} ${y}`)

})



box2.addEventListener('dragend',function(e){
	let x=e.clientX;
	let y=e.clientY;
	console.log(`dragend: ${x} ${y}`);
	box2.style.left = x+'px';
	box2.style.top = y+ 'px';
})




				//drag the text!

// const dragElement=document.getElementById('dragText');
// const area = document.getElementById("drop-area");

// area.addEventListener('dragenter', function(e){

// 	console.log('enter',e.clientX, e.clientY);

// })

// area.addEventListener('drag', function(e){
// 	let x=e.clientX;
// 	let y=e.clientY;
// 	console.log(`dragText: ${x} ${y}`)
	
// })

// area.addEventListener('dragend', function(e){
// 	console.log("drag-Text-End");
// 	let x=e.clientX;
// 	let y=e.clientY;
// 	dragElement.style.left = x+'px';
// 	dragElement.style.top = y+ 'px';

// })



		//Highlight and Shading!
const dragElement=document.getElementById('dragText');
const area = document.getElementById("drop-area");
dragElement.setAttribute('draggable', 'true');

dragElement.addEventListener('dragstart',dragstart_handler);
area.addEventListener('dragover',dragover_handler);
area.addEventListener('drop',drop_handler);

function dragstart_handler(e){
	e.preventDefault();
	e.dataTransfer.setData('text/plain', e.target.id);
}

function dragover_handler(e){
	e.preventDefault();
	e.dataTransfer.dropEffect= 'link';
	area.classList.add('highlight');
}

function drop_handler(e){
	e.preventDefault();
	area.classList.remove('highlight');
	const data= e.dataTransfer.files;
	e.target.appendChild(document.getElementById(data));

}