import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("🇮🇳 Indian States Health Comparison")

df = pd.read_csv("Dataset/state_disease_data.csv")
rhs05 = pd.read_csv("Dataset/rhs_2005.csv")
rhs19 = pd.read_csv("Dataset/rhs_2019.csv")
india = pd.read_csv("Dataset/india_rural_urban_health_2022.csv")

st.write("Compare health conditions and healthcare resources across Indian States and UTs.")

st.divider()

indicator = st.selectbox(
    "Select Health Indicator",
    [
        "diabetes_prevalence",
        "hypertension_prevalence",
        "obesity_prevalence",
        "anemia_women_prevalence",
        "tb_incidence_per_lakh",
        "infant_mortality_rate",
        "sanitation_access_pct",
        "healthcare_access_index"
    ]
)

state_data = df.groupby("state")[indicator].mean().reset_index()

heatmap_data = state_data.set_index("state")[[indicator]]

fig = px.imshow(
    heatmap_data,
    labels={
        "x": "Health Indicator",
        "y": "State",
        "color": indicator
    },
    aspect="auto",
    color_continuous_scale="RdYlGn_r",
    title=f"Health Comparison Across Indian States — {indicator}"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("🏆 State Ranking")

ranking = state_data.sort_values(
    indicator,
    ascending=False
).head(10)

fig2 = px.bar(
    ranking,
    x=indicator,
    y="state",
    orientation="h",
    title=f"Top 10 States — {indicator}"
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("👨‍⚕️ Rural vs Urban Doctors")

doctor_data = india[
    [
        "State_UT",
        "Rural_Doctors_at_PHCs_2022",
        "Urban_Doctors_at_PHCs_2022"
    ]
].dropna()

fig3 = px.bar(
    doctor_data,
    x="State_UT",
    y=[
        "Rural_Doctors_at_PHCs_2022",
        "Urban_Doctors_at_PHCs_2022"
    ],
    barmode="group",
    title="Doctors at Primary Health Centres"
)

fig3.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

st.subheader("🏥 Healthcare Infrastructure Change")

state = st.selectbox(
    "Select State",
    sorted(rhs05["State/UT"].dropna().unique())
)

old = rhs05[rhs05["State/UT"] == state].iloc[0]
new = rhs19[rhs19["State/UT"] == state].iloc[0]

infrastructure = pd.DataFrame({
    "Year": [2005, 2019],
    "Doctors": [old["Doctors"], new["Doctors"]],
    "PHCs": [old["PHCs"], new["PHCs"]],
    "CHCs": [old["CHCs"], new["CHCs"]]
})

metric = st.selectbox(
    "Select Infrastructure",
    ["Doctors", "PHCs", "CHCs"]
)

fig4 = px.line(
    infrastructure,
    x="Year",
    y=metric,
    markers=True,
    title=f"{metric} — {state}"
)

st.plotly_chart(fig4, use_container_width=True)