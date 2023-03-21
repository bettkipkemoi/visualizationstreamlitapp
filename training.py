import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px


#loading dataset
dataset1 = pd.read_csv("MP2_data_option1.csv")
dataset1.head(10)

#title
st.title('Exploring Some Random Dataset')

#chart 1
st.title('Age Distribution Trend')
Age = dataset1['Age'].value_counts()
st.line_chart(Age)
st.text('The line chart shows the trend of the data. Is it a good fit or we try bar chart?')
st.text('Lets go for the bar chart!')

#chart 2
st.title('Age Distribution Counts')
Age2 = dataset1['Age'].value_counts()
st.bar_chart(Age2)

#chart 3
df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.
    # This is the default. So you can also omit the theme argument.
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)