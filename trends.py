import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("📈 Health Trends")

df = pd.read_csv("Dataset/punjab_trends.csv")

st.write(
    "This page analyzes how health and disease indicators "
    "change over time in Punjab."
)

st.divider()

st.subheader("📈 Indicator Trend")

indicator = st.selectbox(
    "Select Indicator",
    sorted(df["disease"].unique())
)

data = df[df["disease"] == indicator].copy()

fig = px.line(
    data,
    x="year",
    y="value",
    color="region",
    markers=True,
    title=f"{indicator.replace('_', ' ').title()} Over Time"
)

fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Value"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("📊 Overall Change")

start = data.groupby("region").first().reset_index()
end = data.groupby("region").last().reset_index()

change = start[["region", "value"]].copy()

change["Final Value"] = end["value"].values
change["Change"] = change["Final Value"] - change["value"]
change["Change"] = change["Change"].round(2)

fig2 = px.bar(
    change,
    x="region",
    y="Change",
    text="Change",
    title="Change Between First and Last Available Year"
)

fig2.update_layout(
    xaxis_title="Region",
    yaxis_title="Change"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

st.subheader("⚖️ Rural vs Urban Trend")

fig3 = px.area(
    data,
    x="year",
    y="value",
    color="region",
    markers=True,
    title=f"Rural vs Urban — {indicator.replace('_', ' ').title()}"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.divider()

st.subheader("📋 Trend Data")

st.dataframe(
    data,
    use_container_width=True,
    hide_index=True
)

st.divider()

if len(data) >= 2:

    first_value = data.iloc[0]["value"]
    last_value = data.iloc[-1]["value"]

    if last_value > first_value:
        st.info(
            f"The selected indicator increased from "
            f"{first_value:.2f} to {last_value:.2f}."
        )

    elif last_value < first_value:
        st.info(
            f"The selected indicator decreased from "
            f"{first_value:.2f} to {last_value:.2f}."
        )

    else:
        st.info(
            "The selected indicator remained unchanged."
        )