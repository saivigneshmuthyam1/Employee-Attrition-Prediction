import streamlit as st
import joblib
import traceback

try:
    model = joblib.load("attrition_model_v2.pkl")
    st.success("Model loaded successfully")

except Exception as e:
    st.error(str(e))
    st.code(traceback.format_exc())
    st.stop()
