# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from pymongo import MongoClient

# Connect to MongoDB
def get_data():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["whr_dashboard"]
    collection = db["happiness"]
    docs = list(collection.find({}, {"_id": 0}))
    data = pd.DataFrame(docs(collection.find()))
    return data

df = get_data()

# Load data
#df = pd.read_csv("WHR2024.csv")
#df = df.dropna(subset=["Country name", "Year", "Ladder score"])

years = sorted(df["Year"].unique())
df['Year'] = df['Year'].astype(int)  

st.title("World Happiness Scores by Country")

selected_year = st.slider("Select a year", min_value=min(years), max_value=max(years), value=max(years))
filtered = df[df["Year"] == selected_year]

# Country selector
#countries = sorted(df["Country name"].unique())
#selected_country = st.selectbox("Select a Country", countries)

# Filter data by country
#country_data = df[df["Country name"] == selected_country]

# Dynamically generate valid years for that country
#years = sorted(country_data["Year"].unique())

# Year range slider (problematic if the country changes)

#Choropleth map
fig = px.choropleth(
    filtered,
    locations="Country name",
    locationmode="country names",
    color="Ladder score",
    hover_name="Country name",
    color_continuous_scale=px.colors.sequential.Plasma,
    title=f"World Happiness Scores in {selected_year}"
)
fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True)
