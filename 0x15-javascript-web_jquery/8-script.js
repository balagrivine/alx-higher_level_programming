//JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json

$.ajax ({
	url: "https://swapi-api.alx-tools.com/api/films/?format=json";
	dataType: "JSON";
	success: function(data) {
		const movies = data.results;
		const titles = movies.map(movie => movie.title);
		titles.forEach(function(movieTitle) {
			$("UL#list_movies").append(`<li>${movieTitle}</li>`);
		});
	}
});
