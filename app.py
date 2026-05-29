# import streamlit as st
# import pandas as pd
# import joblib

# # ---------------------------
# # PAGE CONFIG
# # ---------------------------
# st.set_page_config(
#     page_title="AI Employee Attrition Prediction",
#     page_icon="📊",
#     layout="wide"
# )

# # ---------------------------
# # LOAD MODEL
# # ---------------------------
# model = joblib.load("attrition_model_v2.pkl")

# THRESHOLD = 0.40

# # ---------------------------
# # TITLE
# # ---------------------------
# st.title("📊 AI Powered Employee Attrition Prediction System")
# st.markdown("Predict employee attrition risk using Machine Learning")

# # ---------------------------
# # SIDEBAR INPUTS
# # ---------------------------
# st.sidebar.header("Employee Information")

# # Personal Information
# age = st.sidebar.number_input("Age", 18, 60, 30)
# gender = st.sidebar.selectbox(
#     "Gender",
#     ["Female", "Male"]
# )

# marital_status = st.sidebar.selectbox(
#     "Marital Status",
#     ["Divorced", "Married", "Single"]
# )

# # Job Information
# business_travel = st.sidebar.selectbox(
#     "Business Travel",
#     ["Non-Travel", "Travel_Frequently", "Travel_Rarely"]
# )

# department = st.sidebar.selectbox(
#     "Department",
#     ["Human Resources", "Research & Development", "Sales"]
# )

# job_role = st.sidebar.selectbox(
#     "Job Role",
#     [
#         "Healthcare Representative",
#         "Human Resources",
#         "Laboratory Technician",
#         "Manager",
#         "Manufacturing Director",
#         "Research Director",
#         "Research Scientist",
#         "Sales Executive",
#         "Sales Representative"
#     ]
# )

# overtime = st.sidebar.selectbox(
#     "OverTime",
#     ["No", "Yes"]
# )

# # Compensation
# monthly_income = st.sidebar.number_input(
#     "Monthly Income",
#     1000,
#     25000,
#     5000
# )

# # Satisfaction
# job_satisfaction = st.sidebar.selectbox(
#     "Job Satisfaction",
#     [1, 2, 3, 4]
# )

# environment_satisfaction = st.sidebar.selectbox(
#     "Environment Satisfaction",
#     [1, 2, 3, 4]
# )

# # Experience
# years_at_company = st.sidebar.number_input(
#     "Years At Company",
#     0,
#     40,
#     5
# )

# total_working_years = st.sidebar.number_input(
#     "Total Working Years",
#     0,
#     40,
#     8
# )

# # ---------------------------
# # PREDICT BUTTON
# # ---------------------------
# if st.sidebar.button("Predict Attrition"):

#     employee = pd.DataFrame([{
#         "Age": age,
#         "BusinessTravel": business_travel,
#         "DailyRate": 800,
#         "Department": department,
#         "DistanceFromHome": 5,
#         "Education": 3,
#         "EducationField": "Life Sciences",
#         "EnvironmentSatisfaction": environment_satisfaction,
#         "Gender": gender,
#         "HourlyRate": 60,
#         "JobInvolvement": 3,
#         "JobLevel": 2,
#         "JobRole": job_role,
#         "JobSatisfaction": job_satisfaction,
#         "MaritalStatus": marital_status,
#         "MonthlyIncome": monthly_income,
#         "MonthlyRate": 15000,
#         "NumCompaniesWorked": 2,
#         "OverTime": overtime,
#         "PercentSalaryHike": 15,
#         "PerformanceRating": 3,
#         "RelationshipSatisfaction": 3,
#         "StockOptionLevel": 1,
#         "TotalWorkingYears": total_working_years,
#         "TrainingTimesLastYear": 2,
#         "WorkLifeBalance": 3,
#         "YearsAtCompany": years_at_company,
#         "YearsInCurrentRole": 3,
#         "YearsSinceLastPromotion": 1,
#         "YearsWithCurrManager": 3
#     }])

#     probability = model.predict_proba(employee)[0][1]

#     prediction = (
#         "Likely To Leave"
#         if probability >= THRESHOLD
#         else "Likely To Stay"
#     )

#     if probability < 0.30:
#         risk = "Low Risk"
#     elif probability < 0.70:
#         risk = "Medium Risk"
#     else:
#         risk = "High Risk"

#     # ---------------------------
#     # METRICS
#     # ---------------------------
#     col1, col2, col3 = st.columns(3)

