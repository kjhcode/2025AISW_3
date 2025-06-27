import streamlit as st
import folium
from streamlit_folium import st_folium

# 페이지 설정을 넓게 해서 지도를 시원하게 볼 수 있게 해줄게!
st.set_page_config(layout="wide")

st.title("✨ 나만의 위치 북마크 지도 ✨")
st.write("팬더야, 너만의 소중한 장소들을 지도에 콕콕 찍어 북마크 해봐! 🗺️")

# 💖 북마크 리스트를 저장할 공간을 만들어줄게!
# 'bookmarks'라는 이름으로 세션 상태에 리스트를 저장할 거야.
# 앱을 껐다 켜면 사라지지만, 앱이 실행되는 동안에는 계속 유지된단다!
if "bookmarks" not in st.session_state:
    st.session_state.bookmarks = []

# 📍 지도 만들기!
# 초기 지도의 중심은 네가 전에 관심 있어 했던 광주 북구청 근처로 설정해봤어!
# (광주 북구청 좌표: 35.1740, 126.9130)
m = folium.Map(location=[35.1740, 126.9130], zoom_start=12)

# 📌 기존에 추가된 북마크들을 지도에 표시하기
# 저장된 북마크들을 하나씩 꺼내서 지도에 마커로 찍어줄 거야.
for i, bookmark in enumerate(st.session_state.bookmarks):
    folium.Marker(
        location=[bookmark["latitude"], bookmark["longitude"]], # 위도, 경도
        popup=bookmark["name"], # 마커 클릭하면 나오는 이름
        tooltip=bookmark["name"], # 마우스 올리면 나오는 이름
        icon=folium.Icon(color="red", icon="heart") # 북마크니까 예쁜 하트 아이콘 어때? ❤️
    ).add_to(m) # 지도에 추가!

# 📝 새로운 북마크 추가하는 입력 폼 (왼쪽 사이드바에 나타날 거야!)
st.sidebar.header("📍 새 북마크 추가하기")
with st.sidebar.form("new_bookmark_form"): # 폼으로 만들면 입력 후 자동으로 초기화돼서 편리해!
    name = st.text_input("장소 이름", placeholder="예: 우리집, 단골 카페")
    latitude = st.number_input("위도 (Latitude)", format="%.4f", value=35.1740) # 광주 북구청 위도 기본값
    longitude = st.number_input("경도 (Longitude)", format="%.4f", value=126.9130) # 광주 북구청 경도 기본값
    add_button = st.form_submit_button("북마크 추가!")

    if add_button: # '북마크 추가!' 버튼을 누르면
        if name and latitude is not None and longitude is not None: # 모든 정보가 입력되었는지 확인!
            st.session_state.bookmarks.append({ # 북마크 리스트에 새 장소 추가!
                "name": name,
                "latitude": latitude,
                "longitude": longitude
            })
            st.sidebar.success(f"'{name}' 북마크가 추가되었어! 🎉") # 성공 메시지!
        else:
            st.sidebar.warning("장소 이름, 위도, 경도를 모두 입력해줘! 🥺") # 경고 메시지!

# 📋 내 북마크 목록 보여주기
st.sidebar.header("📋 내 북마크 목록")
if st.session_state.bookmarks: # 북마크가 하나라도 있다면
    for i, bookmark in enumerate(st.session_state.bookmarks):
        st.sidebar.write(f"{i+1}. **{bookmark['name']}** (위도: {bookmark['latitude']:.4f}, 경도: {bookmark['longitude']:.4f})")
    
    # 모든 북마크를 한 번에 지우는 버튼도 만들어줄게!
    if st.sidebar.button("모든 북마크 지우기 🗑️"):
        st.session_state.bookmarks = [] # 리스트를 비워버려!
        st.sidebar.info("모든 북마크가 지워졌어! 다시 시작해봐! 😊")
        st.experimental_rerun() # 지도를 다시 그리도록 페이지를 새로고침해줘!

else: # 북마크가 하나도 없다면
    st.sidebar.info("아직 북마크가 없어! 왼쪽에 추가해봐~ 💖")

# 🗺️ 지도를 화면에 보여주기!
st_folium(m, width=1000, height=600) # 지도의 가로, 세로 크기도 조절할 수 있어!

st.markdown("""
---
### 💡 사용 팁!
*   **위도/경도 찾는 법:** 구글 지도에서 원하는 장소를 검색하고, 마우스 오른쪽 버튼을 클릭하면 위도와 경도를 쉽게 복사할 수 있단다!
*   **저장:** 지금은 앱을 닫으면 북마크가 사라지지만, 나중에는 이 북마크 리스트를 파일(예: JSON 파일)로 저장해서 앱을 다시 켜도 계속 쓸 수 있게 만들 수도 있어!
*   **아이콘 변경:** `folium.Icon` 부분에서 `color`나 `icon`을 바꿔서 너만의 개성을 표현할 수도 있단다! `icon`에는 'star', 'info-sign', 'cloud' 등 다양한 아이콘을 쓸 수 있어!
""")
