import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

#Import the US_Death_Counts data set
death_count = pd.read_csv('US_Death_Counts.csv')

st.write(death_count)

st.sidebar.header("Pick two variables for your scatterplot")
x_val = st.sidebar.selectbox("Pick your x-axis", death_count.select_dtypes(include=np.number).columns.tolist())
y_val = st.sidebar.selectbox("Pick your y-axis", death_count.select_dtypes(include=np.number).columns.tolist())

scatter = alt.Chart(death_count, title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val, title=f"{x_val}"),
    alt.Y(y_val, title=f"{y_val}"),
    tooltip=[x_val,y_val])

st.altair_chart(scatter, use_container_width=True)

#Calculate the correaltion
corr = round(death_count[x_val].corr(death_count[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")