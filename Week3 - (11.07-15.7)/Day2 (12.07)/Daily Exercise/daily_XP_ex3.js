
function calculate() {
    event.preventDefault();
    let temp=document.querySelectorAll("input[type=text]");
    let rad=(temp[0].value);
    rad= parseInt(rad);
    //we calculate the volume according to the input radius
    let volume=(rad*rad*rad*3.14*(4/3));
    //console.log(volume);

    temp[1]=volume;
    document.getElementById("output").innerHTML=`Volume= ${volume}`;
}