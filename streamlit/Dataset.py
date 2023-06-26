import streamlit as st 
import pandas as pd 
import plotly.express as px

df = pd.read_csv('../clean_data/salary-data.csv')

st.title('Dataset Introduction')
st.divider()

# DATASET
st.subheader('Dataset')
st.markdown(" Data diperoleh dari berbagai sumber, termasuk survei, situs pekerjaan, dan sumber lain yang tersedia untuk umum. Dataset mencakup lima variabel: age, years_of_experience, job, education_level dan salary. Dataset ini sudah kami bersihkan / clean data. Proses clean data yang kami lakukan diantaranya mengubah nama beberapa nama kolom, handle duplicated data, handle null values, & handle outlier")
st.write("Link dataset <a href='https://www.kaggle.com/datasets/mohithsairamreddy/salary-data'> di sini</a>", unsafe_allow_html=True)
st.write(df)


# CLEAN DATA
st.subheader('Proses Clean Data')

# 1 
st.write("1. Mengatasi data duplikat")

cek_duplikat = '''# Cek data duplikat
data_new.duplicated().sum()'''

st.code(cek_duplikat, language='python')

hapus_duplikat = '''# Hapus data duplikat
data_new.drop_duplicates(inplace=True)'''

st.code(hapus_duplikat, language='python')

# 2
st.write("2. Mengatasi data null")

cek_null = '''# Cek Apakah ada null values
data_new.isnull().sum()'''

st.code(cek_null, language='python')

hapus_duplikat = '''# Menghapus baris data yang memilik null values
data_new.dropna(inplace=True)'''

st.code(hapus_duplikat, language='python')

# 3
st.write("3. Mengatasi Outlier")

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