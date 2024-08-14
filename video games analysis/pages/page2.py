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

st.markdown("<h1 class='title'>Data Visualisation Before Cleaning</h1>", unsafe_allow_html=True)

df = st.session_state["df"]
    
col1, col2 = st.columns(2)
 
with col1:
    st.text("")
    st.text("")
    st.write("Data Summary:")
    st.write("""
             The video game dataset is originally from kaggle.com and contains data on video games with sales in different regions. Each row of the dataset corresponds to a video game. Attributes include 'Name' (game title), 'Platform' (sales platform), 'Year' (release year for trend analysis), 'Genre' (game genre), 'Publisher' (game publisher for performance assessment), 'NA_Sales', 'EU_Sales', 'JP_Sales' (sales figures for regional insights), and 'Global_Sales' (total global sales for overall success evaluation). Each video game has sales (in millions), and sales data is specifically available for North America, Europe and Japan. Other columns in the dataset detail a video game’s name, platform of release, year of release, genre, and publisher. Platforms of release include platforms such as the Wii, PS4, PC, etc. The year of release ranges from 1980 to 2020. There are 12 unique genres (including a miscellaneous category) and several unique publishers in the dataset, with the most common publisher being Electronic Arts.

             """)
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
 

    publisher_sales = df.groupby('Publisher')['Global_Sales'].sum().reset_index()
    fig2 = px.bar(publisher_sales, x='Publisher', y='Global_Sales', title='Global Sales by Publisher')
    st.plotly_chart(fig2)

    st.write(pd.DataFrame(df.isna().sum(), columns=['Missing Values']), df.describe())

with col2:
    publisher_genre_counts = df.groupby(['Publisher', 'Genre']).size().reset_index(name='Count')
    fig4 = px.bar(publisher_genre_counts, x='Publisher', y='Count', color='Genre',
             title='Number of Games by Publisher and Genre', 
             labels={'Count': 'Number of Games', 'Publisher': 'Publisher'},
             barmode='stack')
    fig4.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig4)

    sales_by_year = df.groupby('Year')[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum().reset_index()
    fig10 = px.line(sales_by_year, x='Year', y=['NA_Sales', 'EU_Sales', 'JP_Sales'],
              title='Video Game Sales by Region Over Time',
              labels={'Year': 'Year', 'value': 'Sales (in millions)', 'variable': 'Region'},
              color_discrete_map={'NA_Sales': 'blue', 'EU_Sales': 'green', 'JP_Sales': 'red'})
    st.plotly_chart(fig10)

    fig5 = px.box(
    df, 
    x="Genre", 
    y="Global_Sales", 
    title="Video Game Sales by Genre")
    fig5.update_layout(xaxis_tickangle=45)
    st.plotly_chart(fig5)

col1, col2, col3, col4, col5 = st.columns(5)

if col3.button('Clean Data'):
    switch_page("page3")


