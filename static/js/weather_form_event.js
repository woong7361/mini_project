function check_form(){
	let [email, comment, guselect] = [$("#comment-email").val(),$("#comment-text").val(),$("#guselect").val()];
	if (email != "" && comment != "" && guselect != "") {
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
