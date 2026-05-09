# AI-Powered Employee Attrition Prediction and HR Analytics System

## Overview

The AI-Powered Employee Attrition Prediction and HR Analytics System is a machine learning-based web application developed to predict whether an employee is likely to leave an organization based on various HR-related factors. The system helps organizations analyze employee behavior patterns and supports data-driven workforce management.

The project uses Machine Learning algorithms such as Random Forest Classifier and Logistic Regression to perform employee attrition prediction. An interactive Streamlit-based user interface is integrated to provide real-time predictions, HR analytics visualization, prediction history tracking, and downloadable reports.

This project is designed for academic, research, and educational purposes and can also serve as a portfolio-ready machine learning application.

---

# Live Demo

🔗 Deployment Link:  
https://attrisense-ai.streamlit.app/



# Key Features

- Employee Attrition Prediction
- HR Analytics Dashboard
- Machine Learning-Based Prediction
- Prediction Confidence Score
- Prediction History Storage
- Download Prediction Reports
- Interactive Streamlit User Interface
- Login Authentication Page
- Data Visualization using Matplotlib
- Real-Time User Input Prediction

---

# Technologies Used

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| Machine Learning | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib |
| Dataset | IBM HR Analytics Dataset |

---

# Machine Learning Algorithms

The following algorithms are used in this project:

- Random Forest Classifier
- Logistic Regression

### Model Accuracy

| Algorithm | Accuracy |
|---|---|
| Random Forest Classifier | 85% – 87% |
| Logistic Regression | 80% – 82% |

---

# Dataset Information

- Dataset Name: IBM HR Analytics Employee Attrition Dataset
- Total Records: 1470
- Features: 35+
- Target Variable: Attrition

### Important Features Used

- Age
- Monthly Income
- Job Level
- OverTime
- Distance From Home
- Job Satisfaction
- Environment Satisfaction
- Years At Company

---

# Project Modules

## 1. Login Module
Provides secure login access for users before accessing the system.

---

## 2. Employee Attrition Prediction Module
Predicts whether an employee is likely to leave the company based on input data.

---

## 3. HR Analytics Dashboard
Displays visual analytics including:

- Attrition Distribution
- Department-wise Attrition
- Overtime Impact
- Employee Age Distribution

---

## 4. Prediction History Module
Stores previous prediction records and displays them in tabular format.

---

## 5. Download Report Module
Allows users to download prediction history as CSV reports.

---

# Project Structure

```bash
employee-attrition-hr-analytics/
│
├── app.py
├── dashboard.py
├── login.py
├── model_training.ipynb
├── history.csv
├── WA_Fn-UseC_-HR-Employee-Attrition.csv
├── requirements.txt
├── README.md
├── .gitignore
└── assets/
```

---

# Screenshots

## Login Page


---

## Employee Prediction Page



---

## HR Analytics Dashboard



---

## Prediction History



---

# Installation and Setup

## Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/employee-attrition-hr-analytics.git
```

---

## Step 2: Open Project Folder

```bash
cd employee-attrition-hr-analytics
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Run Application

```bash
python -m streamlit run app.py
```

---

## Step 5: Run Dashboard

```bash
python -m streamlit run dashboard.py
```

---

## Step 6: Run Login Page

```bash
python -m streamlit run login.py
```

---

# Data Preprocessing Techniques

The following preprocessing techniques are applied:

- Binary Encoding
- One-Hot Encoding
- Feature Selection
- Removal of Unnecessary Columns
- Train-Test Splitting

---

# Future Enhancements

- Batch Employee Prediction using CSV Upload
- Explainable AI Integration
- Cloud Database Integration
- Multi-User Authentication
- Advanced HR Analytics
- Email Notification System
- PDF Report Generation

---

# Use Cases

- HR Attrition Analysis
- Employee Retention Strategy
- Workforce Management
- HR Decision Support
- Machine Learning Academic Project
- Research Paper Implementation

---

# Research Area

Artificial Intelligence and Machine Learning

---

# Author

**Suraj Kumar**  
Final Year Student  
Computer Science Engineering (AI & ML)

---

# License

This project is developed for academic and educational purposes only.

---

# Acknowledgment

- IBM HR Analytics Dataset
- Streamlit Documentation
- Scikit-learn Documentation
- Python Open Source Community
