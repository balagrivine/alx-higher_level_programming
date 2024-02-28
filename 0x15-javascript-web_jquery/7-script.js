//JavaScript script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json

const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";

$(document).ready(function() {
	$.get(URL, function(data) {
		const charName = data.name;
		$("DIV#character").text(`${charName}`);
	});
});
