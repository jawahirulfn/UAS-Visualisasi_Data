import streamlit as st 
import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('../clean_data/salary-data.csv')

st.title('Statistik Deskriptif')

# DATA INFO
st.header('Data Info')

st.write('includes various information such as the amount of data, average, standard deviation, minimum value, quartile, and maximum value.')

st.write(df.describe())

# HISTOGRAM CHART
st.header('Histogram')

histogram_chart = st.selectbox('Select column to visualization to histogram chart: ', ['age', 'salary', 'years of experience'])

if histogram_chart == 'age':
    chart = px.histogram(df, x='age', color_discrete_sequence=['#B9005B'])
    st.plotly_chart(chart)

elif histogram_chart == 'salary':
    chart = px.histogram(df, x='salary', color_discrete_sequence=['#3FA796'])
    st.plotly_chart(chart)

elif histogram_chart == 'years of experience':
    chart = px.histogram(df, x='years_of_experience')
    st.plotly_chart(chart)


# BOXPLOT
st.header('Boxplot')

st.write('To analyze the data in the column, there are outliers or not')

boxplot_chart = st.selectbox('Select column to visualize in boxplot :', ['age', 'salary', 'years of experience'])

if boxplot_chart == 'age':
    chart = px.box(df, title='Boxplot Age', x='age', color_discrete_sequence=['#B9005B'])
    st.plotly_chart(chart)

elif boxplot_chart =='salary':
    chart = px.box(df, title='Boxplot Salary', x='salary',color_discrete_sequence=['#3FA796'])
    st.plotly_chart(chart)

elif boxplot_chart =='years of experience':
    chart = px.box(df, title='Boxplot Years of Experience', x='years_of_experience')
    st.plotly_chart(chart)

# SCATTER PLOT
st.header('Scatter Plot')

scatter_plot = st.selectbox('Select Scatter : ', ['age vs salary', 'age vs years of experience', 'salary vs years of experience'])

if scatter_plot == 'age vs salary':
    chart = px.scatter(df, x='age', y='salary', title='Age vs Salary')
    st.plotly_chart(chart)

elif scatter_plot == 'age vs years of experience':
    chart = px.scatter(df, x='age', y='years_of_experience', title='Age vs Years of Experience')
    st.plotly_chart(chart)

elif scatter_plot == 'salary vs years of experience':
    chart = px.scatter(df, x='salary', y='years_of_experience', title='Salary vs Years of Experience')
    st.plotly_chart(chart)