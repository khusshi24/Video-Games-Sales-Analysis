import streamlit as st
import numpy as np
import pandas as pd
import os
import plotly.express as px
import plotly.graph_objects as go
from streamlit_extras.switch_page_button import switch_page
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

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

st.markdown("<h1 class='title'>Model Selection</h1>", unsafe_allow_html=True)

df = st.session_state["df"]
df2 = df.dropna()

top_publishers = df2['Publisher'].value_counts().nlargest(10).index.tolist()
df2['Publisher'] = df2['Publisher'].apply(lambda x: x if x in top_publishers else 'Other')

top_platforms = df2['Platform'].value_counts().nlargest(10).index.tolist()
df2['Platform'] = df2['Platform'].apply(lambda x: x if x in top_platforms else 'Other')

columns = ['ID','Name','Global_Sales']
df2.drop(columns=columns, inplace=True)

df_encoded = pd.get_dummies(df2, columns=['Platform'], prefix='Platform')
df_encoded = pd.get_dummies(df_encoded, columns=['Publisher'], prefix='Publisher')
df_encoded = pd.get_dummies(df_encoded, columns=['Genre'], prefix='Genre')

X = df_encoded.drop(columns='JP_Sales', axis=1)
y = df_encoded['JP_Sales']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

col1, col2 = st.columns(2)

with col1:
    selected_model = st.selectbox(
    'Select Model',
    ['Linear Regression', 'Random Forest Regression', 'SVR'])

    if selected_model == 'Linear Regression':
        model = LinearRegression()
    elif selected_model == 'Random Forest Regression':
        model = RandomForestRegressor()
    elif selected_model == 'SVR':
        model = SVR()
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    st.write("")
    st.write("")
    st.write("""
             The linear regression model has a moderate level of accuracy, as indicated by the R-squared value of 0.3921. The RMSE of 0.3067 shows that, on average, the model's predictions are about 0.3067 units away from the actual values.
The random forest regression model performs better than the linear regression model, with a higher R-squared value of 0.7313, indicating a better fit to the data. The RMSE of 0.2039 suggests that, on average, the model's predictions are about 0.2039 units away from the actual values.
The SVR model performs the worst among the three models, as indicated by the negative R-squared value of -0.0001, which suggests that the model does not fit the data well. The RMSE of 0.3934 shows that, on average, the model's predictions are about 0.3934 units away from the actual values.


             """)

with col2:
    st.write(f"#### Model: {selected_model}")
    st.write(f"##### MSE: {mse:.4f}")
    st.write(f"##### RMSE: {rmse:.4f}")
    st.write(f"##### R^2: {r2:.4f}")

    fig = px.scatter(x=y_test, y=y_pred, labels={'x': 'Actual Japan Sales', 'y': 'Predicted Japan Sales'}, title=f'Actual vs Predicted Japan Sales ({selected_model})')
    st.plotly_chart(fig)











