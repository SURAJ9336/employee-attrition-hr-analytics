import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

# Page Config
st.set_page_config(
    page_title="HR Analytics Dashboard",
    layout="wide"
)

st.title("HR Analytics Dashboard")

# =========================================
# ROW 1
# =========================================

col1, col2 = st.columns(2)

# -----------------------------
# Attrition Distribution
# -----------------------------
with col1:

    st.subheader("Attrition Distribution")

    attrition_counts = df["Attrition"].value_counts()

    fig1, ax1 = plt.subplots(figsize=(4,4))

    ax1.pie(
        attrition_counts,
        labels=attrition_counts.index,
        autopct='%1.1f%%'
    )

    st.pyplot(fig1)

# -----------------------------
# Age Distribution
# -----------------------------
with col2:

    st.subheader("Age Distribution")

    fig2, ax2 = plt.subplots(figsize=(5,4))

    ax2.hist(df["Age"], bins=20)

    ax2.set_xlabel("Age")
    ax2.set_ylabel("Employees")

    st.pyplot(fig2)

# =========================================
# ROW 2
# =========================================

col3, col4 = st.columns(2)

# -----------------------------
# Department Attrition
# -----------------------------
with col3:

    st.subheader("Department-wise Attrition")

    dept_attrition = pd.crosstab(
        df["Department"],
        df["Attrition"]
    )

    fig3, ax3 = plt.subplots(figsize=(6,4))

    dept_attrition.plot(
        kind='bar',
        ax=ax3
    )

    plt.xticks(rotation=0)

    st.pyplot(fig3)

# -----------------------------
# Overtime Impact
# -----------------------------
with col4:

    st.subheader("OverTime Impact")

    overtime_attrition = pd.crosstab(
        df["OverTime"],
        df["Attrition"]
    )

    fig4, ax4 = plt.subplots(figsize=(5,4))

    overtime_attrition.plot(
        kind='bar',
        ax=ax4
    )

    plt.xticks(rotation=0)

    st.pyplot(fig4)

# =========================================
# FOOTER
# =========================================

st.markdown("---")

st.markdown(
    "AI-Powered Employee Attrition Prediction and HR Analytics System"
)