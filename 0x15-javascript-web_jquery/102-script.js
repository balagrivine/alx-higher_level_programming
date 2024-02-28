// JavaScript script that fetches and prints how to say “Hello” depending on the language

$(document).ready(function() {
	$("INPUT#btn_translate").on("click", function() {

		const langCode = $("INPUT#language_code").val();
		const url = `https://www.fourtonfish.com/hellosalut/hello/${langCode}`;
		$.getJSON(url, function(data) {
			const translation = data.hello;
			$("DIV#hello").text(translation);
		});
	});
});
