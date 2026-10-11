import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

st.title("🤖 Health Burden Prediction")

df = pd.read_csv("Dataset/ml_training_data.csv")

features = [
    "literacy_rate",
    "sanitation_access_pct",
    "safe_water_access_pct",
    "doctor_density_per_10k",
    "income_index",
    "urbanization_pct",
    "hospital_beds_per_10k"
]

target = "health_burden_index"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

pred = model.predict(X_test)

mae = mean_absolute_error(y_test, pred)
mse = mean_squared_error(y_test, pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, pred)

st.divider()

c1, c2, c3, c4 = st.columns(4)

c1.metric("MAE", f"{mae:.2f}")
c2.metric("MSE", f"{mse:.2f}")
c3.metric("RMSE", f"{rmse:.2f}")
c4.metric("R²", f"{r2:.2f}")

st.divider()

st.subheader("🎯 Actual vs Predicted")

result = pd.DataFrame({
    "Actual": y_test,
    "Predicted": pred
})

fig = px.scatter(
    result,
    x="Actual",
    y="Predicted",
    title="Actual vs Predicted Health Burden"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

st.subheader("📊 Feature Influence")

coef = pd.DataFrame({
    "Feature": features,
    "Coefficient": model.coef_
})

fig2 = px.bar(
    coef,
    x="Coefficient",
    y="Feature",
    orientation="h",
    title="Model Coefficients"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

st.divider()

st.subheader("🔮 Predict Health Burden")

values = {}

for feature in features:
    values[feature] = st.number_input(
        feature.replace("_", " ").title(),
        value=float(df[feature].mean())
    )

input_df = pd.DataFrame([values])

prediction = model.predict(input_df)[0]

st.metric(
    "Predicted Health Burden Index",
    f"{prediction:.2f}"
)