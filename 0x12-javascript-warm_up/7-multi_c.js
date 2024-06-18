#!/usr/bin/node
const a = Math.floor(Number(process.argv[2]));
if (isNaN(a)){
  console.log("Missing number of occurences");
} else {
  for (let i = 0; i < a; i++){
	console.log("C is fun");
  }
}
