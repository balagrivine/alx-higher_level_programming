#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

for (const key in dict) {
	console.log(key + ': ' + dict[key]);
}
