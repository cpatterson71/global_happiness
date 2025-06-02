import streamlit as st
import pandas as pd

# load the dataset, filter the data for only the year 2023
df = pd.read_csv("WHR2024.csv")
df_2023 = df[df["Year"] == 2023]

# Get top 10 countries by Ladder score
top10 = df_2023.sort_values("Ladder score", ascending=False).head(10)

st.title("Top 10 Happiest Countries (2023)")
st.bar_chart(top10.set_index("Country name")["Ladder score"])
