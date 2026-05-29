# import streamlit as st
# import joblib
# import traceback

# try:
#     model = joblib.load("attrition_model_v2.pkl")
#     st.success("Model loaded successfully")

# except Exception as e:
#     st.error(str(e))
#     st.code(traceback.format_exc())
#     st.stop()
st.title("AI Powered Employee Attrition Prediction System")

st.sidebar.header("Employee Information")

age = st.sidebar.number_input("Age",18,60,30)

monthly_income = st.sidebar.number_input(
    "Monthly Income",
    1000,
    25000,
    5000
)

# other inputs ...

if st.sidebar.button("Predict Attrition"):
    ...
