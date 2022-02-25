function loading() {
	$(".icons.waiting").addClass("d-none");
	$(".icons.loading").removeClass("d-none");
	$("#weather-submit").attr("disabled", true);
	$("#weather-submit").empty();
	$("#weather-submit").append(
		`<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>`
	);
	$("#weather-submit").append("Loading...");
}
function loaded() {
	$(".icons.loading").addClass("d-none");
	$(".icons.waiting").removeClass("d-none");
	$("#weather-submit").empty();
	$("#weather-submit").attr("disabled", false);
	$("#weather-submit").append("알아보기");
}
