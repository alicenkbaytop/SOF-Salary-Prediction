import streamlit as st
from predict_page import show_predict_page
from details_page import show_details_page

page = st.sidebar.selectbox("Predict Or Details", ("Predict", "Details"))

if page == "Predict":
    show_predict_page()
else:
    show_details_page()