//NOTES FOR CHECKER (look at top of index_XPGold.html)


const dragElements= document.getElementsByClassName('boxes');
const area = document.getElementById('container');

for(let i=0; i<dragElements.length; i++){
   dragElements[i].addEventListener('dragstart', dragstart_handler);

   dragElements[i].addEventListener('drag', function(e){
      // let x=e.clientX;
      // let y=e.clientY;
      // console.log(`drag: ${x} ${y}`)
    })
     dragElements[i].addEventListener('dragend',function(e){
    let x=e.clientX;
    let y=e.clientY;
    // console.log(`dragend: ${x} ${y}`);
    dragElements[i].style.left = x+'px';
    dragElements[i].style.top = y+ 'px';
  })
}

 //area.addEventListener('drop',drop_handler);


 function dragstart_handler(e){
   //e.preventDefault();
  e.dataTransfer.setData('text/plain',e.target.id);
}

function drop_handler(e){
  e.preventDefault();
  console.log("dropped");
  //area.classList.remove('highlight');
  let data = e.dataTransfer.getData('text/plain')
  console.log(data);
  e.target.appendChild(document.getElementById(data))
}