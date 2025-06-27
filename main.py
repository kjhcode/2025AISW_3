import streamlit as st
import folium
import pandas as pd
from streamlit_folium import folium_static

# 1. 데이터 준비 (예시)
data = {'위도': [37.5, 37.6, 37.7],
        '경도': [127.0, 127.1, 127.2],
        '이름': ['장소1', '장소2', '장소3']}
df = pd.DataFrame(data)

# 2. Folium 지도 생성
m = folium.Map(location=[df['위도'].mean(), df['경도'].mean()], zoom_start=10)

for i in range(len(df)):
    folium.Marker(
        location=[df['위도'][i], df['경도'][i]],
        popup=df['이름'][i]
    ).add_to(m)

# 3. Streamlit 앱 구성
st.title("Streamlit과 Folium으로 지도 시각화")

# 4. Folium 지도 표시
folium_static(m)

# (선택사항) 데이터 필터링 및 상호작용
selected_name = st.selectbox("장소 선택", df['이름'])
if selected_name:
    filtered_df = df[df['이름'] == selected_name]
    filtered_map = folium.Map(location=[filtered_df['위도'].iloc[0], filtered_df['경도'].iloc[0]], zoom_start=12)
    folium.Marker(
        location=[filtered_df['위도'].iloc[0], filtered_df['경도'].iloc[0]],
        popup=filtered_df['이름'].iloc[0]
    ).add_to(filtered_map)
    folium_static(filtered_map
