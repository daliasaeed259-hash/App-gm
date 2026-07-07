import streamlit as st
import google.generativeai as genai

st.title("مساعدي الذكي")
genai.configure(api_key="ضع_مفتاح_الـ_API_هنا")
model = genai.GenerativeModel('gemini-1.5-flash')

prompt = st.text_input("اسألني أي شيء:")

if prompt:
    response = model.generate_content(prompt)
    st.write(response.text)
