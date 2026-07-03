import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("model_pickle")

# Page configuration
st.set_page_config(page_title="Auto MPG Prediction", page_icon="🚗")

st.title("🚗 Auto MPG Prediction")
st.write("Enter the vehicle specifications below and click **Predict**.")

# Input fields
displacement = st.number_input(
    "Displacement (cu.in.)",
    min_value=0.0,
    value=150.0,
    step=1.0
)

horsepower = st.number_input(
    "Horsepower",
    min_value=0.0,
    value=100.0,
    step=1.0
)

weight = st.number_input(
    "Weight (lbs)",
    min_value=0.0,
    value=3000.0,
    step=10.0
)

acceleration = st.number_input(
    "Acceleration (sec)",
    min_value=0.0,
    value=15.0,
    step=0.1
)

# Prediction
if st.button("Predict MPG"):
    input_data = np.array([[displacement, horsepower, weight, acceleration]])

    prediction = model.predict(input_data)

    st.success(f"Predicted MPG: **{prediction[0]:.2f}**")
