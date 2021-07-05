			//EX1
var age = window.prompt("Which is your age? ");
//check they are over 18
if(age>18){
	alert("Powering On. Enjoy the ride!");
}else if(age==18){
	alert("Congratulations on your first year of driving. Enjoy the ride!");
}
//else if they are under 18
else{
	alert("Sorry, you are too young to drive this car. Powering off");
}


				//EX2 ------ note: in order to run EX2 and/or EX3 you will need to comment ONE of them out. (Otherwise we declare "a" twice-error)

//set a to be 4
let a = 2 + 2;

//check the value of a (currently 4)
switch (a) {
	//if a=3 3 (false) print- "too small"
  case 3:
    alert( 'Too small' );
    break;
    //if 4 (true!!) print "Exactly"<============= this is what will actually print!
  case 4:
    alert( 'Exactly!' );
    break;
    //if a=5 (false) print "too large"
  case 5:
    alert( 'Too large' );
    break;
    //if a doesn't equal ANY of the values (of 3,4,5) then it will print "I don't know...."
  default:
    alert( "I don't know such values" );
}



				//EX3 --------- note: in order to run EX2 and/or EX3 you will need to comment ONE of them out. (Otherwise we declare "a" twice-error)
//set the value of a to be 4
let a = 2 + 2;


//check the value of a- if it equals 4,3,5 or 'other'
switch (a) {

	//if a=4 print "Right"<===================This is what will print!
  case 4:
    alert('Right!');
    break;
  //if a=3 OR a=5 print "Wrong! Why don't you take a math class"
  case 3: // (*) grouped two cases
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

//if a is other (i.e doesn't equal 3,4,5) then it will print "The result is strange......"
  default:
    alert('The result is strange. Really.');
}