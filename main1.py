import pandas as pd
import numpy as np
import folium

# 데이터
map_data = pd.DataFrame({
    'lat': [-34, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97],
    'lon': [-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
    'name': ['Buenos Aires', 'Paris', 'Melbourne', 'St Petersburg', 
    		 'Abidjan', 'Montreal', 'Nairobi', 'Salvador'],
    'value': [10, 12, 40, 70, 23, 43, 100, 43] 
  })


#1 지도 객체 생성
my_map = folium.Map(
	location=[map_data['lat'].mean(), map_data['lon'].mean()], 
    zoom_start=2)
    
    
#2 지도 커스텀
# 지도에 원형 마커와 값 추가
for index, row in map_data.iterrows():       # 데이터프레임 한 행 씩 처리

    folium.CircleMarker(                     # 원 표시
        location=[row['lat'], row['lon']],   # 원 중심- 위도, 경도
        radius=row['value'] / 5,             # 원의 반지름
        color='pink',                        # 원의 테두리 색상
        fill=True,                           # 원을 채움
        fill_opacity=1.0                     # 원의 내부를 채울 때의 투명도
    ).add_to(my_map)                         # my_map에 원형 마커 추가

    folium.Marker(                           # 값 표시
        location=[row['lat'], row['lon']],   # 값 표시 위치- 위도, 경도
        icon=folium.DivIcon(
        	html=f"<div>{row['name']} {row['value']}</div>"), # 값 표시 방식
    ).add_to(my_map)                         # my_map에 값 추가
    
    
#3 지도 제목과 캡션 추가
st.title('Map with Location Data')
st.caption(
	"Displaying geographical data on a map using Streamlit and Folium")

#4 지도 시각화
st.components.v1.html(my_map._repr_html_(), width=800, height=600)
