		//Part 1- animated moving box
const box = document.getElementById('animate');
const container=document.getElementById('container');
let id;
let left = 0;
let totalWidth = container.offsetWidth;


function myMove() {
  id = setInterval(function(){
    if(left >= (totalWidth-50)){
      	stop();
	}	
    left += 5;
    box.style.left = `${left}px`
  },5)
}


function stop() {
  clearInterval(id)
}


		//Part 2 - dragabble box
const dragElement = document.getElementById('dragBox');
const area = document.getElementById('dragContainer');


dragElement.addEventListener('dragstart', dragstart_handler);
area.addEventListener('dragover',dragover_handler);
area.addEventListener('drop',drop_handler);

function dragstart_handler(e){
  e.dataTransfer.setData('text/plain',e.target.id);
}
function dragover_handler(e){
  // console.log('over');
  e.preventDefault();
  e.dataTransfer.dropEffect = 'link'
  area.classList.add('highlight');
}
function drop_handler(e){
  e.preventDefault();
  area.classList.remove('highlight');
  const data = e.dataTransfer.getData('text/plain')
  console.log(data);
   e.target.appendChild(document.getElementById(data))
}