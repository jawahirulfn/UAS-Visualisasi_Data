import streamlit as st
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv(r"../clean_data/salary-data.csv")

st.title("Data Analysis")

st.divider()

# Visualisasi top 5 pekerjaan
st.subheader("Top 5 Jobs")

st.markdown("Visualize the 5 most jobs based on datasets")

label_job = df['job']

count_job = df['job'].value_counts().head(5)

colors_job = [
    '#5C2E7E', 
    '#810CA8', 
    '#C147E9', 
    '#E5B8F4', 
    '#EEE9DA' ]

job_bar = go.Figure(
    data=go.Bar (
        x=label_job, 
        y=count_job, 
        marker=dict(color=colors_job), 
        width=0.5
    )
)

job_bar.update_layout (
    xaxis_title="Job", 
    yaxis_title="Number of workers"
)

st.plotly_chart(job_bar)

# Visualisasi Rata-rata gaji berdasarkan kategori
st.subheader('Salary Comparison by category')

st.markdown(f"Visualize a comparison of average salaries by selected category. There are 2 categories to choose from, namely 'gender' and 'education level'")

salary_factor = st.selectbox('Select Category: ', ['Gender', 'Education Level'])

if salary_factor == 'Gender':

    salary_mean = df.groupby(['gender']).mean().reset_index()

    color_salary = ['#DB005B', '#810CA8']
     
    salary_chart = go.Figure(
        data=go.Bar (
            x=salary_mean['gender'], 
            y=salary_mean['salary'], 
            width=0.4,
            marker=dict(color=color_salary)
        )
    )

    salary_chart.update_layout(
        title='Average Salary by Gender', 
        xaxis_title='Gender', 
        yaxis_title='Salary'
    )

    st.plotly_chart(salary_chart)

elif salary_factor == 'Education Level':

    salary_mean = df.groupby(['education_level']).mean().reset_index()

    salary_chart = px.bar(
        salary_mean, 
        x='education_level', 
        y='salary', 
        title='Salary comparison by education level', 
        color='education_level'
    )
        
    st.plotly_chart(salary_chart)

    st.table(salary_mean)

# Visualisasi Pekerja berdasarkan kategori
st.subheader('Workers by category')

st.markdown("Displays visualizations of workers by category. There are two categories to choose from: 'gender' and 'Education Level'")

workers_factor = st.selectbox('Select category : ', ['Gender', 'Education Level'])

if workers_factor == 'Gender':

    workers_count = df.groupby('gender').size().reset_index(name='count')

    label = workers_count['gender']

    value= workers_count['count']

    color_workers = ['#D14D72', '#7B2869'] 

    workers_chart = go.Figure(
        data=go.Pie(
            labels=label, 
            values=value,
            marker=dict(colors=color_workers)
        )
    )

    workers_chart.update_layout(title_text='Perbandingan pekerja berdasarkan gender')

    st.plotly_chart(workers_chart)

elif workers_factor == 'Education Level':

    workers_count = df.groupby('education_level').size().reset_index(name='count')

    label = workers_count['education_level']

    value = workers_count['count']

    color_workers = ['#7B2869', '#D14D72', '#C85C8E', '#FFBABA']

    workers_chart = go.Figure(
        data=go.Pie(
            labels=label,
            values=value,
            marker=dict(colors = color_workers)
        )
    )

    workers_chart.update_layout(title_text='Perbandingan karyawan berdasarkan tingkat pendidikan')
    
    st.plotly_chart(workers_chart)