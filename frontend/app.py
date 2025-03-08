import streamlit as st
import requests

st.title("Python Fitness Tracker - Advanced")

st.sidebar.header("User Authentication")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
if st.sidebar.button("Login"):
    st.sidebar.success(f"Logged in as {username}")

st.sidebar.header("User Input")
steps = st.sidebar.number_input("Steps Walked", 0, 50000, 10000)
calories = st.sidebar.number_input("Calories Burned", 0, 5000, 500)
water = st.sidebar.number_input("Water Intake (Liters)", 0, 10, 2)
workouts = st.sidebar.number_input("Workouts Done", 0, 10, 1)

st.write(f"Steps: {steps}, Calories: {calories}, Water: {water}, Workouts: {workouts}")

if st.button("Predict Fitness Score"):
    try:
        response = requests.post("http://localhost:8000/predict", json={"features": [steps, calories, water, workouts]})
        st.success(f"Predicted Score: {response.json()['prediction']}")
    except:
        st.error("❌ Unable to connect to the backend server. Make sure it's running.")
