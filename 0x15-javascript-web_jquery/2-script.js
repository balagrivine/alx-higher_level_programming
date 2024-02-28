//JavaScript script that updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header

$(document).ready(function() {
	$("DIV#header").on("click", function() {
		$("header").css("color", "red");
	});
});
