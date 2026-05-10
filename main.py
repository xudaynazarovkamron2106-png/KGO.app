import streamlit as st
import google.generativeai as genai

# DIQQAT: Bu yerda kalit yo'q, u Streamlit sozlamalaridan olinadi
API_KEY = st.secrets["GEMINI_API_KEY"] 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🌐 KGO GLOBAL APP-AI")
query = st.text_input("Ilova nomini yozing:")

if st.button("AI TAHLILI"):
    if query:
        response = model.generate_content(query)
        st.write(response.text)
