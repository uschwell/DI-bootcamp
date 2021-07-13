const dragElement=document.getElementById('container');
const area = document.getElementById('container');
function setSelected(a){
  dragElement=a;
}

dragElement.addEventListener('dragstart', dragstart_handler);
//area.addEventListener('dragover',dragover_handler);
area.addEventListener('drop',drop_handler);
function dragstart_handler(e){
  // e.preventDefault();
  // console.log(e.target.id);
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
  const data = e.dataTransfer.files;//getData('text/plain')
  console.log(data);
  // e.target.appendChild(document.getElementById(data))
}