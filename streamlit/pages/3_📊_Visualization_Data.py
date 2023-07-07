import streamlit as st
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/jawahirulfn/UAS-Visualisasi_Data/main/clean_data/salary-data.csv')

st.title("Data Analysis")

st.markdown('In data analysis we use clean data. We clean data by several processes including handling null data, handling data duplication, and handling outliers.')

st.divider()

st.sidebar.markdown('''
> Section
1. [Top 5 Jobs](#top-5-jobs)
2. [Salary Comparison by category](#salary-comparison-by-category)
3. [Workers by category](#workers-by-category)
4. [Workers Education level by Gender](#workers-education-level-by-gender)
''', unsafe_allow_html=True)

# Visualisasi top 5 
st.header("Top 5 Jobs")

st.markdown("Visualize the top 5 by category")

job_factor = st.selectbox('Select Category : ', ['top 5 job by salary', 'Top 5 popular job'])

if job_factor == 'top 5 job by salary':
    
    salary_job = df.groupby(['job']).mean().reset_index().sort_values('salary').tail(5)

    salary_job_chart = px.bar(
        salary_job, 
        x=salary_job['job'], 
        y=salary_job['salary'],
        color='job',
        color_discrete_map= {
            'Director of Data Science' : '#FEE0C0',
            'VP of Finance' : '#FF7C7C',
            'Chief Data Officer' : '#BE5A83',
            'Chief Technology Officer' : '#B9005B' ,
            'CEO' : '#804674'
        }
    )

    salary_job_chart.update_layout(title='Top 5 Job by Salary')

    st.plotly_chart(salary_job_chart)

elif job_factor == 'Top 5 popular job':

    count_job = df['job'].value_counts().head(5).reset_index(name='count').rename(columns={'index' : 'job'})

    job_bar = px.bar (
    count_job, 
    x=count_job['job'], 
    y=count_job['count'], 
    color='job',
    color_discrete_map = {
        'Full Stack Engineer' : '#5C2E7E',
        'Software Engineer Manager' : '#810CA8',
        'Senior Project Engineer' : '#C147E9',
        'Senior Software Engineer' : '#E5B8F4',
        'Data Scientist' : '#EEE9DA'
    }
    )

    job_bar.update_layout(
    xaxis_title='Job', 
    yaxis_title='Number Of Workesr', 
    title='Top 5 Popular Job'
    )

    st.plotly_chart(job_bar)

# Visualisasi Rata-rata gaji berdasarkan kategori
st.header('Salary Comparison by category')

st.markdown(f"Visualize a comparison of average salaries by selected category. There are 2 categories to choose from, namely 'gender' and 'education level'")

salary_factor = st.selectbox('Select Category: ', ['Gender', 'Education Level'])

if salary_factor == 'Gender':

    salary_mean = df.groupby('gender').mean().reset_index()

    salary_chart = px.bar(
        salary_mean,
        x=salary_mean['gender'],
        y=salary_mean['salary'],
        width=580,
        color='gender',
        color_discrete_map={'Female' : '#AF0171', 'Male' : '#FF7C7C'}
    )

    salary_chart.update_layout(title='Average Salary by Gender')

    st.plotly_chart(salary_chart)
   

elif salary_factor == 'Education Level':

    salary_mean = df.groupby('education_level').mean().reset_index()
    
    salary_chart = px.bar(
        salary_mean, 
        x=salary_mean['education_level'], 
        y=salary_mean['salary'], 
        title='Salary comparison by education level', 
        color='education_level',
        color_discrete_map={
            "Bachelor's" : '#FF7C7C',
            "High School" : '#FEE0C0',
            "Master's" : '#BE5A83',
            "phD" : '#B9005B'}
    )

    salary_chart.update_layout(
        title = 'Average salary by Education Level', 
        xaxis_title='Education Level', 
        yaxis_title='Salary'
    )
        
    st.plotly_chart(salary_chart)

# Visualisasi Pekerja berdasarkan kategori
st.header('Workers by category')

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

    workers_chart.update_layout(title_text='Comparison of workers by gender')

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

    workers_chart.update_layout(title_text='Comparison of workers by education level')
    
    st.plotly_chart(workers_chart)

st.header('Workers Education level by Gender')

st.write('Visualize comparison education level by gender')

education_count = df.groupby(['gender', 'education_level']).size().reset_index(name='count')

edu_chart = px.bar(
    education_count, 
    x='education_level', 
    y='count', 
    color='gender', 
    color_discrete_map={
        "Male" : '#FEE0C0',
        "Female" : '#B9005B',},
    title='Comparison education level by gender',
    barmode='group'
    )

st.plotly_chart(edu_chart)