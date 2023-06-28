import streamlit as st 
import pandas as pd 
import plotly.express as px

df = pd.read_csv('../clean_data/salary-data.csv')

st.title('Dataset Introduction')
st.divider()

# DATASET
st.subheader('Dataset')
st.markdown("Data is obtained from a variety of sources, including surveys, job sites, and other publicly available sources. The dataset includes five variables: age, years_of_experience, job, education_level and salary. We have cleaned this dataset. Our clean data process includes renaming several column names, handle duplicated data, handle null values, & handle outliers")
st.write("Dataset : ""[salary data](https://www.kaggle.com/datasets/mohithsairamreddy/salary-data)")
st.write("Project : ""[Github](https://github.com/jawahirulfn/UAS-Visualisasi_Data)")
st.write(df)
