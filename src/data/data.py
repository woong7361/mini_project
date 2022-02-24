import pandas as pd
import numpy as np

# data폴더의 korea_xy_location 읽고 가공
location = pd.read_excel('korea_xy_location.xlsx', engine='openpyxl')
location = location[['1단계', '2단계', '격자 X', '격자 Y']]
isSeoul = location['1단계'] == '서울특별시'
seoul = location[isSeoul]
noDupSeoul = seoul.drop_duplicates(['1단계', '2단계'])
noDupSeoul.columns = ['시', '구', 'x', 'y']

# seoul_location.xlsx 로 저장
noDupSeoul.to_excel('seoul_location.xlsx', index=False)
