import pandas as pd
import numpy as np
import streamlit as st

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
