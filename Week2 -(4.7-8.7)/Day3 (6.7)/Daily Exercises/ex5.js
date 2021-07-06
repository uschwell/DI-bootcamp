let family= {
	dad: "Bob",
	mom: "Yael",
	firstChild: "Yoni",
	secondChild: "Inbar",
	thirdChild: "Eli",
	fourthChild: "Moshe",
};

for (const i in family) {
	console.log(`${i}`);
}
for (const i in family) {
	console.log(`${family[i]}`);
}