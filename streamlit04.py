# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("WHR2024.csv")
df = df.dropna(subset=["Country name", "Year", "Ladder score"])

# Country selector
countries = sorted(df["Country name"].unique())
selected_country = st.selectbox("Select a Country", countries)

# Filter data by country
country_data = df[df["Country name"] == selected_country]

# Dynamically generate valid years for that country
years = sorted(country_data["Year"].unique())

# Year range slider (problematic if the country changes)
start_year, end_year = st.slider(
    "Select Year Range",
    min_value=int(min(years)),
    max_value=int(max(years)),
    value=(int(min(years)), int(max(years))),
    step=1
)

# Filter data based on year range
filtered = country_data[(country_data["Year"] >= start_year) & (country_data["Year"] <= end_year)]

# Plot
st.subheader(f"Happiness Score in {selected_country} ({start_year}–{end_year})")
fig = px.line(filtered, x="Year", y="Ladder score", markers=True)
st.plotly_chart(fig, use_container_width=True)
