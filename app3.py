import streamlit as st
st.title("Mske a simple calculator...")

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

operation = st.selectbox("choose operation:" , ["sum", "diff", "mul", "div"])

if st.button("Calculator"):
    if operation=="sum":
        result = num1 + num2
    if operation=="diff":
        result = num1 - num2
    if operation=="mul":
        result = num1 * num2
    if operation=="div":
        if num2 == 0:
            result = ("Can't divide by zero.")
        else:
            result = num1 / num2
    st.write("Result", result)