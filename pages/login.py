import streamlit as st
import subprocess

st.set_page_config(
    page_title="Login",
    layout="centered"
)

st.title("Employee Attrition System Login")

username = st.text_input("Username")
password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if username == "suraj" and password == "12345":

        st.success("Login Successful")

        st.markdown(
            "Run the main application using terminal:"
        )

        st.code(
            "python -m streamlit run app.py"
        )

    else:
        st.error("Invalid Username or Password")