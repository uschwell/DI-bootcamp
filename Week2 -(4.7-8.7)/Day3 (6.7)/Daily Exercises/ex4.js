let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
};




let input=prompt("Please enter your name ");
var check=0;
for (const i in guestList) {
  if((i == input)) {
    console.log(`Hi! I'm ${i}, and I'm from ${guestList[i]}.`);
    check=1;
  }
}
if (!check){
  console.log("Hi! I'm a guest.")
}