let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

for (const i in details){
  console.log(` ${i} ${details[i]}`)
  //you requested a "console log" but if you want to avoid writing new lines you can use the below commands to print
  //process.stdout.write(` ${i} ${details[i]}`);
}