import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("WHR2024.csv")
latest_year = df["Year"].max()
df_latest = df[df["Year"] == latest_year]

col1, col2 = st.columns(2)

with col1:
    st.subheader("GDP vs Happiness")
    fig1 = px.scatter(
        df_latest,
        x="Explained by: Log GDP per capita",
        y="Ladder score",
        hover_name="Country name",
        title="Log GDP vs Ladder Score"
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Social Support vs Happiness")
    fig2 = px.scatter(
        df_latest,
        x="Explained by: Social support",
        y="Ladder score",
        hover_name="Country name",
        title="Social Support vs Ladder Score"
    )
    st.plotly_chart(fig2, use_container_width=True)