#     with col1:
#         st.metric(
#             "Attrition Probability",
#             f"{probability*100:.2f}%"
#         )

#     with col2:
#         st.metric(
#             "Risk Level",
#             risk
#         )

#     with col3:
#         st.metric(
#             "Prediction",
#             prediction
#         )

#     # ---------------------------
#     # PROGRESS BAR
#     # ---------------------------
#     st.subheader("Risk Meter")
#     st.progress(float(probability))

#     # ---------------------------
#     # RISK FACTORS
#     # ---------------------------
#     st.subheader("Top Risk Factors")

#     risk_factors = []

#     if overtime == "Yes":
#         risk_factors.append(
#             "Employee works overtime"
#         )

#     if monthly_income < 5000:
#         risk_factors.append(
#             "Below average salary"
#         )

#     if job_satisfaction <= 2:
#         risk_factors.append(
#             "Low job satisfaction"
#         )

#     if environment_satisfaction <= 2:
#         risk_factors.append(
#             "Low environment satisfaction"
#         )

#     if years_at_company < 3:
#         risk_factors.append(
#             "Short company tenure"
#         )

#     if risk_factors:
#         for factor in risk_factors:
#             st.warning(factor)
#     else:
#         st.success(
#             "No major attrition indicators detected."
#         )

#     # ---------------------------
#     # HR RECOMMENDATIONS
#     # ---------------------------
#     st.subheader("HR Recommendations")

#     if risk == "High Risk":

#         st.error("""
#         • Immediate HR discussion

#         • Review compensation

#         • Reduce overtime

#         • Explore promotion opportunities

#         • Conduct retention interview
#         """)

#     elif risk == "Medium Risk":

#         st.warning("""
#         • Increase employee engagement

#         • Review workload

#         • Schedule periodic check-ins
#         """)

#     else:

#         st.success("""
#         • Maintain current engagement strategy

#         • Continue career development initiatives
#         """)

#     # ---------------------------
#     # INPUT SUMMARY
#     # ---------------------------
#     st.subheader("Employee Data")
#     st.dataframe(employee)


import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="📊",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.metric-card {
    background-color: #1E293B;
    padding: 20px;
    border-radius: 15px;
}

