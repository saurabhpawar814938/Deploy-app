import streamlit as st

st.title("Basic commands in streamlit...")
name = st.text_input("Enter your name:")


date = st.date_input("Enter your date of birth:")
if st.button("Submit"):
    st.write("Hello ", name, "your date of birth is : " ,date)
