#!/usr/bin/node
let i;
let j;
let arg = process.argv[2];

if (isNaN(arg)) {
	console.log('Missing size');
}

for (i = 0; i < arg; i++)
{
	console.log('X'.repeat(Number(arg)));
}
