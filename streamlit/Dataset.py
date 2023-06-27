import streamlit as st 
import pandas as pd 
import plotly.express as px

df = pd.read_csv('../clean_data/salary-data.csv')

st.title('Dataset Introduction')
st.divider()

# DATASET
st.subheader('Dataset')
st.markdown("Data is obtained from a variety of sources, including surveys, job sites, and other publicly available sources. The dataset includes five variables: age, years_of_experience, job, education_level and salary. We have cleaned this dataset. Our clean data process includes renaming several column names, handle duplicated data, handle null values, & handle outliers")
st.write("Link to dataset <a href='https://www.kaggle.com/datasets/mohithsairamreddy/salary-data'> here</a>", unsafe_allow_html=True)
st.write(df)


# CLEAN DATA
st.subheader('The process of cleaning data')
st.markdown("These are some of the stages that we do in the clean data process. Resolve duplicate data, resolve null data, and resolve outliers")

# 1 
st.write("1. Resolve duplicate data")

cek_duplikat = '''# Cek data duplikat
data_new.duplicated().sum()'''

st.code(cek_duplikat, language='python')

hapus_duplikat = '''# Hapus data duplikat
data_new.drop_duplicates(inplace=True)'''

st.code(hapus_duplikat, language='python')

# 2
st.write("2. Resolve null data")

cek_null = '''# Cek Apakah ada null values
data_new.isnull().sum()'''

st.code(cek_null, language='python')

hapus_duplikat = '''# Menghapus baris data yang memilik null values
data_new.dropna(inplace=True)'''

st.code(hapus_duplikat, language='python')

# 3
st.write("3. Resolve Outlier")

batas = '''# Mencari batas MIN dan MAX kolom 'years_of_experience'
# Mencari Q1 dan Q3
Q1 = data_new['years_of_experience'].quantile(0.25)
Q3 = data_new['years_of_experience'].quantile(0.75)

# Mencari IQR(Interquartil Range)
IQR = Q3 - Q1

# Menentukan batas min dan max dalam IQR
batas_min = Q1 - 1.5 * IQR
batas_max = Q3 + 1.5 * IQR
print('batas min: ', batas_min)
print('batas max: ', batas_max)'''

st.code(batas, language='python')

cek_outlier = '''# Cek data outlier atas dan bawah kolom years_of_experienc
outlier_atas = []
outlier_bawah = []

for i in data_new['years_of_experience']:
    if (i < batas_min):
        outlier_bawah.append(i)
    if (i > batas_max):
        outlier_atas.append(i)

print('Outlier Atas: ',outlier_atas)
print('Outlier Bawah: ',outlier_bawah)'''

st.code(cek_outlier, language='python')

hapus_outlier = '''# Hapus data outlier kolom years_of_experience
yoe_clean = data_new[(data_new['years_of_experience'] >= batas_min) & (data_new['years_of_experience'] <= batas_max)]
'''

st.code(hapus_outlier, language='python')