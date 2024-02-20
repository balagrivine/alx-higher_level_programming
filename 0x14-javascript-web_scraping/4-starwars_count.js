#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
	if (err)
	{
		console.error(err);
	}
	const filmsData = JSON.parse(body);

	const filmWedge = filmsData.results.filter(film => film.characters .includes('https://swapi-api.alx-tools.com/api/people/18/'));
	console.log(filmWedge.length);
	return;
});
