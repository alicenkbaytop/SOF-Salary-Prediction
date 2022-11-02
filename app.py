import streamlit as st
from predict_page import show_predict_page
from details_page import show_details_page

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
page = st.sidebar.selectbox("Details Or Predict", ("Predict", "Details"))

if page == "Predict":
    show_predict_page()
else:
    show_details_page()