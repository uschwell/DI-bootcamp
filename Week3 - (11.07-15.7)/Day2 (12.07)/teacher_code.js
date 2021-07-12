// 1. Click on a button
// 1. Add the planets on the DOM dynamically
// 2. Every planet - mouseover - background -> blue
                   // - mouseover - background -> blue
let planets = ["Mercury", "Pluto", "Mars", "Earth"];
let button = document.getElementsByTagName("input")[0];
button.addEventListener("click", addPlanets);
function addPlanets(event){
    console.log(event)
    let section =  event.target.nextElementSibling;
    console.log(section)
    for (let planet of planets){
        // --> 1st for loop : planet = "Mercury";
        // --> 1st for loop : planet = "Pluto";
        let divPlanet = document.createElement("div");
        divPlanet.addEventListener("mouseover", changeClass);
        divPlanet.addEventListener("mouseout", changeClass);
        let textNode = document.createTextNode(planet);
        divPlanet.appendChild(textNode);
        section.appendChild(divPlanet);
    }
}
function changeClass(event){
    event.target.classList.toggle("title")
};