//JavaScript script that toggles the class of the <header> element when the user clicks on the tag DIV#toggle_header:

$(document).ready(function() {
	$("DIV#toggle_header").on("click", function() {
		const header = $("header");

		if (header.hasClass("red")) {
			header.removeClass("red").addClass("green");
		}
		else {
			header.removeclass("green").addClass("red");
	});
});
