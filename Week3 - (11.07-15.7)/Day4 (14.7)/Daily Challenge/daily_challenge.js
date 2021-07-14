const taskList= document.getElementById('toDoList');
let listTasks = [];

function addTask(){

	//get the input text
	let input=document.getElementById("inputBox").value;
	if(input!=""){
		//reset the text box for next time
		document.getElementById("inputBox").value="";

		//note: (these indentations are for my ease of use of the code)
		//create a new overall div container to add to  the list
		let temp = document.createElement("DIV");
						temp.setAttribute("class", "listItem");
		//create a text div to save the input text
		let textBox= document.createElement("DIV");
						//save the input text in our new div
						textBox.textContent = input;

		//create a check div to add a checkmark
		let checkBox = document.createElement("input");
		checkBox.setAttribute("type", "checkBox");
		checkBox.style.font='awesome';
		checkBox.addEventListener('checked', cross_out);

		//add the checkbox AND the textBox to our overall div
		temp.appendChild(checkBox);
		temp.appendChild(textBox);


		listTasks.push(input);

		//finally, we add our overall div to the to-do list
		taskList.appendChild(temp);
	}

}


function cross_out(e){
	e.setAttribute.checked='true';
}

function cross_in(e){
	e.setAttribute("style", "del");
}