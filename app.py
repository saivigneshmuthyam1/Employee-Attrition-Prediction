# import streamlit as st
# import pandas as pd
# import joblib

# model = joblib.load("attrition_model_v2.pkl")

# st.title("AI Powered Employee Attrition Prediction System")
# st.title("AI Powered Employee Attrition Prediction System")

# st.sidebar.header("Employee Information")

# age = st.sidebar.number_input("Age",18,60,30)

# monthly_income = st.sidebar.number_input(
#     "Monthly Income",
#     1000,
#     25000,
#     5000
# )

# # other inputs ...

# if st.sidebar.button("Predict Attrition"):
#     ...

import streamlit as st
import pandas as pd
import joblib

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="AI Employee Attrition Prediction",
    page_icon="📊",
    layout="wide"
)

# ---------------------------
# LOAD MODEL
# ---------------------------
model = joblib.load("attrition_model_v2.pkl")

THRESHOLD = 0.40

# ---------------------------
# TITLE
# ---------------------------
st.title("📊 AI Powered Employee Attrition Prediction System")
st.markdown("Predict employee attrition risk using Machine Learning")

# ---------------------------
# SIDEBAR INPUTS
# ---------------------------
st.sidebar.header("Employee Information")

# Personal Information
age = st.sidebar.number_input("Age", 18, 60, 30)
gender = st.sidebar.selectbox(
    "Gender",
    ["Female", "Male"]
)

marital_status = st.sidebar.selectbox(
    "Marital Status",
    ["Divorced", "Married", "Single"]
)

# Job Information
business_travel = st.sidebar.selectbox(
    "Business Travel",
    ["Non-Travel", "Travel_Frequently", "Travel_Rarely"]
)

department = st.sidebar.selectbox(
    "Department",
    ["Human Resources", "Research & Development", "Sales"]
)

job_role = st.sidebar.selectbox(
    "Job Role",
    [
        "Healthcare Representative",
        "Human Resources",
        "Laboratory Technician",
        "Manager",
        "Manufacturing Director",
        "Research Director",
        "Research Scientist",
        "Sales Executive",
        "Sales Representative"
    ]
)

overtime = st.sidebar.selectbox(
    "OverTime",
    ["No", "Yes"]
)

# Compensation
monthly_income = st.sidebar.number_input(
    "Monthly Income",
    1000,
    25000,
    5000
)

# Satisfaction
job_satisfaction = st.sidebar.selectbox(
    "Job Satisfaction",
    [1, 2, 3, 4]
)

environment_satisfaction = st.sidebar.selectbox(
    "Environment Satisfaction",
    [1, 2, 3, 4]
)

# Experience
years_at_company = st.sidebar.number_input(
    "Years At Company",
    0,
    40,
    5
)

total_working_years = st.sidebar.number_input(
    "Total Working Years",
    0,
    40,
    8
)

# ---------------------------
# PREDICT BUTTON
# ---------------------------
if st.sidebar.button("Predict Attrition"):

    employee = pd.DataFrame([{
        "Age": age,
        "BusinessTravel": business_travel,
        "DailyRate": 800,
        "Department": department,
        "DistanceFromHome": 5,
        "Education": 3,
        "EducationField": "Life Sciences",
        "EnvironmentSatisfaction": environment_satisfaction,
        "Gender": gender,
        "HourlyRate": 60,
        "JobInvolvement": 3,
        "JobLevel": 2,
        "JobRole": job_role,
        "JobSatisfaction": job_satisfaction,
        "MaritalStatus": marital_status,
        "MonthlyIncome": monthly_income,
        "MonthlyRate": 15000,
        "NumCompaniesWorked": 2,
        "OverTime": overtime,
        "PercentSalaryHike": 15,
        "PerformanceRating": 3,
        "RelationshipSatisfaction": 3,
        "StockOptionLevel": 1,
        "TotalWorkingYears": total_working_years,
        "TrainingTimesLastYear": 2,
        "WorkLifeBalance": 3,
        "YearsAtCompany": years_at_company,
        "YearsInCurrentRole": 3,
        "YearsSinceLastPromotion": 1,
        "YearsWithCurrManager": 3
    }])

    probability = model.predict_proba(employee)[0][1]

    prediction = (
        "Likely To Leave"
        if probability >= THRESHOLD
        else "Likely To Stay"
    )

    if probability < 0.30:
        risk = "Low Risk"
    elif probability < 0.70:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    # ---------------------------
    # METRICS
    # ---------------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Attrition Probability",
            f"{probability*100:.2f}%"
        )

    with col2:
        st.metric(
            "Risk Level",
            risk
        )

    with col3:
        st.metric(
            "Prediction",
            prediction
        )

    # ---------------------------
    # PROGRESS BAR
    # ---------------------------
    st.subheader("Risk Meter")
    st.progress(float(probability))

    # ---------------------------
    # RISK FACTORS
    # ---------------------------
    st.subheader("Top Risk Factors")

    risk_factors = []

    if overtime == "Yes":
        risk_factors.append(
            "Employee works overtime"
        )

    if monthly_income < 5000:
        risk_factors.append(
            "Below average salary"
        )

    if job_satisfaction <= 2:
        risk_factors.append(
            "Low job satisfaction"
        )

    if environment_satisfaction <= 2:
        risk_factors.append(
            "Low environment satisfaction"
        )

    if years_at_company < 3:
        risk_factors.append(
            "Short company tenure"
        )

    if risk_factors:
        for factor in risk_factors:
            st.warning(factor)
    else:
        st.success(
            "No major attrition indicators detected."
        )

    # ---------------------------
    # HR RECOMMENDATIONS
    # ---------------------------
    st.subheader("HR Recommendations")

    if risk == "High Risk":

        st.error("""
        • Immediate HR discussion

        • Review compensation

        • Reduce overtime

        • Explore promotion opportunities

        • Conduct retention interview
        """)

    elif risk == "Medium Risk":

        st.warning("""
        • Increase employee engagement

        • Review workload

        • Schedule periodic check-ins
        """)

    else:

        st.success("""
        • Maintain current engagement strategy

        • Continue career development initiatives
        """)

    # ---------------------------
    # INPUT SUMMARY
    # ---------------------------
    st.subheader("Employee Data")
    st.dataframe(employee)
