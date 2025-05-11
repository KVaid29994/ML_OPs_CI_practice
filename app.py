import streamlit as st

st.set_page_config(page_title="BMI Tracker", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stApp {
        background: linear-gradient(120deg, #a1c4fd, #c2e9fb);
        padding: 2rem;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)
# Title
st.title("💪 BMI & Health Tracker")

# Inputs
weight = st.number_input("Enter your weight (kg):", min_value=30.0, max_value=200.0, step=0.5)
height = st.number_input("Enter your height (cm):", min_value=100.0, max_value=250.0, step=0.5)

# Calculate BMI
if weight and height:
    bmi = weight / ((height / 100) ** 2)
    st.subheader(f"📊 Your BMI: {bmi:.2f}")

    # Health category
    if bmi < 18.5:
        status = "Underweight 😕"
    elif 18.5 <= bmi < 25:
        status = "Normal weight 😃"
    elif 25 <= bmi < 30:
        status = "Overweight 😐"
    else:
        status = "Obese 😟"
    
    st.success(f"Health Status: **{status}**")

    st.info("💡 Tip: Keep tracking and maintain a balanced lifestyle!")
