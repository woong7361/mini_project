import requests
import datetime as dt
import pandas as pd

def getAirCondition(guName):
    # resultCode 결과코드
    # resultMsg  결과메세지
    # numOfRows  한 페이지 결과 수
    # pageNo     페이지 번호
    # totalCount 전체 결과 수
    # items      목록
    # dataTime   측정일
    # mangName   측정망
    # 정보        so2Value
    # 아황산가스 농도 coValue
    # 일산화탄소 농도 o3Value
    # 오존 농도    no2Value
    # 이산화질소 농도 pm10Value
    # 미세먼지(PM10) 농도 pm10Value
    # 미세먼지(PM10) 24시간예측이동농도 pm25Value
    # 미세먼지(PM2.5) 농도 pm25Value
    # 미세먼지(PM2.5) 24시간예측이동농도 khaiValue
    # 통합대기환경수치 khaiGrade
    # 통합대기환경지수 so2Grade
    # 아황산가스 지수 coGrade
    # 일산화탄소 지수 o3Grade
    # 오존 지수 no2Grade
    # 이산화질소 지수 pm10Grade
    # 미세먼지(PM10)24시간등급 pm25Grade
    # 미세먼지(PM2.5) 24 시간 등급 pm10Grade1h
    # 미세먼지(PM10) 1 시간 등급 pm25Grade1h


    SERVICE_KEY = '6kDG3hNORaARv7W8cSUsMljgWXSesh6RWfGFzWp0nUc1wR2szvaeC5A/CkGkea0ShVlyPuokZ5zWzIvVeVHFwg=='

    url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
    params = {'serviceKey': SERVICE_KEY, 'returnType': 'json', 'numOfRows': '1',
              'pageNo': '1', 'stationName': guName, 'dataTerm': 'DAILY', 'ver': '1.0'}

    response = requests.get(url, params=params)

    # make response to dictionary
    json = response.json()


    result = -1
    # confirm resultCode
    if json['response']['header']['resultCode'] == '00':
        # fail
        if not json['response']['body']['items']:           #잘못된 주소 입력시 빈 리스트 반환
            result = -1
        # success
        else:
            #성공이라면 pm10 과 pm25 의 미세먼지 값을 tuple로 반환
            json = response.json()
            result = {
                'pm10Value': json['response']['body']['items'][0]['pm10Value'],
                'pm25Value': json['response']['body']['items'][0]['pm25Value']
                }

    return result

def getWeather(guName):
    # T1H     기온    ℃
    # RN1     1 시간 강수량 mm
    # REH     습도 % 8

    SERVICE_KEY = '6kDG3hNORaARv7W8cSUsMljgWXSesh6RWfGFzWp0nUc1wR2szvaeC5A/CkGkea0ShVlyPuokZ5zWzIvVeVHFwg=='

    #현재시간 parameter 생성
    now = dt.datetime.now()
    currentDate = str(now.year) + str(format(now.month, '02')) + str(now.day)

    #seoul_location.xlsx에서 입력한 구 이름과 일치하는 좌표 탐색
    location = pd.read_excel('static/data/seoul_location.xlsx', engine='openpyxl')
    selectGu = location[location['구'] == guName]


    result = -1
    #fail
    if selectGu.empty:
        result = -1
    else:
    #success
        coordinate = (selectGu.iloc[0]['x'], selectGu.iloc[0]['y'])

        url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
        params = {'serviceKey': SERVICE_KEY,'pageNo': '1', 'numOfRows': '14', 'dataType': 'JSON',
                  'base_date': currentDate, 'base_time': '0600','nx': coordinate[0], 'ny': coordinate[1]}

        response = requests.get(url, params=params)

        json = response.json()
        itemList = json['response']['body']['items']['item']

        list = {'T1H': 'temperature', 'RN1': 'precipitation', 'REH': 'humidity'}

        result = {}
        for li in list:
            for item in itemList:
                if item['category'] == li:
                    result[list[li]] = item['obsrValue']


    return result