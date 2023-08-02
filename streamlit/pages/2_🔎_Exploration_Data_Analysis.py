import streamlit as st 
import pandas as pd 
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/jawahirulfn/UAS-Visualisasi_Data/main/dataset/Salary_Data.csv')

st.title('Exploration Data Analysis')

# DATA INFO
st.header('Data Information')

st.write('includes various information such as the amount of data, average, standard deviation, minimum value, quartile, and maximum value.')

st.write(df.describe())

# HISTOGRAM CHART
st.header('Histogram')

histogram_chart = st.selectbox('Select column to visualization to histogram chart: ', ['Age', 'Salary', 'Years of Experience'])

if histogram_chart == 'Age':
    chart = px.histogram(df, x='Age', color_discrete_sequence=['#B9005B'])
    st.plotly_chart(chart)

elif histogram_chart == 'Salary':
    chart = px.histogram(df, x='Salary', color_discrete_sequence=['#3FA796'])
    st.plotly_chart(chart)

elif histogram_chart == 'Years of Experience':
    chart = px.histogram(df, x='Years of Experience')
    st.plotly_chart(chart)


# BOXPLOT
st.header('Boxplot')

st.write('To analyze the data in the column, there are outliers or not')

boxplot_chart = st.selectbox('Select column to visualize in boxplot :', ['Age', 'Salary', 'Years of Experience'])

if boxplot_chart == 'Age':
    chart = px.box(df, title='Boxplot Age', x='Age', color_discrete_sequence=['#B9005B'])
    st.plotly_chart(chart)

elif boxplot_chart =='Salary':
    chart = px.box(df, title='Boxplot Salary', x='Salary',color_discrete_sequence=['#3FA796'])
    st.plotly_chart(chart)

elif boxplot_chart =='Years of Experience':
    chart = px.box(df, title='Boxplot Years of Experience', x='Years of Experience')
    st.plotly_chart(chart)

# SCATTER PLOT
st.header('Scatter Plot')

scatter_plot = st.selectbox('Select Scatter : ', ['age vs salary', 'age vs years of experience', 'salary vs years of experience'])

if scatter_plot == 'age vs salary':
    chart = px.scatter(df, x='Age', y='Salary', title='Age vs Salary')
    st.plotly_chart(chart)

elif scatter_plot == 'age vs years of experience':
    chart = px.scatter(df, x='Age', y='Years of Experience', title='Age vs Years of Experience')
    st.plotly_chart(chart)

elif scatter_plot == 'salary vs years of experience':
    chart = px.scatter(df, x='Salary', y='Years of Experience', title='Salary vs Years of Experience')
    st.plotly_chart(chart)