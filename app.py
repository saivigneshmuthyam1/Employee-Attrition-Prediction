

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

        # ======================================
    # PROFESSIONAL KPI CARDS
    # ======================================

    st.markdown("## Prediction Results")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div style="
            background:#1E293B;
            padding:20px;
            border-radius:15px;
            text-align:center;">
            <h4>Attrition Probability</h4>
            <h2>{probability*100:.2f}%</h2>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div style="
            background:#1E293B;
            padding:20px;
            border-radius:15px;
            text-align:center;">
            <h4>Risk Level</h4>
            <h2>{risk}</h2>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div style="
            background:#1E293B;
            padding:20px;
            border-radius:15px;
            text-align:center;">
            <h4>Prediction</h4>
            <h2>{prediction}</h2>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ======================================
    # GAUGE + RISK FACTORS
    # ======================================

    #left, right = st.columns([2,1])
    gauge_col, factor_col = st.columns([1.5,1])
    with gauge_col:
        st.subheader("📊 Attrition Risk Gauge")
        st.plotly_chart(fig)

    with factor_col:
        st.subheader("⚠️ Risk Factors")

    with left:

        st.subheader("📊 Attrition Risk Gauge")
    
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=probability * 100,
            title={'text': "Attrition Risk (%)"},
            gauge={
                'axis': {'range': [0,100]},
                'bar': {'color': "#2563EB"},
                'steps': [
                    {'range':[0,30],'color':"#22C55E"},
                    {'range':[30,70],'color':"#EAB308"},
                    {'range':[70,100],'color':"#EF4444"}
                ]
            }
        ))

        fig.update_layout(
            height=350,
            margin=dict(l=0,r=0,t=20,b=0),
            paper_bgcolor="#0E1117",
            font_color="white"
        )
    
        st.plotly_chart(
            fig,
            use_container_width=False
        )
    
    with right:

        st.subheader("⚠️ Risk Factors")

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
                "No major attrition indicators."
            )
        else:
            for factor in risk_factors:
                st.warning(factor)

    st.markdown("---")

    # ======================================
    # HR RECOMMENDATIONS
    # ======================================

    st.subheader("🎯 HR Recommendations")

    if risk == "High Risk":

        st.error("""
• Immediate HR discussion

• Review compensation package

• Reduce overtime burden

• Explore promotion opportunities

• Conduct retention interview
""")

    elif risk == "Medium Risk":

        st.warning("""
• Increase employee engagement

• Review workload

• Schedule periodic check-ins

• Discuss career development
""")

    else:

        st.success("""
• Maintain current engagement strategy

• Continue career development initiatives

• Recognize employee contributions
""")

    st.markdown("---")

    # ======================================
    # DOWNLOAD REPORT
    # ======================================

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

    # ======================================
    # COLLAPSIBLE EMPLOYEE DATA
    # ======================================

    with st.expander("📋 Employee Input Summary"):

        display_df = employee.T
        display_df.columns = ["Value"]
    
        st.dataframe(
            display_df,
            use_container_width=True
    )

    st.markdown("---")

    st.markdown("---")

    m1,m2,m3,m4 = st.columns(4)
    
    m1.metric("Accuracy","73.1%")
    m2.metric("Recall","78.7%")
    m3.metric("Precision","34.9%")
    m4.metric("ROC-AUC","80.3%")
