//JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.

$(document).ready(function() {
	const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
	$.getJSON(url, function(data) {
		const helloTemplate = data.translations.hello;

		$("DIV#hello").text(helloTemplate);
	});
});
