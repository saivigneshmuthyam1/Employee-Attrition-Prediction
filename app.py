import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Employee Attrition Predictor",
    layout="wide"
)

model = joblib.load("attrition_model_v2.pkl")

st.title("AI Powered Employee Attrition Prediction System")

st.write("Predict employee attrition risk using Machine Learning")
