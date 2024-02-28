//JavaScript script that adds, removes and clears LI elements from a list when the user clicks:

$(document).ready(function() {
	$("DIV#add_item").on("click", function() {
		const newItem = $("<li>").text("Item");
		$("UL.my_list").append(newItem);
	});

	$("DIV#remove_item").on("click", function() {
		$("UL.my_list li:last").remove();
	});

	$("DIV#clear_list").on("click", function() {
		$("UL.my_list").empty;
	});
});
