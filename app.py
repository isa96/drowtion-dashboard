# load libraries
import os
import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt 

plt.style.use('seaborn-dark-palette')

st.title('Dashboard Drowtion')
choosen_file = st.file_uploader('Input Logs File Here')

if choosen_file is not None:
    # read choosen logs file
    data = pd.read_csv(choosen_file, sep = ';', names = ['Eye', 'Mouth', 'X', 'Y', 'Z', 'Condition'])
    st.dataframe(data, height = 140)

    # metrics thresholding overview
    col_1, col_2, col_3 = st.columns(3)
    col_1.metric(label = "Eye Threshold", value = "%0.3f" % data['Eye'].loc[0])
    col_2.metric(label = "Mouth Threshold", value = "%0.3f" % data['Mouth'].loc[0])
    col_3.metric(label = "Head Threshold", value = "%0.3f" % data['Y'].loc[0])

    # Graph Visualisation
    st.write('Parameter Visualisation of Drowsy Detection')
    st.line_chart(data.iloc[:, [0, 1, 3]])

    st.write('Head Pose Angle Visualisation')
    st.line_chart(data.iloc[:, [2, 3, 4]])

    st.write('Condition Percentage Graph')
    try:
        fig, ax = plt.subplots()
        ax.bar(range(1, 5), data['Condition'].value_counts().values, color = ['#FF6464', '#FF9F45', '#00B4D8', '#8BDB81'])
        ax.set_xticks(range(1, 5), data.Condition.unique().tolist())
        st.pyplot(fig)
    except ValueError:
        st.error("Logs file not contain 'confidence' parameter, please try other logs file.")