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
    title='Top 5 job'
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
        x=salary_mean['education_level'], 
        y=salary_mean['salary'], 
        title='Salary comparison by education level', 
        color='education_level'
    )

    salary_chart.update_layout(
        title = 'Average salary by education level', 
        xaxis_title='Education Level', 
        yaxis_title='Salary'
    )
        
    st.plotly_chart(salary_chart)

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