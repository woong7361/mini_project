function check_form(){
	let guselect = $("#guselect").val();
	if (guselect != "") {
		$("#weather-submit").removeClass("btn-secondary");
		$("#weather-submit").removeClass("disabled");
		$("#weather-submit").addClass("btn-primary");
	} else {
		$("#weather-submit").removeClass("btn-primary");
		$("#weather-submit").removeClass("disabled");
		$("#weather-submit").removeClass("btn-secondary");
		$("#weather-submit").addClass("btn-secondary");
		$("#weather-submit").addClass("disabled");
	};
}
