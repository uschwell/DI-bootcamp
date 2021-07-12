
			//EX1-part 1
function insertRow(){
	// Find a <table> element with id="myTable":
	var table = document.getElementById("sampleTable");
	// console.log(table);

	// Create an empty <tr> element and add it to the 1st position of the table:
	var row = table.insertRow(-1);

	// Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
	var cell1 = row.insertCell(0);
	var cell2 = row.insertCell(1);
	var temp=table.querySelectorAll("TR");
	// console.log(temp);
	var length=temp.length;
	// Add some text to the new cells:
	cell1.innerHTML = `Row${length} cell 1`;
	cell2.innerHTML = `Row${length} cell 2`;
}

