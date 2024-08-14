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

st.markdown("<h1 class='title'>Data Visualisation After Cleaning</h1>", unsafe_allow_html=True)

df = st.session_state["df"]
df2 = df
df2 = df2.drop(df2.index[0])
df2 = df.dropna()
print(df)

top_publishers = df2['Publisher'].value_counts().nlargest(10).index.tolist()
df2['Publisher'] = df2['Publisher'].apply(lambda x: x if x in top_publishers else 'Other')

top_platforms = df2['Platform'].value_counts().nlargest(10).index.tolist()
df2['Platform'] = df2['Platform'].apply(lambda x: x if x in top_platforms else 'Other')
    
col1, col2 = st.columns(2)
 
with col1:
    st.text("")
    st.text("")
    st.write("Data Summary:")
    st.write("""
             After conducting Exploratory Data Analysis (EDA), we aimed to analyse the number of games by different Publishers and Genres. Additionally, we examined video game sales by region over time. Furthermore, we investigated Global Sales by Publisher. We dropped the NA values from the dataset. For Publisher and Platform, we grouped the lesser performing ones into 'Other', and combined the rest into 'Other'. Notably, North America had the most sales, followed by Europe and Japan. From our analysis, we discovered that Nintendo has the highest sales, while Electronic Arts has produced the most games.
             """)
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    publisher_sales = df2.groupby('Publisher')['Global_Sales'].sum().reset_index()
    fig2 = px.bar(publisher_sales, x='Publisher', y='Global_Sales', title='Global Sales by Publisher')
    st.plotly_chart(fig2)

    st.write(pd.DataFrame(df2.isna().sum(), columns=['Missing Values']), df2.describe())


with col2:
    publisher_genre_counts = df2.groupby(['Publisher', 'Genre']).size().reset_index(name='Count')
    fig4 = px.bar(publisher_genre_counts, x='Publisher', y='Count', color='Genre',
             title='Number of Games by Publisher and Genre', 
             labels={'Count': 'Number of Games', 'Publisher': 'Publisher'},
             barmode='stack')
    fig4.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig4)

    sales_by_year = df2.groupby('Year')[['NA_Sales', 'EU_Sales', 'JP_Sales']].sum().reset_index()
    fig10 = px.line(sales_by_year, x='Year', y=['NA_Sales', 'EU_Sales', 'JP_Sales'],
              title='Video Game Sales by Region Over Time',
              labels={'Year': 'Year', 'value': 'Sales (in millions)', 'variable': 'Region'},
              color_discrete_map={'NA_Sales': 'blue', 'EU_Sales': 'green', 'JP_Sales': 'red'})
    st.plotly_chart(fig10)

    fig5 = px.box(
    df2, 
    x="Genre", 
    y="Global_Sales", 
    title="Video Game Sales by Genre")
    fig5.update_layout(xaxis_tickangle=45)
    st.plotly_chart(fig5)  

col1, col2, col3, col4, col5 = st.columns(5)

if col3.button('Go To Modelling'):
    switch_page("page4")


