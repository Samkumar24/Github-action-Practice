import streamlit as st

st.title("Simple Calculator")

a = st.number_input("Enter first number", value=0)
b = st.number_input("Enter second number", value=0)

st.subheader("Results")
st.write("Addition:", a + b)
st.write("Multiplication:", a * b)
