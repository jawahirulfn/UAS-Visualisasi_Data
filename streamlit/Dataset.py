import streamlit as st 
import pandas as pd 
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/jawahirulfn/UAS-Visualisasi_Data/main/dataset/Salary_Data.csv')

st.title('Dataset Introduction')
st.divider()

# DATASET
st.subheader('Dataset')
st.markdown("Data is obtained from a variety of sources, including surveys, job sites, and other publicly available sources. The dataset includes five variables: Age, Gender, Education Level, Job Title, Years of Experience and Salary. ")
st.write("Dataset : ""[salary data](https://www.kaggle.com/datasets/mohithsairamreddy/salary-data)")
st.write("Project : ""[Github](https://github.com/jawahirulfn/UAS-Visualisasi_Data)")
st.write(df)
