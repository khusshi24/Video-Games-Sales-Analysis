import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout="wide",initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    .title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>Video Games Sales</h1>", unsafe_allow_html=True)
 
col1, col2 = st.columns(2)
 
with col1:
    st.write("Project Details:")
    st.write("""
             The objective of this project is to analyze and predict video game sales in Japan. This project includes exploratory data analysis (EDA) using different graphs to gain insights into the dataset. The analysis covers features such as platform, publisher, and genre to understand their impact on sales. The project also involves building predictive models, including Linear Regression, Random Forest Regression, and SVR, to predict video game sales. The models are evaluated using metrics like Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R-squared. The goal is to create a comprehensive analysis and prediction tool for video game sales in Japan.

             """)
with col2:
    file = st.file_uploader('Upload file', type=['csv'])
    if file is not None:
        df = pd.read_csv(file)
        st.session_state["df"] = df
    if st.button("Submit"):
        switch_page("page2")
 
    
