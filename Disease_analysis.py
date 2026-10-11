import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sm

st.title("🦠 Disease Analysis")

df = pd.read_csv("Dataset/state_disease_data.csv")
punjab = pd.read_csv("Dataset/punjab_district_data.csv")

st.write(
    "Explore disease patterns and their relationship with "
    "healthcare and socio-economic indicators."
)

diseases = [
    "diabetes_prevalence",
    "hypertension_prevalence",
    "obesity_prevalence",
    "anemia_women_prevalence",
    "tb_incidence_per_lakh",
    "diarrhea_under5_prevalence",
    "stunting_under5_prevalence"
]

st.divider()

st.subheader("🔥 Disease Pattern Across India")

selected = st.multiselect(
    "Select Diseases",
    diseases,
    default=diseases[:4]
)

heatmap_data = (
    df.groupby("state")[selected]
    .mean()
)

fig = px.imshow(
    heatmap_data,
    text_auto=".1f",
    aspect="auto",
    title="Disease Indicator Heatmap"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("📍 Punjab Disease Ranking")

disease = st.selectbox(
    "Select Disease",
    diseases
)

ranking = (
    punjab.groupby("district")[disease]
    .mean()
    .reset_index()
    .sort_values(disease, ascending=False)
)

fig2 = px.bar(
    ranking,
    x=disease,
    y="district",
    orientation="h",
    title=f"Punjab Districts — {disease}"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

st.subheader("🔎 Disease and Healthcare Relationship")

factor = st.selectbox(
    "Select Factor",
    [
        "doctor_density_per_10k",
        "hospital_beds_per_10k",
        "sanitation_access_pct",
        "safe_water_access_pct",
        "literacy_rate",
        "income_index"
    ]
)

fig3 = px.scatter(
    punjab,
    x=factor,
    y=disease,
    color="region",
    hover_name="district",
    trendline="ols",
    title=f"{disease} vs {factor}"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)