import streamlit as st
from predict_page import show_predict_page
from details_page import show_details_page

"""with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
"""
st.markdown(
    """
    <style>
    * {
        background-color: #8d4141;
        border: 2px solid #CCCCCC;
        padding: 5% 5% 5% 10%;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

page = st.sidebar.selectbox("Details Or Predict", ("Predict", "Details"))

if page == "Predict":
    show_predict_page()
else:
    show_details_page()