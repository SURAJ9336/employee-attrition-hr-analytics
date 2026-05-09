import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import streamlit as st


import matplotlib.pyplot as plt  # If needed



# -----------------------------
# LOGIN SYSTEM
# -----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("AttriSense AI Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        if username == "admin" and password == "admin123":

            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("Invalid Username or Password")

    st.stop()






df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Binary encoding
df['Attrition'] = df['Attrition'].apply(lambda x: 1 if x =='Yes' else 0)
df['Gender'] = df['Gender'].apply(lambda x: 1 if x =='Male' else 0)
df['Over18'] = df['Over18'].apply(lambda x: 1 if x =='Y' else 0)
df['OverTime'] = df['OverTime'].apply(lambda x: 1 if x =='Yes' else 0)

# One-hot encoding
df = df.join(pd.get_dummies(df['BusinessTravel'])).drop('BusinessTravel', axis=1)
df = df.join(pd.get_dummies(df['Department'], prefix='Department')).drop('Department', axis=1)
df = df.join(pd.get_dummies(df['EducationField'], prefix='Education')).drop('EducationField', axis=1)
df = df.join(pd.get_dummies(df['JobRole'], prefix='Role')).drop('JobRole', axis=1)
df = df.join(pd.get_dummies(df['MaritalStatus'], prefix='Status')).drop('MaritalStatus', axis=1)

# Drop useless columns
df = df.drop(['EmployeeNumber', 'EmployeeCount', 'Over18', 'StandardHours'], axis=1)


x, y = df.drop('Attrition', axis=1), df['Attrition']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = RandomForestClassifier(n_jobs=-1)
model.fit(x_train, y_train)


# STREAMLIT FRONTEND 
st.set_page_config(page_title="Employee Attrition Predictor", layout="centered")
st.title("Employee Attrition Prediction App")
st.write("This tool predicts if an employee is likely to leave the company based on their profile.")

#  USER INPUT FORM
st.subheader("Enter Employee Details")

age = st.slider("Age", 18, 60, 30)
gender = st.selectbox("Gender", ["Male", "Female"])
monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=50000, value=15000)
job_level = st.selectbox("Job Level", [1, 2, 3, 4, 5])
years_at_company = st.slider("Years at Company", 0, 40, 5)
overtime = st.selectbox("OverTime", ["Yes", "No"])
distance_from_home = st.slider("Distance From Home (km)", 1, 50, 10)
job_satisfaction = st.slider("Job Satisfaction (1=Low, 4=High)", 1, 4, 3)
environment_satisfaction = st.slider("Environment Satisfaction (1=Low, 4=High)", 1, 4, 3)

#  Create Input Data
input_data = pd.DataFrame({
'Age': [age],
'Gender': [1 if gender == "Male" else 0],
'MonthlyIncome': [monthly_income],
'JobLevel': [job_level],
'YearsAtCompany': [years_at_company],
'OverTime': [1 if overtime == "Yes" else 0],
'DistanceFromHome': [distance_from_home],
'JobSatisfaction': [job_satisfaction],
'EnvironmentSatisfaction': [environment_satisfaction],
  
})


# Fill missing columns with 0
for col in x.columns:
    if col not in input_data.columns:
        input_data[col] = 0


input_data = input_data[x.columns]


#  Predict 
if st.button("Predict Attrition"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

        # Save Prediction History

    history_data = pd.DataFrame({
        "Age": [age],
        "MonthlyIncome": [monthly_income],
        "Prediction": [
            "Leave" if prediction == 1 else "Stay"
        ],
        "Confidence": [
            round(
                probability * 100,
                2
            ) if prediction == 1
            else round(
                (1 - probability) * 100,
                2
            )
        ]
    })

    history_data.to_csv(
        "history.csv",
        mode='a',
        header=False,
        index=False
    )

    if prediction == 1:
        st.error(f" This employee is likely to leave.(Confidence: {round(probability * 100, 2)}%)")
    else:
        st.success(f" This employee is likely to stay.(Confidence: {round((1 - probability) * 100, 2)}%)")


st.subheader("Prediction History")

history = pd.read_csv("history.csv")

st.dataframe(history)

csv = history.to_csv(index=False)

st.download_button(
    label="Download Prediction History",
    data=csv,
    file_name='prediction_history.csv',
    mime='text/csv'
)
