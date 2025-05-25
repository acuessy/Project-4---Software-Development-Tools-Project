import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('vehicles_us.csv')

# Clean model_year
df = df[df['model_year'].notna()]
df['model_year'] = df['model_year'].astype(int)

# App layout
st.header("Used Car Listings Dashboard")

# Histogram
st.subheader("Distribution of Car Prices")
fig1 = px.histogram(df, x='price', nbins=50)
st.plotly_chart(fig1)

# Scatter plot
st.subheader("Price vs. Odometer (by Type)")
fig2 = px.scatter(df, x='odometer', y='price', color='type')
st.plotly_chart(fig2)

# Checkbox
if st.checkbox("Only show cars with under 100,000 miles"):
    filtered = df[df['odometer'] < 100000]
    fig3 = px.scatter(filtered, x='odometer', y='price', color='type')
    st.subheader("Filtered (Under 100K Miles)")
    st.plotly_chart(fig3)
