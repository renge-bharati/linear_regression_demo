import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("Salary Prediction App 💼")

exp = st.number_input("Experience in Years", 0.0)

if st.button("Predict"):
    result = model.predict([[exp]])
    st.write(f"Expected Salary: ₹{result[0]:.2f}")
