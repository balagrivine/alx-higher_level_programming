#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, response, body) => {
	if (err)
	{
		console.error(err);
		return;
	}

	const movieData = JSON.parse(body);
	console.log(movieData.title);
	return;
});
