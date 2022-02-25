function get_weather() {
	let state_name = $("#guselect").val();
	loading();
	$.ajax({
		type: "GET",
		url: `/apis/weather?state=${state_name}`, 
		data: {},
		success: function(res) {
			loaded();
			update_weather(res);
			$("#state_title").empty();
			$("#state_title").append(state_name);
		},
		error: function(...err) {
			loaded();
			const message = err[2];
			console.log(`${message}, 에러발생.`);
		}
	});
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

/*
function weather_to_html(city, temp) {
	return (`${temp}`);
}


function get_weather_old() {
	let state_name = $("#state_input").val();

	alert(val);
	$.ajax({
		type: "GET",
		url: "http://spartacodingclub.shop/sparta_api/weather/seoul",
		url: "http://spartacodingclub.shop/sparta_api/weather/seoul",
		data: {},
		success: function(res) {
			
			update_weather(res);
		}
	});
}


*/
