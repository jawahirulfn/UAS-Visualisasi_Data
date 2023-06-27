import streamlit as st
import pandas as pd 
import numpy as np
from PIL import Image

#EDA
salary = pd.read_csv("salary-data.csv")

@st.cache
def load_data(nrows):
    data = pd.read_csv('salary-data.csv', nrows=nrows)
    return data

option = st.sidebar.radio(
    'Silakan pilih:',
    ('Home','Dataframe','Chart'));

if option == 'Home' or option == '':
    st.title('APLIKASI GAJI PEGAWAI');
    st.image("salary.jpg", width=400, use_column_width=False)
    st.markdown('A The dataset was obtained from multiple sources, including surveys, job posting sites, and other publicly available sources.A total of 1751 data points were collected.The dataset included fivevariables: age, experience, job role, and education level and salary')
    st.write("Source: ""[salary-data](https://www.kaggle.com/datasets/mohithsairamreddy/salary-data)")

    st.subheader("Data gaji pegawai")
    st.dataframe(salary)

    df = pd.DataFrame(
        {
            "Variabel": ["Age", "Gender", "Education Level", "Job Title", "Years of Experience", "Salary"],
            "Information": ["Age of Employeer", "Gender of Employeer", "Education Level of Employeer", "Role of Experience", "Experience of Employeer", "Monthly Salary"],
        })
    st.dataframe(df)

elif option == 'Dataframe':
    st.write("""## Dataframe""") #menampilkan judul halaman dataframe

    if st.checkbox("Show Shape"):
        st.write(salary.shape)

    if st.checkbox("Show Columns"):
        all_columns = salary.columns.to_list()
        st.write(all_columns)

    if st.checkbox("Show Selected Columns"):
        selected_columns = st.multiselect("Select Columns", all_columns)
        new_data = salary[selected_columns]
        st.dataframe(new_data)

    if st.checkbox("Show Value Counts"):
        st.write(salary.iloc[:, -1].value_counts())

    if st.checkbox("Correlation Plot(Matplotlib)"):
        plt.matshow(salary.corr())
        st.pyplot()

    if st.checkbox("Correlation Plot(Seaborn)"):
        st.write(sns.heatmap(salary.corr(), annot=True, cmap='coolwarm'))
        st.pyplot()

    if st.checkbox("Pie Plot"):
        all_columns = salary.columns.to_list()
        column_to_plot = st.selectbox("Select 1 Column", all_columns)
        if salary[column_to_plot].dtype == object:
            pie_plot = salary[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
            st.write(pie_plot)
            st.pyplot()

    all_columns_names = salary.columns.tolist()
    type_of_plot = st.selectbox("Select Type of Plot", ["area", "bar", "line", "hist", "box", "kde"])
    selected_columns_names = st.multiselect("Select Columns To Plot", all_columns_names)

    if st.button("Generate Plot"):
        st.success("Generating Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names))

    if type_of_plot == 'area':
        numeric_columns = salary.select_dtypes(include='number').columns.tolist()
        selected_numeric_columns = [col for col in selected_columns_names if col in numeric_columns]

        if len(selected_numeric_columns) >= 2:
            x_column = selected_numeric_columns[0]
            y_columns = selected_numeric_columns[1:]
            cust_data = salary[selected_numeric_columns]
            st.area_chart(cust_data.set_index(x_column))
    

    elif type_of_plot == 'bar':
        non_numeric_columns = salary.select_dtypes(exclude='number').columns.tolist()
        selected_non_numeric_columns = [col for col in selected_columns_names if col in non_numeric_columns]

        if len(selected_non_numeric_columns) >= 1:
            for col in selected_non_numeric_columns:
                bar_plot = salary[col].value_counts().plot.bar()
                st.write(bar_plot)
                st.pyplot()

        elif type_of_plot:
            cust_data = salary[selected_columns_names]
            st.write(cust_data.plot(kind=type_of_plot))
            st.pyplot()


































































    
elif option == 'Chart':
    st.write("""## Draw Charts""") #menampilkan judul halaman 

    option = st.selectbox(
    'Category',
    ('All Category', 'Age', 'Gender', 'Education Level', 'Job Title', 'Years of Experience', 'Salary'))
    
    col1, col2 = st.columns(2)
    with col1:
        option = st.selectbox(
        "chart",
        ("Age", "Gender", "Education Level", "Job Title", "Years of Experience", "Salary"))

    with col2:
        option = st.selectbox(
        "bloxplot",
        ("Age", "Gender", "Education Level", "Job Title", "Years of Experience", "Salary"),
        )
    
    

    



