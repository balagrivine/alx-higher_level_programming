#!/usr/bin/node

if (process.argv.length < 4) {
	console.log(0);
}

else {
	myList = process.argv.sort();
	console.log(myList[myList.length - 2]);
}
