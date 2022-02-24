function get_weather() {
	let state_name = $("#state_input").val();
	alert(`요청한 정보는 ${state_name}구 입니다.`);
	$.ajax({
		type: "GET",
		url: `/apis/weather?state=${state_name}`, /* api 주소 넣는 부분 */
		data: {},
		success: function(res) {
			alert(`${state_name}구 에대한 응답을 수신하였습니다.`);
			update_weather(res);
		},
		error: function(...err) {
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
