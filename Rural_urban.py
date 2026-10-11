import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("⚖️ Rural vs Urban Health Analysis")

state_df = pd.read_csv("Dataset/state_disease_data.csv")
punjab_df = pd.read_csv("Dataset/punjab_district_data.csv")
india_df = pd.read_csv("Dataset/india_rural_urban_health_2022.csv")

st.write(
    "A detailed comparison of rural and urban health conditions "
    "using state-level and Punjab-level data."
)

st.divider()

st.header("🇮🇳 India")

indicator = st.selectbox(
    "Select India Indicator",
    [
        "diabetes_prevalence",
        "hypertension_prevalence",
        "obesity_prevalence",
        "anemia_women_prevalence",
        "tb_incidence_per_lakh",
        "diarrhea_under5_prevalence",
        "stunting_under5_prevalence",
        "infant_mortality_rate",
        "sanitation_access_pct",
        "healthcare_access_index"
    ]
)

india_comparison = (
    state_df.groupby("region")[indicator]
    .mean()
    .reset_index()
)

fig = px.bar(
    india_comparison,
    x="region",
    y=indicator,
    text=indicator,
    title=f"India Rural vs Urban — {indicator}"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.header("📍 Punjab")

punjab_indicator = st.selectbox(
    "Select Punjab Indicator",
    [
        "literacy_rate",
        "sanitation_access_pct",
        "safe_water_access_pct",
        "doctor_density_per_10k",
        "hospital_beds_per_10k",
        "income_index",
        "diabetes_prevalence",
        "hypertension_prevalence",
        "cancer_incidence_per_lakh",
        "respiratory_disease_prevalence",
        "anemia_women_prevalence",
        "infant_mortality_rate"
    ]
)

punjab_comparison = (
    punjab_df.groupby("region")[punjab_indicator]
    .mean()
    .reset_index()
)

fig2 = px.bar(
    punjab_comparison,
    x="region",
    y=punjab_indicator,
    text=punjab_indicator,
    title=f"Punjab Rural vs Urban — {punjab_indicator}"
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.header("👨‍⚕️ Doctor Availability")

doctor_data = india_df[
    [
        "State_UT",
        "Rural_Doctors_at_PHCs_2022",
        "Urban_Doctors_at_PHCs_2022"
    ]
].dropna()

doctor_data["Doctor_Gap"] = (
    doctor_data["Urban_Doctors_at_PHCs_2022"]
    -
    doctor_data["Rural_Doctors_at_PHCs_2022"]
)

fig3 = px.bar(
    doctor_data.sort_values("Doctor_Gap"),
    x="State_UT",
    y="Doctor_Gap",
    title="Urban Doctors − Rural Doctors"
)

fig3.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

st.header("💡 Interpretation")

st.info(
    "Rural-urban differences help identify disparities in "
    "healthcare availability and health indicators. These "
    "differences indicate patterns in the data."
)