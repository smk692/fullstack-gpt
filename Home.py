import streamlit as st

from datetime import datetime

st.set_page_config(
    page_title="FullstackGPT Home",
    page_icon="🤖",
)

today = datetime.today().strftime("%H:%M:%S")

with st.sidebar:
    st.title('손(손민기/Son) LMM 공부중')
    st.write(today)

st.markdown(
    """
# Hello!
            
Welcome to my FullstackGPT Portfolio!
            
Here are the apps I made:
            
- [x] [📃 DocumentGPT](/DocumentGPT)
- [x] [🔒 PrivateGPT](/PrivateGPT)
- [x] [❓ QuizGPT](/QuizGPT)
- [x] [🖥️ SiteGPT](/SiteGPT)
- [x] [💼 MeetingGPT](/MeetingGPT)
- [x] [📈 InvestorGPT](/InvestorGPT)
"""
)
