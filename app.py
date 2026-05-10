import streamlit as st
import requests

# مفتاحك الذهبي
API_KEY = "4f74f8c769e012d50f70c0fe7e344070"

st.set_page_config(page_title="المحلل المحترف Live", layout="wide")

def get_live():
    url = "https://v3.football.api-sports.io/fixtures?live=all"
    headers = {'x-rapidapi-key': API_KEY, 'x-rapidapi-host': 'v3.football.api-sports.io'}
    try:
        response = requests.get(url, headers=headers)
        return response.json().get('response', [])
    except:
        return []

st.title("⚽ مركز المباريات المباشرة")

matches = get_live()

if not matches:
    st.info("حالياً ماكو مباريات مباشرة.. الموقع يتحدث أول ما تبدي اللعبة.")
else:
    for m in matches:
        st.markdown(f"""
        <div style="background:#1e293b; padding:20px; border-radius:15px; margin-bottom:10px; border-right:5px solid #3b82f6; direction:rtl; color:white;">
            <h3>{m['teams']['home']['name']} {m['goals']['home']} - {m['goals']['away']} {m['teams']['away']['name']}</h3>
            <p style="color:#ef4444;">الدقيقة: {m['fixture']['status']['elapsed']}' ⏱️</p>
        </div>
        """, unsafe_allow_html=True)
