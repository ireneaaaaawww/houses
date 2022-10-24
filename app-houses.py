import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')


st.title('California Housing Data(1900) by Yayun Liu')
df = pd.read_csv('housing.csv')

price_filter = st.slider('Median House Price:', 0, 500001, 207000)  # min, max, default

# create a multi select
capital_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a radio
income_level = st.sidebar.radio('Choose income level:',('Low', 'Medium', 'High'))

# filter by population
df = df[df.median_house_value <= price_filter]

# filter by capital
if income_level == 'Low':
    df = df[df.median_income <= 2.5]
elif income_level == 'Mediun':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
else:
    df = df[df.median_income >= 2.5]

# show on map
st.map(df)

# show the plot
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(20, 10))
df.median_house_value.hist(ax=ax,bins=30)
st.pyplot(fig)