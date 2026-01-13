import streamlit as st
st.title("Basic command like slider button, etc")

age = st.slider("Enter your age: ", 0,100)
city = st.selectbox("Choose your city: ", ["delhi", "pune","mumbai","banglore"] )
gender = st.radio("Select your gender:", ["male", "female", "other"])
if st.button("show details"):
    st.write("age:", age)
    st.write("city:", city)
    st.write("gender:", gender)

