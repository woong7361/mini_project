function get_weather() {
	let state_name = $("#guselect").val();
	alert(`요청한 정보는 ${state_name} 입니다.`);
	loading();
	$.ajax({
		type: "GET",
		url: `http://localhost:5000/apis/weather?state=${state_name}`, 
		data: {},
		success: function(res) {
			loaded();
			alert(`${state_name}구 에대한 응답을 수신하였습니다.`);
			update_weather(res);
		},
		error: function(...err) {
			loaded();
			const message = err[2];
			alert(`${message}, 에러발생.`);
		}
	});
}

function update_weather(data) {
	alert("응답은 console에");
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
