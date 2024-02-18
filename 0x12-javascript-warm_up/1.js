#!/usr/bin/node

const Person = {
	name: ["Bob", "Smith"],
	age: 32,
	bio: function () {
		console.log('${this.name[0]} ${this.name[1]} is ${this.age} years');
	}
};
Person.bio();