h1,h2,h3 {
    color:white;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

model = joblib.load("attrition_model_v2.pkl")

THRESHOLD = 0.40

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📊 AI Powered Employee Attrition Prediction System")

st.markdown(
"""
Predict employee attrition risk using Machine Learning.
"""
)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("Employee Information")

# PERSONAL

st.sidebar.subheader("Personal Information")

age = st.sidebar.number_input(
    "Age",
    18,
    60,
    30
)

gender = st.sidebar.selectbox(
    "Gender",
    ["Female", "Male"]
)

marital_status = st.sidebar.selectbox(
    "Marital Status",
    ["Divorced", "Married", "Single"]
)

education = st.sidebar.selectbox(
    "Education",
    [1,2,3,4,5]
)

education_field = st.sidebar.selectbox(
    "Education Field",
    [
        "Human Resources",
        "Life Sciences",
        "Marketing",
        "Medical",
        "Other",
        "Technical Degree"
    ]
)

# JOB

st.sidebar.subheader("Job Information")

business_travel = st.sidebar.selectbox(
    "Business Travel",
    [
        "Non-Travel",
        "Travel_Frequently",
        "Travel_Rarely"
    ]
)

department = st.sidebar.selectbox(
    "Department",
    [
        "Human Resources",
        "Research & Development",
        "Sales"
    ]
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

job_level = st.sidebar.selectbox(
    "Job Level",
    [1,2,3,4,5]
)

job_involvement = st.sidebar.selectbox(
    "Job Involvement",
    [1,2,3,4]
)

overtime = st.sidebar.selectbox(
    "OverTime",
    ["No","Yes"]
)

# COMPENSATION

st.sidebar.subheader("Compensation")

monthly_income = st.sidebar.number_input(
    "Monthly Income",
    1000,
    25000,
    5000
)

daily_rate = st.sidebar.number_input(
    "Daily Rate",
    100,
    2000,
    800
)

hourly_rate = st.sidebar.number_input(
    "Hourly Rate",
    10,
    100,
    60
)

monthly_rate = st.sidebar.number_input(
    "Monthly Rate",
    1000,
    30000,
    15000
)

percent_salary_hike = st.sidebar.number_input(
    "Percent Salary Hike",
    0,
    50,
    15
)

stock_option_level = st.sidebar.selectbox(
    "Stock Option Level",
    [0,1,2,3]
)

# SATISFACTION

st.sidebar.subheader("Satisfaction")

job_satisfaction = st.sidebar.selectbox(
    "Job Satisfaction",
    [1,2,3,4]
)

environment_satisfaction = st.sidebar.selectbox(
    "Environment Satisfaction",
    [1,2,3,4]
)

relationship_satisfaction = st.sidebar.selectbox(
    "Relationship Satisfaction",
    [1,2,3,4]
)

work_life_balance = st.sidebar.selectbox(
    "Work Life Balance",
    [1,2,3,4]
)

# EXPERIENCE

st.sidebar.subheader("Experience")

distance_from_home = st.sidebar.number_input(
    "Distance From Home",
    0,
    50,
    5
)

total_working_years = st.sidebar.number_input(
    "Total Working Years",
    0,
    40,
    8
)

years_at_company = st.sidebar.number_input(
    "Years At Company",
    0,
    40,
    5
)

years_in_current_role = st.sidebar.number_input(
    "Years In Current Role",
    0,
    20,
    3
)

years_since_last_promotion = st.sidebar.number_input(
    "Years Since Last Promotion",
    0,
    20,
    1
)

years_with_curr_manager = st.sidebar.number_input(
    "Years With Current Manager",
    0,
    20,
    3
)

num_companies_worked = st.sidebar.number_input(
    "Companies Worked",
    0,
    10,
    2
)

# --------------------------------------------------
# PREDICT
# --------------------------------------------------

if st.sidebar.button("Predict Attrition"):

    employee = pd.DataFrame([{

        "Age": age,
        "BusinessTravel": business_travel,
        "DailyRate": daily_rate,
        "Department": department,
        "DistanceFromHome": distance_from_home,
        "Education": education,
        "EducationField": education_field,
        "EnvironmentSatisfaction": environment_satisfaction,
        "Gender": gender,
        "HourlyRate": hourly_rate,
        "JobInvolvement": job_involvement,
        "JobLevel": job_level,
        "JobRole": job_role,
        "JobSatisfaction": job_satisfaction,
        "MaritalStatus": marital_status,
        "MonthlyIncome": monthly_income,
        "MonthlyRate": monthly_rate,
        "NumCompaniesWorked": num_companies_worked,
        "OverTime": overtime,
        "PercentSalaryHike": percent_salary_hike,
        "PerformanceRating": 3,
        "RelationshipSatisfaction": relationship_satisfaction,
        "StockOptionLevel": stock_option_level,
        "TotalWorkingYears": total_working_years,
        "TrainingTimesLastYear": 2,
        "WorkLifeBalance": work_life_balance,
        "YearsAtCompany": years_at_company,
        "YearsInCurrentRole": years_in_current_role,
        "YearsSinceLastPromotion": years_since_last_promotion,
        "YearsWithCurrManager": years_with_curr_manager
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

    # METRICS

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Attrition Probability",
        f"{probability*100:.2f}%"
    )

    col2.metric(
        "Risk Level",
        risk
    )

    col3.metric(
        "Prediction",
        prediction
    )

    # GAUGE

    st.subheader("📊 Attrition Risk Gauge")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        title={'text': "Attrition Risk (%)"},
        gauge={
            'axis': {'range': [0,100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0,30], 'color': "green"},
                {'range': [30,70], 'color': "gold"},
                {'range': [70,100], 'color': "red"}
            ]
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # RISK FACTORS

    st.subheader("Top Risk Factors")

    risk_factors = []

    if overtime == "Yes":
        risk_factors.append("Employee works overtime")

    if monthly_income < 5000:
        risk_factors.append("Below average salary")

    if job_satisfaction <= 2:
        risk_factors.append("Low job satisfaction")

    if environment_satisfaction <= 2:
        risk_factors.append("Low environment satisfaction")

    if years_at_company < 3:
        risk_factors.append("Short company tenure")

    if len(risk_factors) == 0:
        st.success(
            "No major attrition indicators detected."
        )

    else:
        for factor in risk_factors:
            st.warning(factor)

    # HR RECOMMENDATIONS

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

    # REPORT

    st.subheader("📄 Download Report")

    report = pd.DataFrame({
        "Probability":[round(probability*100,2)],
        "Risk":[risk],
        "Prediction":[prediction]
    })

    csv = report.to_csv(index=False)

    st.download_button(
        "Download Prediction Report",
        csv,
        "employee_attrition_report.csv",
        "text/csv"
    )

    # DATA

    st.subheader("Employee Data")

    st.dataframe(employee)
