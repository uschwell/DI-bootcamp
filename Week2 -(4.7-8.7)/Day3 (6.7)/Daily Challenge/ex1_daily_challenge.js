
//using only one loop
var stars=["*","* *","* * *","* * * *","* * * * *","* * * * * *"]
for(let i=0;i<6;i++){
	console.log(stars[i]);
}


//using two loops
for(let x=0; x<6; x++){
	var line=["*"];
	for(let y=0;y<x;y++){
		line.push("*");
	}
	console.log(line);
}

//note: we could use some version of "printf()" to avoid creating a newline each time-altenative solution

