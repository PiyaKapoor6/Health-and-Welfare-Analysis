import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("📍 Detailed Punjab Health Analysis")

df = pd.read_csv("Dataset/punjab_district_data.csv")

st.write(
    "Detailed analysis of health, healthcare infrastructure and welfare "
    "indicators across Punjab districts."
)

st.divider()

district = st.selectbox(
    "Select District",
    sorted(df["district"].unique())
)

data = df[df["district"] == district]

row = data.iloc[0]

c1, c2, c3, c4 = st.columns(4)

c1.metric("Literacy", f"{row['literacy_rate']:.1f}%")
c2.metric("Sanitation", f"{row['sanitation_access_pct']:.1f}%")
c3.metric("Safe Water", f"{row['safe_water_access_pct']:.1f}%")
c4.metric("Doctors / 10k", f"{row['doctor_density_per_10k']:.1f}")

st.divider()

st.subheader(f"📊 Health Profile of {district}")

profile = pd.DataFrame({
    "Indicator": [
        "Literacy",
        "Sanitation",
        "Safe Water",
        "Doctor Availability",
        "Hospital Beds"
    ],
    "Value": [
        row["literacy_rate"],
        row["sanitation_access_pct"],
        row["safe_water_access_pct"],
        row["doctor_density_per_10k"],
        row["hospital_beds_per_10k"]
    ]
})

fig = px.line_polar(
    profile,
    r="Value",
    theta="Indicator",
    line_close=True,
    markers=True,
    title=f"{district} Health Profile"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("🏆 Punjab District Comparison")

indicator = st.selectbox(
    "Select Indicator",
    [
        "literacy_rate",
        "sanitation_access_pct",
        "safe_water_access_pct",
        "doctor_density_per_10k",
        "hospital_beds_per_10k",
        "income_index"
    ]
)

districts = (
    df.groupby("district")[indicator]
    .mean()
    .reset_index()
    .sort_values(indicator, ascending=False)
)

fig2 = px.bar(
    districts,
    x="district",
    y=indicator,
    title=f"Punjab Districts — {indicator}"
)

fig2.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("⚖️ Rural vs Urban")

fig3 = px.bar(
    data,
    x="region",
    y=[
        "literacy_rate",
        "sanitation_access_pct",
        "safe_water_access_pct"
    ],
    barmode="group",
    title=f"{district} — Rural vs Urban"
)

st.plotly_chart(fig3, use_container_width=True)