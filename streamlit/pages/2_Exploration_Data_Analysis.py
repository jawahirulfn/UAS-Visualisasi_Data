import streamlit as st
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv(r"../clean_data/salary-data.csv")

st.title("Exploration Data Analysis")
st.divider()

# Visualisasi top 5 pekerjaan
st.subheader("Top 5 Jobs")
st.markdown("Visualize the 5 most jobs based on datasets")

label_job = df['job']
count_job = df['job'].value_counts().head(5)

colors_job = [
    '#884A39', 
    '#C38154', 
    '#FFC26F', 
    '#F9E0BB', 
    '#EEE9DA']

job_bar = go.Figure(
    data=go.Bar(
        x=label_job, 
        y=count_job, 
        marker=dict(color=colors_job), 
        width=0.5))

job_bar.update_layout(
    xaxis_title="Job", 
    yaxis_title="Number of workers")

st.plotly_chart(job_bar)

# Rata-rata gaji berdasarkan kategori
st.subheader('Salary Comparison by category')
st.markdown(f"Visualize a comparison of average salaries by selected category. There are 2 categories to choose from, namely 'gender' and 'education level'")

salary_factor = st.selectbox('Select Category: ', ['gender', 'education_level'])

if salary_factor == 'gender':
    salary_mean = df.groupby(['gender']).mean().reset_index()
    salary_chart = px.bar(
        salary_mean, 
        x='gender', 
        y='salary', 
        title='Salary comparison by gender', 
        color='gender')
    st.plotly_chart(salary_chart)

elif salary_factor == 'education_level':
    salary_mean = df.groupby(['education_level']).mean().reset_index()
    salary_chart = px.bar(
        salary_mean, 
        x='education_level', 
        y='salary', 
        title='Salary comparison by education level', 
        color='education_level')
    st.plotly_chart(salary_chart)

