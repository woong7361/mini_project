import requests
from pprint import pprint
import json

_SERVICE_KEY = "POZVRpWN23c3nN3LZZ0XTJqXKKH5WHC3bHReKNfWykE1W06SAi7TPQ6n1gY%2BJGWnMZwTOUNQlDr38OJl22WDew%3D%3D";

def get_bad_state_stations(page = 1, count = 10):
	url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getUnityAirEnvrnIdexSnstiveAboveMsrstnList?";
	query = f"pageNo={page}&numOfRows={count}&returnType=json&serviceKey={_SERVICE_KEY}";

	to_json = (parse_json(url+query));
	return (to_json["body"]);

def get_station_state(station_name, page = 1, count = 1):
	url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?";
	query = f"serviceKey={_SERVICE_KEY}&returnType=json&numOfRows={count}&pageNo={page}&stationName={station_name}&dataTerm=DAILY&ver=1.0"
	to_json = (parse_json(url+query));

	body, header = [to_json["body"], to_json["header"]];
	total_count = body["totalCount"];
	items = body["items"];
	print(f"total count is {total_count}");
	return (items, total_count);

def parse_json(url):
	headers = {
		"User-Agent":
		"Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0",
	};
	data = requests.get(url, headers=headers);
	return (json.loads(data.text)["response"]);

if __name__ == "__main__":
#	print("환경 나쁨 측정소--------------");
#	print(get_bad_state_stations());
#	print();
#	print("강남구 측정 데이터------------");
	g_data, total_count = get_station_state("강남구", count = 2);
	pprint(g_data);
