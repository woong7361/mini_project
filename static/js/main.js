function get_weather() {
	let state_name = $("#guselect").val();
	loading();
	$.ajax({
		type: "GET",
		url: `/apis/weather?state=${state_name}`, 
		data: {},
		success: function(res) {
			loaded();
			if (res["message"])
				window.alert(res["msg"]);

			res = res["temperature"] ? res : make_mockdata();
			update_weather(res);
			res["date"] = Date().split("GMT")[0].trimRight();
			res["state"] = state_name;
			log_weather(res);
			render_log(res);
			$("#state_title").empty();
			$("#state_title").append(state_name);
		},
		error: function(...err) {
			loaded();
			let res = make_mockdata();
			update_weather(res);
			res["date"] = Date().split("GMT")[0].trimRight();
			res["state"] = state_name;
			log_weather(res);
			render_log(res);
			$("#state_title").empty();
			$("#state_title").append(state_name);
		}
	});
}

function make_mockdata() {
	let data = {};
	window.alert("공공데이터 서버이슈로 임의데이터로 처리합니다.");
	data["temperature"] = "-2"
	data["humidity"] = "41";
	data["pm10Value"] = "14";
	data["pm25Value"] = "12";

	return (data);
}
function render_log(data) {
	let to_html = `
	<div class="accordion-item">
		<h2 class="accordion-header" id="headingOne">
			<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
				<span>${data["date"]},</span><span>${data["state"]}</span>
			</button>
		</h2>
		<div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
		  <div class="accordion-body">
				<ul class="list-group list-group-horizontal">
					<li class="list-group-item">기온: ${data["temperature"]}</li>
					<li class="list-group-item">습도: ${data["humidity"]}</li>
					<li class="list-group-item">pm25: ${data["pm25Value"]}</li>
					<li class="list-group-item">pm10: ${data["pm10Value"]}</li>
				</ul>
		  </div>
		</div>
	</div>
`;
	$("#searchlogger").append(to_html);
}

function log_weather(data) {
	let logs;

	logs = window.sessionStorage.getItem("w_search_logs");
	if (logs == null) { 
		window.sessionStorage.setItem("w_search_logs", JSON.stringify([]));
		logs = [];
	} else {
		logs = JSON.parse(logs);
	}

	if (data != null)
		logs.push(data);

	window.sessionStorage.setItem("w_search_logs", JSON.stringify(logs));
	return (logs);
}

function update_weather(data) {
	$("#temp-v").empty();
	$("#hum-v").empty();
	$("#pm10-v").empty();
	$("#pm25-v").empty();
	$("#temp-v").append(data["temperature"]);
	$("#hum-v").append(data["humidity"]);
	$("#pm10-v").append(data["pm10Value"]);
	$("#pm25-v").append(data["pm25Value"]);
	console.log(data);
}

$(window).on('load', function () {
	window.sessionStorage.setItem("w_search_logs", JSON.stringify([]));
})
