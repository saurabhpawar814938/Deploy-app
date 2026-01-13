import streamlit as st
import google.generativeai as genai

st.title("Welcome to my streamlit app.")

user_input = st.text_input("Ask me anything")


genai.configure(api_key = "AIzaSyBsY5WV-ucMyP84yoq6gSfwWZ3a1I8KCo8")

model = genai.GenerativeModel("models/gemini-2.5-flash")
if user_input:
    response = model.generate_content(user_input)
    st.write("Response: ", response.text)