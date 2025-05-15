import streamlit as st
from parser import ResumeParser

st.title("AI Resume Parser")

uploaded_file = st.file_uploader("Upload a Resume", type=["pdf"])
if uploaded_file:
    parser = ResumeParser(uploaded_file)
    st.write("👤 Name:", parser.get_name())
    st.write("🛠️ Skills:", parser.get_skills())
    st.write("🎓 Education:", parser.get_education())
