#!/usr/bin/node

exports.esrever = function (list) {
	let newList = [];
	for (let i = list.length; i > 0; i--)
	{
		newList.push(list[i - 1]);
	}
	return newList;
}
