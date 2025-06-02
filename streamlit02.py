import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("WHR2024.csv")

# Drop rows with missing year
df = df.dropna(subset=["Year"])

year = st.slider("Select Year", int(df["Year"].min()), int(df["Year"].max()), step=1)
filtered = df[df["Year"] == year]

fig = px.histogram(filtered, x="Ladder score", nbins=20, title=f"Happiness Scores in {year}")
st.plotly_chart(fig)
