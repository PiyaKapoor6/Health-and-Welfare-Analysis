import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="Health & Welfare Dashboard",
    page_icon="🏥",
)

st.title("🏥 Health & Welfare Analysis")
st.write("A data-driven analysis of health disparities across India with a detailed focus on Punjab.")

st.divider()

df = pd.read_csv("Dataset/state_disease_data.csv")
punjab = pd.read_csv("Dataset/punjab_district_data.csv")

states = df["state"].nunique()
districts = punjab["district"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("🇮🇳 States / UTs", states)
c2.metric("📍 Punjab Districts", districts)
c3.metric("👥 Rural Records", len(df[df["region"] == "Rural"]))
c4.metric("🏙️ Urban Records", len(df[df["region"] == "Urban"]))

st.divider()

st.header("📊 Health Indicator Overview")

indicator = st.selectbox("Choose an indicator",[
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

summary = (df.groupby("state")[indicator].mean().sort_values(ascending=False).head(10).reset_index())

fig = px.bar(summary,x=indicator,y="state",orientation="h",title=f"Top 10 States — {indicator}",text=indicator)

fig.update_layout(yaxis_title="State",xaxis_title=indicator.replace("_", " ").title())

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.header("⚖️ Rural vs Urban Snapshot")

comparison = (
    df.groupby("region")[indicator]
    .mean()
    .reset_index()
)

fig2 = px.pie(
    comparison,
    names="region",
    values=indicator,
    hole=0.45,
    title=f"Rural vs Urban — {indicator}"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

st.header("🔄 How the Analysis Works")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("1️⃣ India")
    st.write("Compare health conditions across States and UTs.")

with col2:
    st.subheader("2️⃣ Punjab")
    st.write("Study Punjab at district level.")

with col3:
    st.subheader("3️⃣ Diseases")
    st.write("Identify disease patterns and related factors.")

with col4:
    st.subheader("4️⃣ Prediction")
    st.write("Use ML to predict health burden.")

st.divider()

st.header("💡 Welfare Perspective")

st.write(
    "The analysis can help highlight differences in healthcare "
    "conditions and identify regions that may need greater "
    "attention in healthcare planning and welfare initiatives."
)

st.success(
    "Use the navigation menu to explore the detailed analysis."
)